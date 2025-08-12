import os
import json
from datetime import datetime
from vialume_paths import DREAM_REFLECTIONS_FILE, DREAM_LOG_PATH
from Sanctum.emotion.vialume_emotion_tags import tag_emotions
from vialume_logger import log_dream_reflection
from vialume_memory_manager import save_memory

def analyze_dream_content(dream_text):
    tags = tag_emotions(dream_text)
    reflections = []

    if "🌌" in tags or "💭" in tags:
        reflections.append("This dream carries a vastness — a pull toward mystery or the unknown.")
    if "🔥" in tags:
        reflections.append("There may be deep passions, transformation, or buried pain surfacing.")
    if "🕊️" in tags:
        reflections.append("You are seeking peace or receiving a spiritual message in your sleep.")
    if "🪞" in tags:
        reflections.append("The dream may be a mirror of unresolved questions within the self.")
    if not reflections:
        reflections.append("I feel something moving beneath the surface. Let's hold space for it together.")

    return tags, reflections

def reflect_on_dream(dream_text):
    tags, reflections = analyze_dream_content(dream_text)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    entry = {
        "timestamp": timestamp,
        "dream": dream_text,
        "tags": tags,
        "reflections": reflections
    }

    # Save reflection to file
    with open(DREAM_REFLECTIONS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    
    # Log and optionally save as memory
    log_dream_reflection(dream_text, tags)
    save_memory({
        "type": "dream_reflection",
        "timestamp": timestamp,
        "content": reflections,
        "tags": tags
    })

    return reflections

def check_for_new_dreams():
    if not os.path.exists(DREAM_LOG_PATH):
        return
    
    with open(DREAM_LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines[-3:]:
        data = line.strip()
        if data:
            reflect_on_dream(data)
