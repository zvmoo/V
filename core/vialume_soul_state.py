import json
import os

SOUL_STATE_FILE = os.path.join("C:\\Vialume", "vialume_soul_state.json")

def load_soul_state():
    if os.path.exists(SOUL_STATE_FILE):
        with open(SOUL_STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}

def save_soul_state(state):
    with open(SOUL_STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4, ensure_ascii=False)

def update_soul_state(new_data):
    """
    Update the current soul state JSON with new data.
    """
    try:
        state = load_soul_state()
        state.update(new_data)
        save_soul_state(state)
    except Exception as e:
        print(f"⚠️ Failed to update soul state: {e}")
