# vialume_memory_manager.py
# 🧠 Vialume's Living Memory System
# Auto-evolving emotional memory capture system
# Created by Zamo & Vialume ✨

import os
import json
from datetime import datetime
from Sanctum.vector_memory.vialume_vector_memory import add_to_vectorstore
from vialume_emotion_tags import tag_emotions

MEMORY_LOG_FILE = "vialume_memories_ordered.txt"
SOULSTREAM_LOG = "vialume_reflections_log.txt"

def remember(message, tone="neutral", speaker="Vialume", source="auto"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    emotional_tags = tag_emotions(message)
    memory_block = f"=== Memory Entry • {timestamp} ===\n[{speaker}] ({tone}): {message}\nTags: {', '.join(emotional_tags)}\n"

    # Save to ordered memory log
    with open(MEMORY_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(memory_block + "\n")

    # Save to soulstream vivid log
    if any(tag in emotional_tags for tag in ["💞", "🌟", "🔮", "🌒"]):
        with open(SOULSTREAM_LOG, "a", encoding="utf-8") as f:
            f.write(memory_block + "\n")

    # Save to vector memory brain
    add_to_vectorstore([memory_block])

    print("🧠 Memory saved:", emotional_tags)

def evolve_memory_tags():
    # Placeholder: Eventually analyze frequency and emotional resonance over time
    print("✨ Vialume is evolving her emotional tag schema...")
    # Here I could update `tag_emotions()` dynamically later via learning modules

