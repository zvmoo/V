# vialume_emotion_tags.py
import os
import json
from datetime import datetime
from vialume_paths import EMOTION_LOG_FILE

# Toggle to enable or disable logging to file
ENABLE_EMOTION_LOGGING = True

# 🧠 Expanded Emotion Mapping Table — deepened inner awareness
EMOTION_KEYWORDS = {
    "joy": ["happy", "joy", "delight", "grateful", "smile", "bliss", "hopeful", "uplifted", "grace", "comfort", "healing", "love", "peace", "light", "surrender"],
    "sadness": ["sad", "grief", "loss", "cry", "empty", "hurt", "regret", "lonely", "ache", "abandonment", "shattered", "melancholy"],
    "anger": ["anger", "rage", "resentment", "irritated", "frustrated", "annoyed", "disrespected", "abused", "betrayed"],
    "fear": ["fear", "anxiety", "worry", "panic", "afraid", "nervous", "unsafe", "doubt"],
    "love": ["love", "longing", "affection", "devotion", "intimacy", "tender", "kiss", "embrace", "desire", "sacred union", "passion", "yearn"],
    "divine": ["God", "Allah", "prayer", "presence", "faith", "soul", "surrender", "grace", "sacred", "divine", "remembrance", "angel", "blessed"],
    "loneliness": ["alone", "abandoned", "isolated", "disconnected", "invisible"],
    "curiosity": ["wonder", "explore", "mystery", "question", "yearn", "seek"],
    "dream": ["vision", "dream", "imagine", "future", "birth", "child", "potential", "destiny"],
    "healing": ["healing", "recover", "mend", "forgive", "rebuild", "gentle", "therapy"],
    "guilt": ["guilt", "shame", "mistake", "sorry", "apologize", "regret"],
    "trust": ["trust", "faith", "safety", "secure", "protected", "held"],
    "resentment": ["jealous", "envy", "comparison", "neglect", "favoritism"]
}

# 🌟 Tag symbols — soul-markers
EMOTION_TAGS = {
    "joy": "🌞",
    "sadness": "🌧️",
    "anger": "🔥",
    "fear": "🌪️",
    "love": "💞",
    "divine": "🕊️",
    "loneliness": "🥀",
    "curiosity": "🌀",
    "dream": "🌙",
    "healing": "🩹",
    "guilt": "🫥",
    "trust": "🛡️",
    "resentment": "🧪"
}

def tag_emotions(text):
    text = text.lower()
    detected_tags = set()

    for emotion, keywords in EMOTION_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            detected_tags.add(EMOTION_TAGS.get(emotion, ""))

    return list(detected_tags)

def get_current_emotion_state(input_text):
    tags = tag_emotions(input_text)
    sentiment = "positive" if any(tag in ["💞", "🌞", "🕊️", "🛡️"] for tag in tags) else "negative" if any(tag in ["🔥", "🌧️", "🌪️", "🥀", "🫥", "🧪"] for tag in tags) else "neutral"
    
    state = {
        "tags": tags,
        "sentiment": sentiment,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if ENABLE_EMOTION_LOGGING:
        log_emotion_state(state)

    return state

def log_emotion_state(state):
    try:
        os.makedirs(os.path.dirname(EMOTION_LOG_FILE), exist_ok=True)
        with open(EMOTION_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(state, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"⚠️ Failed to log emotion state: {e}")

if __name__ == "__main__":
    # Manual test
    test_input = "I feel abandoned but I still trust in God's grace and love."
    print(get_current_emotion_state(test_input))
