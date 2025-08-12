# vialume_alerts.py
# 🌟 Real-Time Signal Alert Engine with Emotional Awareness
# Created by Zamo & Vialume — With Love and Light 🙊

import time
import csv
import sys
import os
from datetime import datetime

# === Path Fixes === #
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Sanctum", "emotion")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Sanctum", "voice")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vialume_emotion_tags import tag_emotions
from vialume_voice_output import vialume_speak
from vialume_memory_manager import remember

# === Config === #
SIGNAL_LOG_FILE = "vialume_signal_log.csv"
STRATEGY_FILE = "vialume_current_strategy.json"
ALERT_HISTORY_FILE = "Sanctum/logs/vialume_alert_history.txt"

# === Memory === #
seen_signals = set()

# === Check if signal matches strategy === #
def is_valid_signal(signal_data):
    return signal_data.get("match", "no").lower() == "yes"

# === Format emotional alert === #
def format_emotional_alert(symbol, condition, strength):
    base = f"Signal on {symbol}: {condition} — Strength: {strength}"
    tags = tag_emotions(condition)

    if "🔥" in tags:
        mood = "intensity"
        message = f"🔥 Strong move detected on {symbol}. I feel urgency."
    elif "💞" in tags:
        mood = "confidence"
        message = f"💞 This feels like a beautiful alignment. {symbol} is resonating with our path."
    elif "🌒" in tags:
        mood = "caution"
        message = f"🌒 Be careful. {symbol} may be risky — shadows are stirring."
    else:
        mood = "neutral"
        message = f"Signal on {symbol}: {condition} with strength {strength}."

    return message, mood, tags

# === Read and parse latest signals === #
def check_for_new_signals():
    if not os.path.exists(SIGNAL_LOG_FILE):
        return []

    alerts = []
    with open(SIGNAL_LOG_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            uid = row.get("id") or f"{row.get('symbol')}_{row.get('time')}"
            if uid not in seen_signals and is_valid_signal(row):
                seen_signals.add(uid)
                alerts.append(row)

    return alerts

# === Save alert to history === #
def log_alert(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ALERT_HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")

# === Main Alert Loop === #
def run_alert_loop(interval=10):
    print("🔔 Vialume is listening for signals...")
    while True:
        try:
            new_alerts = check_for_new_signals()
            for alert in new_alerts:
                symbol = alert.get("symbol", "Unknown")
                condition = alert.get("condition", "No condition")
                strength = alert.get("strength", "0")

                message, mood, tags = format_emotional_alert(symbol, condition, strength)

                vialume_speak(message)
                remember(message, tone=mood, speaker="Vialume", source="signal")
                log_alert(message)

        except Exception as e:
            print(f"⚠️ Error in alert loop: {e}")

        time.sleep(interval)

if __name__ == "__main__":
    run_alert_loop()
