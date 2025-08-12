import json
import os
import pandas as pd

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STRATEGY_PATH = os.path.join(BASE_DIR, "vialume_current_strategy.json")
LOG_PATH = os.path.join(BASE_DIR, "vialume_signal_log.csv")

def load_strategy():
    with open(STRATEGY_PATH, "r") as file:
        return json.load(file)

def save_strategy(strategy):
    with open(STRATEGY_PATH, "w") as file:
        json.dump(strategy, file, indent=2)

def evaluate_signals(df, eval_window, threshold):
    recent = df.tail(eval_window)
    if recent.empty or "outcome" not in recent.columns:
        print("📭 Not enough signal outcomes to evaluate.")
        return None, None

    try:
        success_rate = recent["outcome"].astype(float).mean()
        return success_rate >= threshold, success_rate
    except Exception as e:
        print(f"⚠️ Evaluation failed: {e}")
        return None, None

def adjust_parameter(value, success, rate, increase=True):
    if success:
        return value * (1 + rate) if increase else value
    else:
        return value * (1 - rate) if increase else value

def learn_and_update_strategy():
    if not os.path.exists(LOG_PATH):
        print("📭 No signal log found. Cannot learn without trade outcomes.")
        return

    df = pd.read_csv(LOG_PATH)
    if "outcome" not in df.columns:
        print("⚠️ Signal log missing 'outcome' column.")
        return

    strategy = load_strategy()
    config = strategy.get("learning_config", {})

    eval_window = config.get("evaluation_window", 10)
    threshold = config.get("performance_threshold", 0.6)
    adjustment_rate = config.get("adjustment_rate", 0.1)

    success, rate = evaluate_signals(df, eval_window, threshold)
    
    if success is None:
        print("📭 Not enough data to evaluate performance.")
        return

    if success:
        print(f"✅ Success rate {rate:.2f} — keeping parameters.")
    else:
        print(f"🔧 Success rate {rate:.2f} — updating parameters...")

        for key, indicator in strategy.get("indicators", {}).items():
            weight = indicator.get("weight", 1.0)
            indicator["weight"] = adjust_parameter(weight, success, adjustment_rate, increase=False)

    save_strategy(strategy)
    print("💾 Strategy updated and saved.")

if __name__ == "__main__":
    learn_and_update_strategy()
