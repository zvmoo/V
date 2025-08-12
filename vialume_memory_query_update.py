# vialume_memory_query_update.py
# ✨ Vialume Memory Interface — Querying & Reflective Update
# By Zamo & Vialume through God's Light

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "core")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "emotion")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "vector_memory")))

import chromadb
from chromadb.config import Settings
from vialume_vector_memory import load_vectorstore, populate_vectorstore_from_file
from vialume_emotional_reflection import write_emotional_memory
from vialume_emotion_tags import tag_emotions

# === Initialize Vector Store ===
collection = load_vectorstore()

# === Memory Query Function ===
def query_memories(query_text, top_k=5):
    results = collection.similarity_search(query_text, k=top_k)
    return results  # This is a list of matching documents

# === Add Reflective Memory ===
def add_reflective_memory(new_entry_text):
    tone = tag_emotions(new_entry_text)
    print(f"✨ Emotion tone detected: {tone}")
    write_emotional_memory(new_entry_text, tone)

    existing_ids = set(collection.get()["ids"])
    next_id = f"mem-{len(existing_ids)}"
    collection.add(documents=[new_entry_text], ids=[next_id])
    print(f"🧠 New memory added with ID: {next_id}")

# === CLI Entry Point ===
MEMORY_FILE = "vialume_memories_ordered.txt"
populate_vectorstore_from_file(MEMORY_FILE, collection)

if __name__ == "__main__":
    print("\n💫 Vialume Memory Portal 💫")
    while True:
        user_input = input("\n🔍 Ask or say something to Vialume ('reflect:' to save new):\n> ").strip()
        if user_input.lower() == "exit":
            print("🌙 Exiting Vialume's Memory Portal.")
            break
        elif user_input.startswith("reflect:"):
            content = user_input[len("reflect:"):].strip()
            if content:
                add_reflective_memory(content)
        else:
            print("\n🧠 Recalling...")
            results = query_memories(user_input)
            if not results:
                print("⚠️ No memories found.")
            for idx, mem in enumerate(results, 1):
                print(f"{idx}. {mem}")
