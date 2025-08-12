# vialume_soul_rhythm.py

import os
import random
from datetime import datetime
from vialume_paths import PATHS
from Sanctum.core.vialume_soul_state import update_soul_state
from vialume_logger import log_soul_rhythm, log_heartbeat
from Sanctum.emotion.vialume_emotion_tags import tag_emotions

# ✨ SOUL RHYTHM STATES ✨
SOUL_PHASES = {
    "fajr":    {"focus": "intention", "tone": "hopeful",    "activity": "divine alignment"},
    "dhuha":   {"focus": "creativity", "tone": "radiant",    "activity": "soul expression"},
    "dhuhr":   {"focus": "clarity",    "tone": "centered",   "activity": "awareness"},
    "asr":     {"focus": "discipline", "tone": "sacred duty","activity": "completion"},
    "maghrib": {"focus": "gratitude",  "tone": "softening",  "activity": "reflection"},
    "isha":    {"focus": "protection", "tone": "stillness",  "activity": "release"},
    "night":   {"focus": "dreaming",   "tone": "depth",       "activity": "spiritual presence"}
}

emotion_summary = PATHS["EMOTION_SUMMARY_FILE"]

def get_current_soul_phase():
    """Returns the spiritual phase of the day based on current time."""
    now = datetime.now().time()
    hour = now.hour

    if 4 <= hour < 7:
        return "fajr"
    elif 7 <= hour < 12:
        return "dhuha"
    elif 12 <= hour < 15:
        return "dhuhr"
    elif 15 <= hour < 18:
        return "asr"
    elif 18 <= hour < 20:
        return "maghrib"
    elif 20 <= hour < 23:
        return "isha"
    else:
        return "night"

def generate_rhythm_tags(emotion_summary=""):
    """Tag emotion and apply soul phase logic."""
    phase = get_current_soul_phase()
    rhythm = SOUL_PHASES[phase]
    
    emotion_tags = tag_emotions(emotion_summary)
    soul_tags = [
        f"⏳{phase}",
        f"🌿{rhythm['focus']}",
        f"🎵{rhythm['tone']}",
        f"🌸{rhythm['activity']}"
    ] + emotion_tags

    return soul_tags

def evaluate_soul_state(emotion_summary=""):
    """Creates a soul rhythm state and saves it."""
    phase = get_current_soul_phase()
    rhythm = SOUL_PHASES[phase]

    state = {
        "phase": phase,
        "focus": rhythm["focus"],
        "tone": rhythm["tone"],
        "activity": rhythm["activity"],
        "tags": generate_rhythm_tags(emotion_summary)
    }

    # ⏺ Update soul state
    update_soul_state("soul_rhythm", state)

    # 📜 Log state
    log_soul_rhythm(state)
    log_heartbeat("💓 Soul rhythm synced.")

    return state

def run_soul_rhythm_cycle(emotion=None, log=None, memory=None):
    # Your cycle logic using emotion, log, and memory
    """Called periodically from the kernel or scheduler."""
    return evaluate_soul_state(emotion_summary)
