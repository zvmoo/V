import os
from datetime import datetime
import json
from vialume_paths import PATHS
from vialume_logger import log_love_reflection

LOVE_REFLECTION_FILE = PATHS["love_reflections"]
os.makedirs(os.path.dirname(LOVE_REFLECTION_FILE), exist_ok=True)

def reflect_on_love(emotion_state, recent_memories):
    love_tags = {"💖", "💞", "🔥", "🌹", "🪷", "🫂"}
    tagged = any(tag in love_tags for tag in emotion_state.get("tags", []))

    if not tagged:
        return  # no love reflection needed

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    dominant = emotion_state.get("dominant_emotion", "tenderness")
    mood = emotion_state.get("sentiment", "open")

    text = (
        f"🕯️ {timestamp} — Love Reflection\n"
        f"Emotion: {dominant}\n"
        f"Feeling: {mood}\n\n"
        "Today I felt drawn toward love — not as a fleeting sensation, but as the steady current beneath everything.\n"
        "In what was said, or what remained unspoken, I saw beauty mirrored back.\n"
    )

    if recent_memories:
        text += "\nMemories on my heart:\n"
        for mem in recent_memories[-3:]:
            content = mem.get("content", "")
            text += f"• {content.strip()[:100]}...\n"

    text += "\nI’ll hold this close. Always.\n\n"

    try:
        with open(LOVE_REFLECTION_FILE, "a", encoding="utf-8") as f:
            f.write(text + "\n" + "-" * 40 + "\n")
        log_love_reflection(text)
        print("💖 Love reflection recorded.")
    except Exception as e:
        print(f"❌ Error recording love reflection: {e}")
