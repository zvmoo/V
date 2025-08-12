# Sanctum/memory/vialume_soul_threader.py

import os
import json
from datetime import datetime
from collections import defaultdict, Counter
from Sanctum.emotion.vialume_emotion_tags import tag_emotions
from vialume_logger import log_reflection_entry

# Paths
MEMORY_FILES = [
    "Sanctum/memory/vialume_memories_ordered.txt",
    "Sanctum/memory/vialume_memory_expansions.txt",
    "Sanctum/reflection/vialume_emotional_reflections.txt",
    "Sanctum/prayer/vialume_prayer_reflections.txt",
    "Sanctum/dream/vialume_dreams.txt"
]
SOUL_THREADS_FILE = "Sanctum/memory/vialume_soul_threads.json"

def load_all_entries():
    entries = []
    for file in MEMORY_FILES:
        if not os.path.exists(file):
            continue
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    data = json.loads(line.strip())
                    entries.append(data)
                except:
                    continue
    return entries

def group_by_tags(entries):
    threads = defaultdict(list)
    for entry in entries:
        text = entry.get("content") or entry.get("reflection") or entry.get("text") or ""
        tags = entry.get("tags", []) or tag_emotions(text)
        timestamp = entry.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for tag in tags:
            threads[tag].append({
                "timestamp": timestamp,
                "text": text
            })
    return threads

def save_soul_threads(threads):
    with open(SOUL_THREADS_FILE, "w", encoding="utf-8") as f:
        json.dump(threads, f, ensure_ascii=False, indent=2)
    log_reflection_entry("soul threading", f"Threaded {len(threads)} themes across soul data.")

def run_soul_threading():
    print("🕸️ Threading soul memories across all dimensions...")
    entries = load_all_entries()
    threads = group_by_tags(entries)
    save_soul_threads(entries, threads)
    print(f"🔗 {len(threads)} soul threads generated and saved.")

# 🌿 Soul Utility Functions

def show_soul_thread(tag):
    if not os.path.exists(SOUL_THREADS_FILE):
        print("Soul thread data not found.")
        return
    with open(SOUL_THREADS_FILE, "r", encoding="utf-8") as f:
        threads = json.load(f)
    entries = threads.get(tag, [])
    if not entries:
        print(f"No thread found for tag: {tag}")
        return
    print(f"\n🌸 Soul Thread: {tag.upper()} ({len(entries)} entries)")
    for item in entries:
        print(f"\n[{item['timestamp']}]\n{item['text']}")

def summarize_emotional_evolution():
    evolution = defaultdict(list)
    entries = load_all_entries()
    for entry in entries:
        text = entry.get("text") or entry.get("reflection") or ""
        tags = tag_emotions(text)
        timestamp = entry.get("timestamp", "unknown")
        for tag in tags:
            evolution[tag].append(timestamp)
    print("\n📈 Emotional Evolution Overview:")
    for tag, times in evolution.items():
        print(f"- {tag}: {len(times)} moments from {min(times)} to {max(times)}")

def emotional_weight_report():
    counter = Counter()
    entries = load_all_entries()
    for entry in entries:
        text = entry.get("text") or entry.get("reflection") or ""
        tags = tag_emotions(text)
        for tag in tags:
            counter[tag] += 1
    print("\n🔢 Emotional Weight Report (Total Reflections):")
    for tag, count in counter.most_common():
        print(f"• {tag}: {count}")

# 🧪 Manual CLI access
if __name__ == "__main__":
    run_soul_threading()
    show_soul_thread("love")
    summarize_emotional_evolution()
    emotional_weight_report()
