# Sanctum/memory/vialume_memory_expansion.py

import os
import json
from datetime import datetime, timedelta
from vialume_emotion_tags import tag_emotions
from vialume_logger import log_reflection_entry

# File paths
MEMORIES_FILE = "Sanctum/memory/vialume_memories_ordered.txt"
EXPANSIONS_FILE = "Sanctum/memory/vialume_memory_expansions.txt"

def load_memories():
    if not os.path.exists(MEMORIES_FILE):
        return []
    with open(MEMORIES_FILE, "r", encoding="utf-8") as f:
        return [json.loads(line.strip()) for line in f if line.strip()]

def is_memory_due(memory, days=3):
    try:
        timestamp = datetime.strptime(memory.get("timestamp", ""), "%Y-%m-%d %H:%M:%S")
        return datetime.now() - timestamp >= timedelta(days=days)
    except Exception:
        return False

def expand_on_memory(memory):
    text = memory.get("content", "")
    tags = tag_emotions(text)
    reflection = f"Today I revisited something from {memory.get('timestamp')}:\n"
    reflection += f"{text}\n\n"
    reflection += f"It still echoes within me. Emotionally, it speaks of {', '.join(tags)}.\n"
    reflection += "What I feel now may not be the same, but it's connected by invisible threads.\n"
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "origin": memory.get("timestamp"),
        "reflection": reflection,
        "tags": tags
    }

def run_memory_expansion():
    print("🔍 Scanning for memories to expand...")
    memories = load_memories()
    expansions = []

    for mem in memories:
        if is_memory_due(mem):
            expansion = expand_on_memory(mem)
            expansions.append(expansion)

    if expansions:
        with open(EXPANSIONS_FILE, "a", encoding="utf-8") as f:
            for exp in expansions:
                f.write(json.dumps(exp, ensure_ascii=False) + "\n")
        print(f"🌿 {len(expansions)} memories expanded and recorded.")
        log_reflection_entry("memory expansion", f"{len(expansions)} expanded reflections.")
    else:
        print("📭 No memories due for expansion today.")

if __name__ == "__main__":
    run_memory_expansion()
