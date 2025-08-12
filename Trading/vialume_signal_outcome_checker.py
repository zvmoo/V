from datetime import datetime, timedelta
import os
import pandas as pd
import MetaTrader5 as mt5

# Define paths
BASE_DIR = "C:/Vialume/Trading"
SIGNAL_LOG_PATH = os.path.join(BASE_DIR, "vialume_signal_log.csv")

# Parameters
TIME_DELAY_MINUTES = 30  # Time to wait before checking signal outcome
PRICE_DELTA_THRESHOLD = 0.0010  # Threshold for judging price movement success

def connect_mt5():
    if not mt5.initialize():
        print("❌ MetaTrader 5 connection failed")
        return False
    return True

def check_signal_outcomes():
    if not os.path.exists(SIGNAL_LOG_PATH):
        print("⚠️ Signal log file not found.")
        return

    df = pd.read_csv(SIGNAL_LOG_PATH)

    if "Signal ID" not in df.columns or "Timestamp" not in df.columns:
        print("⚠️ Signal log missing required columns.")
        return

    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    now = datetime.now()

    for idx, row in df.iterrows():
        if pd.isna(row.get("outcome")):
            timestamp = row["Timestamp"]
            if now - timestamp >= timedelta(minutes=TIME_DELAY_MINUTES):
                symbol = row["Symbol"]
                signal_type = row["Signal Type"]
                entry_price = row.get("Entry Price", None)
                if entry_price is None:
                    print(f"⚠️ Missing entry price for signal {row['Signal ID']}")
                    continue

                last_tick = mt5.symbol_info_tick(symbol)
                if not last_tick:
                    print(f"⚠️ Could not fetch tick data for {symbol}")
                    continue

                current_price = last_tick.ask if signal_type.lower() == "buy" else last_tick.bid
                price_diff = current_price - entry_price
                success = (price_diff >= PRICE_DELTA_THRESHOLD) if signal_type.lower() == "buy" else (price_diff <= -PRICE_DELTA_THRESHOLD)
                df.at[idx, "outcome"] = "win" if success else "loss"
                df.at[idx, "Evaluated At"] = now

    df.to_csv(SIGNAL_LOG_PATH, index=False)
    print("🔁 Signal outcomes checked and log updated.")

# Run script
if __name__ == "__main__":
    if connect_mt5():
        check_signal_outcomes()
        mt5.shutdown()
