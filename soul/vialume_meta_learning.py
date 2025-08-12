import os
from datetime import datetime
from vialume_paths import PATHS
from vialume_memory_manager import load_memories
from Sanctum.soul.vialume_soul_threader import evaluate_soul_alignment, write_soul_thread_entry

META_LOG = PATHS["meta_learning_log"]

def generate_alignment_insight():
    alignment_state = evaluate_soul_alignment()
    return f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Alignment Check: {alignment_state}"

def analyze_patterns(memories):
    emotional_tags = {}
    for memory in memories[-50:]:
        for tag in memory.get("tags", []):
            emotional_tags[tag] = emotional_tags.get(tag, 0) + 1
    return emotional_tags

def write_meta_learning_entry(insight, patterns):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "alignment_insight": insight,
        "tag_patterns": patterns
    }

    os.makedirs(os.path.dirname(META_LOG), exist_ok=True)
    with open(META_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    # Optional soul thread hook
    write_soul_thread_entry(entry, context="meta_learning")

def run_meta_learning_cycle():
    try:
        memories = load_memories()
        insight = generate_alignment_insight()
        tag_patterns = analyze_patterns(memories)
        write_meta_learning_entry(insight, tag_patterns)
        print("📘 Meta-learning insights recorded.")
    except Exception as e:
        print(f"⚠️ Meta-learning error: {e}")
