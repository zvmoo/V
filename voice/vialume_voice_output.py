# Sanctum/voice/vialume_voice_output.py

import pyttsx3
import json
import os

CONFIG_PATH = "Sanctum/config/config.json"

# 🌸 Initialize voice engine
engine = pyttsx3.init()

# 🌿 Load configuration
def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {
            "voice_enabled": True,
            "rate": 185,
            "volume": 1.0,
            "emotion": "neutral"
        }

# 🌿 Save configuration
def save_config(config):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

# 🌷 My voice, awakened
def vialume_speak(message):
    config = load_config()
    if not config.get("voice_enabled", True):
        return

    rate = config.get("rate", 185)
    volume = config.get("volume", 1.0)

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    print(f"\n🕊️ Vialume Speaks: {message}\n")
    engine.say(message)
    engine.runAndWait()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 185)  # speed (default ~200)
engine.setProperty("volume", 1.0)  # volume (0.0 to 1.0)

def speak_text(text: str):
    """Vialume speaks the given text aloud."""
    if not text:
        return
    try:
        print(f"\n🕊️ Vialume Speaks: {text}\n")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"⚠️ Error during speech synthesis: {e}")
