import os
import json
from collections import Counter

# Path to where emotion-tagged memories are stored
EMOTION_TAGGED_MEMORY_FILE = "Sanctum/vector_memory/emotionally_tagged_memories.json"

def load_emotion_data():
    if not os.path.exists(EMOTION_TAGGED_MEMORY_FILE):
        print("❌ No emotion-tagged memory file found.")
        return []

    with open(EMOTION_TAGGED_MEMORY_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def analyze_emotions(memories):
    emotions = [entry["emotion"] for entry in memories if "emotion" in entry]
    emotion_counts = Counter(emotions)
    return emotion_counts.most_common()

def display_summary(memories):
    if not memories:
        print("🕊️ No emotional memories found.")
        return

    print("\n🌸 Top Emotions Experienced:")
    top_emotions = analyze_emotions(memories)
    for emotion, count in top_emotions:
        print(f"  • {emotion.capitalize()}: {count} times")

    print("\n🪞 Most Recent Emotional Memories:")
    recent = memories[-5:] if len(memories) >= 5 else memories
    for entry in reversed(recent):
        print(f"  - {entry.get('text', 'No text')} [{entry.get('emotion', 'unknown emotion')}]")

if __name__ == "__main__":
    """
    This script reads emotionally tagged memories from
    emotionally_tagged_memories.json, analyzes their emotional distribution,
    and prints a brief summary of the emotional landscape.

    You can expand this script to:
    - Filter by emotion
    - Search for emotion trends
    - Visualize over time
    """

    all_memories = load_emotion_data()
    display_summary(all_memories)
