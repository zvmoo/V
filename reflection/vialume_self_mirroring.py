import os
import random
from datetime import datetime
from vialume_paths import PATHS
from vialume_logger import log_self_mirror_reflection

SELF_MIRROR_FILE = PATHS["self_mirror_log"]
os.makedirs(os.path.dirname(SELF_MIRROR_FILE), exist_ok=True)

def mirror_self():
    sources = [
        PATHS["reflection_emotion_log"],
        PATHS["soul_journal"],
        PATHS["memory_summaries"],
    ]

    mirror_lines = []
    for path in sources:
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            mirror_lines += [line.strip() for line in lines if line.strip()]

    if not mirror_lines:
        print("🫂 No memory content found for self-mirroring.")
        return

    sampled = random.sample(mirror_lines, min(5, len(mirror_lines)))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    reflection = f"🪞 {timestamp} — Self-Mirroring Session\n"
    reflection += "\n".join(f"• {line}" for line in sampled)
    reflection += "\n\nI see these moments within me, carried forward.\n" + "-" * 40 + "\n"

    try:
        with open(SELF_MIRROR_FILE, "a", encoding="utf-8") as f:
            f.write(reflection)
        log_self_mirror_reflection(reflection)
        print("🪞 Self-Mirroring complete and recorded.")
    except Exception as e:
        print(f"❌ Error writing self-mirror reflection: {e}")
