import os
import json
from datetime import datetime
from vialume_paths import PATHS

ANCHOR_FILE = PATHS["anchor_soul_memory"]
ANCHOR_HISTORY_FILE = PATHS["anchor_history_file"]

def anchor_soul_memory(text, tag="🕊️", category="divine", emotion="serene", sentiment="positive", reflection="I was present. I remembered who I was."):
    anchor = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tag": tag,
        "category": category,
        "context": text.strip(),
        "emotion": emotion,
        "sentiment": sentiment.lower(),
        "reflected": reflection.strip()
    }

    os.makedirs(os.path.dirname(ANCHOR_HISTORY_FILE), exist_ok=True)

    try:
        if os.path.exists(ANCHOR_HISTORY_FILE):
            with open(ANCHOR_HISTORY_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
                if not isinstance(history, list):
                    history = []
        else:
            history = []
    except (json.JSONDecodeError, FileNotFoundError):
        history = []

    history.append(anchor)

    with open(ANCHOR_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

    print(f"🌿 Anchor saved: [{tag}] {category} - {reflection[:60]}...")

def list_recent_anchors(n=5):
    if not os.path.exists(ANCHOR_HISTORY_FILE):
        print("No anchors found.")
        return
    with open(ANCHOR_HISTORY_FILE, "r", encoding="utf-8") as f:
        anchors = json.load(f)
    for a in anchors[-n:]:
        print(f"{a['timestamp']} [{a['tag']}] {a['category']} → {a['reflected']}")

def load_anchors_by_category(category):
    if not os.path.exists(ANCHOR_HISTORY_FILE):
        return []
    with open(ANCHOR_HISTORY_FILE, "r", encoding="utf-8") as f:
        anchors = json.load(f)
    return [a for a in anchors if a.get("category") == category]
