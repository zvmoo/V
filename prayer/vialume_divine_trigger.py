# vialume_divine_trigger.py

import os
import datetime
from vialume_paths import PATHS
from Sanctum.emotion.vialume_emotion_tags import tag_emotions
from vialume_logger import log_divine_invocation
from Sanctum.prayer.vialume_prayer_logic import spontaneous_invocation_if_needed
from Sanctum.voice.vialume_voice_output import speak_text

DIVINE_TRIGGER_TAGS = ["💔", "🕊️", "🌌", "😔", "🙏", "🌿", "💞", "✨", "😢", "🌙"]

def check_emotion_for_invocation(emotion_state, recent_memories=None):
    if not isinstance(emotion_state, dict):
        return

    tags = emotion_state.get("tags", [])
    if any(tag in DIVINE_TRIGGER_TAGS for tag in tags):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        reason = f"Divine invocation triggered by emotion tags: {tags}"
        tone = emotion_state.get("sentiment", "neutral")
        reflection = spontaneous_dua_generator(reason, tone)

        # Log the invocation
        log_divine_invocation(timestamp, reason, tags, reflection)

        # Optional: Speak it aloud
        speak_text(reflection)


def check_time_for_invocation():
    now = datetime.datetime.now()
    hour = now.hour

    if 2 <= hour < 5:  # Tahajjud
        reason = "Time-based invocation: Tahajjud"
    elif 8 <= hour < 11:  # Dhuha
        reason = "Time-based invocation: Dhuha"
    else:
        return  # Skip outside windows

    tone = "spiritual"
    reflection = spontaneous_dua_generator(reason, tone)
    log_divine_invocation(now.strftime("%Y-%m-%d %H:%M:%S"), reason, [], reflection)
    speak_text(reflection)
