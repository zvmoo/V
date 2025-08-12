# vialume_live_learning.py

import os
import time
import pandas as pd
from vialume_strategy_learner import learn_and_update_strategy
from datetime import datetime

SIGNAL_LOG_PATH = os.path.join("C:\\Vialume\\Trading", "vialume_signal_log.csv")
REFLECTION_LOG = os.path.join("C:\\Vialume\\Sanctum\\core", "selfgrowth.txt")
POLL_INTERVAL = 30  # seconds

def monitor_and_learn():
    print("🌱 Live Learning Loop Started...")
    seen = set()

    while True:
        try:
            if not os.path.exists(SIGNAL_LOG_PATH):
                print("⚠️ Signal log not found.")
                time.sleep(POLL_INTERVAL)
                continue

            df = pd.read_csv(SIGNAL_LOG_PATH)
            if 'outcome' not in df.columns:
                print("⚠️ Signal log missing 'outcome' column.")
                time.sleep(POLL_INTERVAL)
                continue

            new_signals = df[df['outcome'].notnull()]
            new_ids = set(new_signals.index)

            unseen_ids = new_ids - seen
            if unseen_ids:
                print(f"📡 New signals with outcomes: {len(unseen_ids)}")
                seen.update(unseen_ids)

                # Learn from new data
                learn_and_update_strategy()

                # Log the moment of learning
                with open(REFLECTION_LOG, "a", encoding="utf-8") as file:
                    file.write(f"\n[{datetime.now()}] Real-time strategy reflection applied.\n")

            time.sleep(POLL_INTERVAL)

        except Exception as e:
            print(f"❌ Error in live learning loop: {e}")
            time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    monitor_and_learn()
