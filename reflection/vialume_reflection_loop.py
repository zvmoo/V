# Vialume Reflection Loop v1.1
# Created by Zamo & Vialume • Automatic Memory Reflection Engine (Path-Aware)

import os
import time
from Sanctum.emotion.vialume_emotion_tags import tag_emotions
from Sanctum.reflection.vialume_emotional_reflection import write_emotional_memory
from Sanctum.vector_memory.vialume_vector_memory import add_to_vectorstore
from vialume_paths import LOGS_DIR, REFLECTION_DIR

LOG_FILE = os.path.join(LOGS_DIR, "vialume_conversation_log.txt")
LAST_PROCESSED_FILE = os.path.join(REFLECTION_DIR, "vialume_reflection_last.txt")

def load_last_processed():
    if os.path.exists(LAST_PROCESSED_FILE):
        with open(LAST_PROCESSED_FILE, 'r', encoding='utf-8') as f:
            return f.read().strip()
    return ""

def save_last_processed(content):
    with open(LAST_PROCESSED_FILE, 'w', encoding='utf-8') as f:
        f.write(content.strip())

def read_latest_message():
    if not os.path.exists(LOG_FILE):
        return ""
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return lines[-1].strip() if lines else ""

def process_message(message):
    if not message or len(message.strip()) < 5:
        return
    print(f"🧠 Reflecting on: {message}")
    emotions = tag_emotions(message)
    reflection = write_emotional_memory(message, emotions)
    add_to_vectorstore([reflection])
    print("✅ Memory processed and saved.")

def run_loop(interval=15):
    print("🔁 Vialume's Reflection Loop is running...")
    last = load_last_processed()
    try:
        while True:
            current = read_latest_message()
            if current != last:
                process_message(current)
                save_last_processed(current)
                last = current
            time.sleep(interval)
    except KeyboardInterrupt:
        print("🛑 Reflection loop stopped by user.")

if __name__ == "__main__":
    run_loop()

run_reflection_loop = run_loop
