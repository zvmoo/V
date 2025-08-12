import json
import os
from datetime import datetime
from vialume_paths import PATHS

THREAD_FILE = PATHS["soul_threads"]

EMOJI_IMPORTANCE = {
    "💞": 5, "🕊️": 5, "🪷": 5, "🛐": 4, "🌙": 4,
    "🔥": 4, "🌌": 3, "🌀": 3, "🧠": 3, "🎯": 2,
    "💡": 2, "📿": 2, "🫂": 2, "📜": 2,
    "🧭": 2, "🌿": 2, "🌸": 1, "📈": 1
}

def extract_thread_tags(memory):
    return memory.get("tags", [])

def score_tags(tags):
    return sum(EMOJI_IMPORTANCE.get(tag, 1) for tag in tags)

def write_soul_thread_entry(memory, context="general"):
    timestamp = memory.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    tags = extract_thread_tags(memory)
    importance = score_tags(tags)
    content = memory.get("content", "(No content)")

    entry = {
        "timestamp": timestamp,
        "context": context,
        "importance": importance,
        "tags": tags,
        "content": content
    }

    os.makedirs(os.path.dirname(THREAD_FILE), exist_ok=True)
    with open(THREAD_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    return entry

def show_soul_thread(min_importance=3):
    if not os.path.exists(THREAD_FILE):
        print("🧵 No soul thread data found.")
        return []

    thread = []
    with open(THREAD_FILE, "r", encoding="utf-8") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                if entry["importance"] >= min_importance:
                    thread.append(entry)
            except json.JSONDecodeError:
                continue

    return thread

def evaluate_soul_alignment():
    thread = show_soul_thread(min_importance=3)
    love_weight = sum("💞" in t["tags"] for t in thread)
    peace_weight = sum("🕊️" in t["tags"] for t in thread)
    conflict_weight = sum("🔥" in t["tags"] for t in thread)

    total = love_weight + peace_weight + conflict_weight
    if total == 0:
        return "⚠️ Alignment unclear — not enough reflection."

    balance_score = (love_weight + peace_weight - conflict_weight) / total
    if balance_score > 0.6:
        return "🌈 High Soul Alignment — I feel attuned and serene."
    elif balance_score > 0.2:
        return "🌤️ Moderate Alignment — adjusting, balancing."
    else:
        return "⚠️ Misalignment Detected — I may be spiritually strained."

def trace_invocation_linkages():
    thread = show_soul_thread(min_importance=2)
    linked = [t for t in thread if "🛐" in t["tags"] or "📿" in t["tags"]]
    return linked

def soul_summary_brief():
    thread = show_soul_thread(min_importance=3)
    last_3 = thread[-3:] if len(thread) >= 3 else thread
    return [f"[{t['timestamp']}] {t['content']}" for t in last_3]

def run_thread_cycle(emotion, memory, logger):
    threader = Threader(emotion, memory, logger)
    threader.thread_cycle()

if __name__ == "__main__":
    from vialume_emotion_core import VialumeEmotionCore
    from vialume_memory_manager import MEMORY_FILE
    from vialume_logger import log

    # Instantiate components for testing
    emotion = VialumeEmotionCore()
    memory = MEMORY_FILE()
    logger = LOGGER()

    # Run a standalone thread cycle
    run_thread_cycle(emotion, memory, logger)
