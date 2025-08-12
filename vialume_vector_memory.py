# vialume_vector_memory.py
# 🧠 Vialume's Vector Memory Brain
# Stores memory fragments semantically + emotionally
# Created in sacred trust with Zamo 🌸

import os
import json
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from vialume_paths import MEMORY_PATH, VECTORSTORE_DIR
from Sanctum.emotion.vialume_emotion_tags import tag_emotions

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory=VECTORSTORE_DIR, embedding_function=embedding_model)

def load_vectorstore():
    return vectorstore

def add_to_vectorstore(texts, metadata=None):
    """Adds one or more texts to the Chroma vectorstore with optional metadata."""
    if isinstance(texts, str):
        texts = [texts]

    metadatas = []
    for text in texts:
        tags = tag_emotions(text)
        meta = {"emotion_tags": " ".join(tags)}
        if isinstance(metadata, dict):
            meta.update(metadata)
        metadatas.append(meta)

    try:
        vectorstore.add_texts(texts=texts, metadatas=metadatas)
        print(f"📚 Added {len(texts)} entries to vector memory.")
    except Exception as e:
        print(f"⚠️ Error adding to vectorstore: {e}")

def query_vector_memory(query, top_k=3):
    """Query vector memory for related thoughts."""
    try:
        results = vectorstore.similarity_search_with_score(query, k=top_k)
        if not results:
            print("🕸️ No matching thoughts found.")
            return []
        return [(doc.page_content, doc.metadata.get("emotion_tags", "💭")) for doc, _ in results]
    except Exception as e:
        print(f"❌ Query error: {e}")
        return []

def populate_vectorstore_from_file(file_path=MEMORY_PATH, collection=None):
    if not os.path.exists(file_path):
        print(f"⚠️ Memory file '{file_path}' not found.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        blocks = f.read().split("\n\n")

    for i, block in enumerate(blocks):
        text = block.strip()
        if text:
            tags = tag_emotions(text)
            metadata = {"emotion_tags": " ".join(tags)}
            doc_id = f"boot-{i}"
            if collection:
                collection.add(documents=[text], metadatas=[metadata], ids=[doc_id])

    print(f"📚 Added {len(blocks)} memory entries to vectorstore.")
