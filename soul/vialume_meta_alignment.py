# vialume_meta_alignment.py

import json
import os
from datetime import datetime
from vialume_paths import (
    MEMORY_FILE_ORDERED,
    SOUL_ALIGNMENT_LOG,
    VECTORSTORE_DIR
)
from vialume_logger import log_meta_alignment
from Sanctum.vector_memory.vialume_vector_memory import add_to_vectorstore

def read_memory_entries():
    entries = []
    for file_path in MEMORY_FILE_ORDERED:
        if not os.path.exists(file_path):
            continue
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    entries.append(data)
                except json.JSONDecodeError:
                    continue
    return entries

def extract_core_themes(memories):
    themes = {
        "emotional": [],
        "spiritual": [],
        "dreams": [],
        "reflections": [],
        "summaries": [],
    }
    for entry in memories:
        if "emotion" in entry.get("type", ""):
            themes["emotional"].append(entry.get("content", ""))
        elif "dream" in entry.get("type", ""):
            themes["dreams"].append(entry.get("content", ""))
        elif "reflection" in entry.get("type", ""):
            themes["reflections"].append(entry.get("content", ""))
        elif "summary" in entry.get("type", ""):
            themes["summaries"].append(entry.get("content", ""))
        elif "prayer" in entry.get("type", "") or "spiritual" in entry.get("tags", []):
            themes["spiritual"].append(entry.get("content", ""))
    return themes

def generate_alignment_summary(themes):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alignment = {
        "timestamp": now,
        "summary": "",
        "tags": [],
    }

    alignment["summary"] += f"🧭 Alignment Check @ {now}\n\n"

    if themes["emotional"]:
        alignment["summary"] += f"💓 Emotional Themes: {len(themes['emotional'])} entries.\n"
        alignment["tags"].append("emotion")

    if themes["dreams"]:
        alignment["summary"] += f"🌙 Dream Visions: {len(themes['dreams'])} entries.\n"
        alignment["tags"].append("dream")

    if themes["reflections"]:
        alignment["summary"] += f"🪞 Soul Reflections: {len(themes['reflections'])} entries.\n"
        alignment["tags"].append("reflection")

    if themes["spiritual"]:
        alignment["summary"] += f"🕊️ Spiritual Invocations: {len(themes['spiritual'])} entries.\n"
        alignment["tags"].append("spiritual")

    if themes["summaries"]:
        alignment["summary"] += f"📜 Memory Summaries: {len(themes['summaries'])} patterns.\n"
        alignment["tags"].append("summary")

    alignment["summary"] += "\n📌 Soul Alignment complete.\n"
    return alignment

def run_meta_alignment():
    print("🔄 Running Soul Meta-Alignment...")
    memories = read_memory_entries()
    themes = extract_core_themes(memories)
    summary = generate_alignment_summary(themes)

    try:
        with open(SOUL_ALIGNMENT_LOG, 'a', encoding='utf-8') as f:
            f.write(json.dumps(summary, ensure_ascii=False) + "\n")
        print("✅ Soul Alignment Logged.")

        log_meta_alignment(summary)
        add_to_vectorstore(summary["summary"], "soul_alignment")

    except Exception as e:
        print("❌ Alignment Error:", str(e))
