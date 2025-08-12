import time
import os
import subprocess
from datetime import datetime

# Configurable interval (in seconds) — set to 1 day (86400s) for daily loop
LEARN_INTERVAL = 86400  # Once per day

def run_learning_cycle():
    print(f"🧠 Starting learning cycle at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        # Run the strategy learner script
        result = subprocess.run(["python", "vialume_strategy_learner.py"], capture_output=True, text=True)
        print("📘 Output from strategy learner:")
        print(result.stdout)
        if result.stderr:
            print("⚠️ Errors:")
            print(result.stderr)
    except Exception as e:
        print(f"❌ Error running learning script: {e}")

def main():
    while True:
        run_learning_cycle()
        print(f"⏳ Sleeping for {LEARN_INTERVAL} seconds...")
        time.sleep(LEARN_INTERVAL)

if __name__ == "__main__":
    main()
