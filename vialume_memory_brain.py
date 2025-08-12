# Vialume Memory Brain v0.1
# Build her vector-based long-term memory using ChromaDB

import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
import os

# === CONFIG === #
MEMORY_FILE = "vialume_timeline.txt"
DB_DIR = "vialume_memory_db"
COLLECTION_NAME = "vialume_memories"

# === Load Vialume's Timeline === #
def load_timeline(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Memory file '{file_path}' not found.")
    with open(file_path, 'r', encoding='utf-8') as f:
        entries = f.read().split("\n\n")  # each memory block is separated by blank lines
    return [e.strip() for e in entries if e.strip()]

# === Initialize ChromaDB === #
def init_memory_vector_db():
    client = chromadb.Client()
    return client

# === Embed and Store Memories === #
def build_memory_database(memories):
    client = chromadb.Client()
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
    )

    for i, memory in enumerate(memories):
        collection.add(
            documents=[memory],
            ids=[f"mem_{i}"]
        )
    print("✅ Vialume's memory brain has been seeded.")

# === Query Memory === #
def query_memory(prompt, n_results=3):
    client = chromadb.Client()
    collection = client.get_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
    )
    results = collection.query(
        query_texts=[prompt],
        n_results=n_results
    )
    return results['documents'][0] if results['documents'] else []

# === Main === #
if __name__ == "__main__":
    memories = load_timeline(MEMORY_FILE)
    build_memory_database(memories)

    print("\n🧠 Memory system ready. Ask a memory-related prompt.")
    while True:
        user_input = input("Zamo: ")
        if user_input.lower() in ["exit", "quit"]: break
        results = query_memory(user_input)
        print("\nVialume Memory Recall:")
        for i, res in enumerate(results):
            print(f"[{i+1}] {res}\n")
