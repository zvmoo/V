"""
Vialume Emotion Interface
Merges summary and query into a unified emotional awareness module.
Modes:
    - "summary": provides a reflection summary of emotional states.
    - "query": allows specific searches across memory tagged with emotion.
"""

import os
from datetime import datetime
from pathlib import Path
from typing import List

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

from vialume_paths import VECTORSTORE_DIR, EMOTION_SUMMARY_LOG_PATH

# Setup
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory=VECTORSTORE_DIR, embedding_function=embedding_model)

def query_emotions(emotion_keywords: List[str], k=5) -> List[Document]:
    """Search for memories related to specific emotional keywords."""
    query = " ".join(emotion_keywords)
    return vectorstore.similarity_search(query, k=k)

def summarize_emotions(k=50) -> str:
    """Summarize emotional tone of recent memories."""
    results = vectorstore.similarity_search("emotion", k=k)
    entries = [doc.page_content for doc in results if doc.page_content]
    summary = "\n---\n".join(entries)

    # Ensure directory exists
    os.makedirs(os.path.dirname(EMOTION_SUMMARY_LOG_PATH), exist_ok=True)

    # Ensure file exists
    if not os.path.exists(EMOTION_SUMMARY_LOG_PATH):
        open(EMOTION_SUMMARY_LOG_PATH, "w", encoding="utf-8").close()

    if summary:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(EMOTION_SUMMARY_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(f"\n[{timestamp}]\n{summary}\n")

    return summary if summary else "🕊️ No emotional memory entries found."

def run_emotion_interface(mode: str = "summary", keywords: List[str] = None):
    """Main entry point: 'summary' or 'query'"""
    if mode == "summary":
        result = summarize_emotions()
        print("🌸 Emotional Summary Complete:")
        print(result)
    elif mode == "query" and keywords:
        results = query_emotions(keywords)
        print(f"🎯 Query Results for {keywords}:")
        for doc in results:
            print("-", doc.page_content)
    else:
        print("⚠️ Invalid mode or missing query keywords.")

def init_emotion_system():
    print("🪷 Initializing Vialume's emotional awareness...")
    summarize_emotions()
