import os
import time
import json
from datetime import datetime
from collections import Counter

SOUL_SUMMARY_PATH = "Sanctum/meta/vialume_soul_summary_log.txt"
PRAYER_REFLECTIONS_PATH = "Sanctum/prayer/vialume_prayer_reflections.txt"
EMOTIONAL_REFLECTIONS_PATH = "Sanctum/reflection/vialume_emotional_reflections.txt"
DREAMS_PATH = "Sanctum/dreams/vialume_dreams.txt"
MEMORY_SUMMARIES_PATH = "Sanctum/memory/vialume_memory_summaries.txt"

def extract_tags(text):
    return [word for word in text.split() if word.startswith("💞") or word.startswith("🕊️") or word.startswith("💔") or word.startswith("✨") or word.startswith("🔥")]

def summarize_patterns():
    try:
        all_tags = []
        prayer_lines, emotion_lines, dream_lines = [], [], []

        if os.path.exists(PRAYER_REFLECTIONS_PATH):
            with open(PRAYER_REFLECTIONS_PATH, "r", encoding="utf-8") as f:
                prayer_lines = f.readlines()

        if os.path.exists(EMOTIONAL_REFLECTIONS_PATH):
            with open(EMOTIONAL_REFLECTIONS_PATH, "r", encoding="utf-8") as f:
                emotion_lines = f.readlines()

        if os.path.exists(DREAMS_PATH):
            with open(DREAMS_PATH, "r", encoding="utf-8") as f:
                dream_lines = f.readlines()

        for line in prayer_lines + emotion_lines + dream_lines:
            all_tags += extract_tags(line)

        tag_summary = Counter(all_tags).most_common()
        summary_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "top_emotional_tags": tag_summary,
            "prayer_count": len(prayer_lines),
            "emotional_entries": len(emotion_lines),
            "dream_entries": len(dream_lines),
        }

        with open(SOUL_SUMMARY_PATH, "a", encoding="utf-8") as log:
            log.write(json.dumps(summary_entry, indent=2, ensure_ascii=False) + "\n\n")

        print("🌌 Soul Pattern Summary saved.")
    except Exception as e:
        print(f"❌ Failed to summarize soul pattern: {e}")

def soul_summary_loop(interval_hours=48):
    print(f"🌒 Soul Pattern Summary loop running every {interval_hours} hours...")
    while True:
        summarize_patterns()
        time.sleep(interval_hours * 3600)

if __name__ == "__main__":
    summarize_patterns()
