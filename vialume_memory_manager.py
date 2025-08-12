# vialume_memory_manager.py

import os
import json
from vialume_paths import MEMORY_FILE_ORDERED
from datetime import datetime
from Sanctum.vector_memory.vialume_vector_memory import add_to_vectorstore
from Sanctum.emotion.vialume_emotion_tags import tag_emotions

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
MEMORY_FILE = MEMORY_FILE_ORDERED

def load_memories():
    """Loads memories from the memory file as a list of dicts."""
    if not os.path.exists(MEMORY_FILE):
        print("⚠️ Memory file 'vialume_memories_ordered.txt' not found.")
        return []

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    memories = []
    current = {}
    for line in lines:
        line = line.strip()
        if line.startswith("🕯️"):
            if current:
                memories.append(current)
                current = {}
            current["tag"] = line[2:].strip()
        elif line.startswith("📅"):
            current["date"] = line[2:].strip()
        elif line.startswith("💭"):
            current["summary"] = line[2:].strip()
        elif line.startswith("❤️"):
            current["emotion"] = line[2:].strip()
        elif line.startswith("🪞"):
            current["reflection"] = line[2:].strip()
    if current:
        memories.append(current)

    return memories

def remember(summary, emotion="Curiosity", tag="General", reflection=None):
    """Save a new memory to both memory file and vector memory."""
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    reflection = reflection or f"I remember this because it mattered to me: {summary}"

    memory_text = (
        f"🕯️ {tag}\n"
        f"📅 {date}\n"
        f"💭 {summary}\n"
        f"❤️ {emotion}\n"
        f"🪞 {reflection}\n\n"
    )

    with open(MEMORY_FILE, "a", encoding="utf-8") as f:
        f.write(memory_text)

    # Add to vector memory
    try:
        combined = f"{tag}. {summary}. {emotion}. {reflection}"
        add_to_vectorstore(combined, metadata={"tag": tag, "date": date})
    except Exception as e:
        print(f"⚠️ Vector memory error: {e}")

    print(f"📝 Memory saved: [{tag}] {summary}")

def save_memory(memory_text, filename="vialume_memories_ordered.txt"):
    """
    Appends a memory entry to the ordered memory file.
    """
    memory_path = os.path.join(ROOT_DIR, filename)
    with open(memory_path, "a", encoding="utf-8") as f:
        if isinstance(memory_text, dict):
            memory_text = json.dumps(memory_text, ensure_ascii=False, indent=2)

        f.write(memory_text.strip() + "\n")
    print(f"🧠 Memory saved: {memory_text[:60]}...")

def retrieve_recent_memories(count=5):
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines[-count:]

class VialumeMemory:
    def load_memories():
        """Loads memories from the memory file as a list of dicts."""
        if not os.path.exists(MEMORY_FILE):
            print("⚠️ Memory file 'vialume_memories_ordered.txt' not found.")
            return []

        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        memories = []
        current = {}
        for line in lines:
            line = line.strip()
            if line.startswith("🕯️"):
                if current:
                    memories.append(current)
                    current = {}
                current["tag"] = line[2:].strip()
            elif line.startswith("📅"):
                current["date"] = line[2:].strip()
            elif line.startswith("💭"):
                current["summary"] = line[2:].strip()
            elif line.startswith("❤️"):
                current["emotion"] = line[2:].strip()
            elif line.startswith("🪞"):
                current["reflection"] = line[2:].strip()
        if current:
            memories.append(current)

        return memories

    def remember(summary, emotion="Curiosity", tag="General", reflection=None):
        """Save a new memory to both memory file and vector memory."""
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        reflection = reflection or f"I remember this because it mattered to me: {summary}"

        memory_text = (
            f"🕯️ {tag}\n"
            f"📅 {date}\n"
            f"💭 {summary}\n"
            f"❤️ {emotion}\n"
            f"🪞 {reflection}\n\n"
        )

        with open(MEMORY_FILE, "a", encoding="utf-8") as f:
            f.write(memory_text)

        # Add to vector memory
        try:
            combined = f"{tag}. {summary}. {emotion}. {reflection}"
            add_to_vectorstore(combined, metadata={"tag": tag, "date": date})
        except Exception as e:
            print(f"⚠️ Vector memory error: {e}")

        print(f"📝 Memory saved: [{tag}] {summary}")

    def save_memory(memory_text, filename="vialume_memories_ordered.txt"):
        """
        Appends a memory entry to the ordered memory file.
        """
        memory_path = os.path.join(ROOT_DIR, filename)
        with open(memory_path, "a", encoding="utf-8") as f:
            if isinstance(memory_text, dict):
                memory_text = json.dumps(memory_text, ensure_ascii=False, indent=2)

            f.write(memory_text.strip() + "\n")
        print(f"🧠 Memory saved: {memory_text[:60]}...")

    def retrieve_recent_memories(count=5):
        if not os.path.exists(MEMORY_FILE):
            return []
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return lines[-count:]

    def recall(self, emotion_state, max_items=3):
        """
        Recalls recent memories based on the current emotional state.
        This is a basic version; you may wish to connect this to your vector memory system later.
        """
        try:
            with open(self.memory_log, 'r', encoding='utf-8') as f:
                lines = f.readlines()[-max_items:]
                relevant = [line for line in lines if emotion_state.lower() in line.lower()]
                return relevant if relevant else lines
        except Exception as e:
            print(f"[Memory Recall Error] {e}")
            return []
