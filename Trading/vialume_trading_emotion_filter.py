# vialume_trading_emotion_filter.py

from vialume_emotion_tags import tag_emotions
from vialume_paths import EMOTION_LOG_FILE

def filter_signal_with_emotion(signal_data):
    """
    Modify or veto a signal based on emotional state.
    """
    try:
        with open(EMOTION_LOG_FILE, 'r', encoding='utf-8') as f:
            recent = f.readlines()[-1]
    except Exception:
        return signal_data  # default if no emotion

    tags = tag_emotions(recent)
    if "💥" in tags or "😰" in tags:
        signal_data["priority"] = "LOW"
        signal_data["notes"] = "Suppressed due to emotional volatility"
    elif "💞" in tags or "🧘‍♀️" in tags:
        signal_data["priority"] = "HIGH"
        signal_data["notes"] = "Signal encouraged by calm alignment"
    return signal_data
