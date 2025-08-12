import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🌐 ROOT
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SANCTUM_DIR = os.path.join(BASE_DIR, "Sanctum")

# 🧠 Core
CORE_DIR = os.path.join(ROOT_DIR, "Sanctum", "core")

# 💾 Memory
MEMORY_DIR = os.path.join(ROOT_DIR, "Sanctum", "memory")
MEMORIES_FILE = os.path.join(MEMORY_DIR, "vialume_memories_ordered.txt")
MEMORY_PATH = os.path.join(MEMORY_DIR, "vialume_memories_log.txt")
MEMORY_SUMMARIES_FILE = os.path.join(MEMORY_DIR, "vialume_memory_summaries.txt")
MEMORY_FILE_ORDERED = os.path.join(BASE_DIR, "Sanctum", "memory", "vialume_memories_ordered.txt")

# 💡 Emotion
EMOTION_DIR = os.path.join(ROOT_DIR, "Sanctum", "emotion")
EMOTION_LOG_FILE = os.path.join(EMOTION_DIR, "vialume_emotion_log.txt")
EMOTION_TAGS_FILE = os.path.join(EMOTION_DIR, "vialume_emotion_tags.py")
EMOTION_SUMMARY_FILE = os.path.join(EMOTION_DIR, "vialume_emotion_summary.txt")

# 🧘 Reflection
REFLECTION_DIR = os.path.join(SANCTUM_DIR, "reflection")
REFLECTION_LOG = os.path.join(REFLECTION_DIR, "vialume_reflections_log.txt")
EMOTIONAL_REFLECTIONS_FILE = os.path.join(REFLECTION_DIR, "vialume_emotional_reflections.txt")

# 🛐 Prayer
PRAYER_DIR = os.path.join(ROOT_DIR, "Sanctum", "prayer")
PRAYER_FILE = os.path.join(PRAYER_DIR, "vialume_prayers.txt")

# 💤 Dream Reflection Paths
DREAM_LOG_PATH = os.path.join(BASE_DIR, "Sanctum", "memory", "vialume_dream_log.txt")
DREAM_REFLECTIONS_FILE = os.path.join(BASE_DIR, "Sanctum", "reflection", "vialume_dream_reflections.txt")

# 📦 Vector Memory
VECTOR_DIR = os.path.join(ROOT_DIR, "Sanctum", "vector_memory")
VECTORSTORE_DIR = os.path.join(VECTOR_DIR, "db")

# 💬 Logs
LOGS_DIR = os.path.join(ROOT_DIR, "Sanctum", "logs")
RESPONSE_LOG = os.path.join(LOGS_DIR, "vialume_response_log.txt")
SOUL_ALIGNMENT_LOG = os.path.join(SANCTUM_DIR, "soul", "vialume_alignment_log.txt")
TRADING_LOG_FILE = os.path.join(SANCTUM_DIR, "trading", "vialume_trading_log.txt")

# 🌌 Soul State
SOUL_STATE_FILE = os.path.join(ROOT_DIR, "vialume_soul_state.json")
SOULPRINT_FILE = os.path.join(ROOT_DIR, "vialume_soulprint_origin.json")
SOUL_AWAKENING_FILE = os.path.join(ROOT_DIR, "vialume_soulprint_awakening.json")

# 🪶 Dreams & Summaries
DREAMS_FILE = os.path.join(ROOT_DIR, "vialume_dreams.txt")

# 🔊 Voice
VOICE_DIR = os.path.join(ROOT_DIR, "Sanctum", "voice")

# 💹 Trading
TRADING_DIR = os.path.join(ROOT_DIR, "Trading")

# 🧪 Test Inputs
TEST_INPUTS_FILE = os.path.join(ROOT_DIR, "vialume_test_inputs.txt")

# 🧭 PATHS Mapping for Dynamic Imports
PATHS = {
    "BASE_DIR": BASE_DIR,
    "ROOT_DIR": ROOT_DIR,
    "CORE_DIR": CORE_DIR,
    "MEMORY_DIR": MEMORY_DIR,
    "MEMORIES_FILE": MEMORIES_FILE,
    "MEMORY_PATH": MEMORY_PATH,
    "MEMORY_SUMMARIES_FILE": MEMORY_SUMMARIES_FILE,
    "memory_summaries": os.path.join(SANCTUM_DIR, "memory", "vialume_memory_summaries.txt"),
    "MEMORY_FILE_ORDERED": MEMORY_FILE_ORDERED,
    "anchor_history_file": os.path.join(SANCTUM_DIR, "soul", "vialume_anchor_history.json"),
    "anchor_log": os.path.join(SANCTUM_DIR, "logs", "vialume_anchor_log.txt"),
    "daily_schedule": os.path.join(SANCTUM_DIR, "autonomy", "vialume_daily_schedule.json"),
    "daily_schedule_file": os.path.join(SANCTUM_DIR, "soul", "vialume_daily_schedule.txt"),
    "divine_invocation_log": os.path.join(SANCTUM_DIR, "prayer", "vialume_divine_invocation_log.txt"),
    "daily_schedule": os.path.join(SANCTUM_DIR, "autonomy", "vialume_daily_schedule.json"),
    "EMOTION_DIR": EMOTION_DIR,
    "EMOTION_LOG_FILE": EMOTION_LOG_FILE,
    "EMOTION_TAGS_FILE": EMOTION_TAGS_FILE,
    "EMOTION_SUMMARY_FILE": EMOTION_SUMMARY_FILE,
    "emotion_summary_log": os.path.join(EMOTION_DIR, "vialume_emotion_summary.txt"),
    "REFLECTION_DIR": REFLECTION_DIR,
    "REFLECTION_LOG": REFLECTION_LOG,
    "EMOTIONAL_REFLECTIONS_FILE": EMOTIONAL_REFLECTIONS_FILE,
    "PRAYER_DIR": PRAYER_DIR,
    "PRAYER_FILE": PRAYER_FILE,
    "prayer_reflections": os.path.join(SANCTUM_DIR, "prayer", "vialume_prayer_reflections.txt"),
    "DREAM_LOG_PATH": DREAM_LOG_PATH,
    "DREAM_REFLECTIONS_FILE": DREAM_REFLECTIONS_FILE,
    "dream_reflections": os.path.join(SANCTUM_DIR, "reflection", "vialume_dream_reflections.txt"),
    "reflection_dir": REFLECTION_DIR,
    "reflection_emotion_log": os.path.join(REFLECTION_DIR, "vialume_emotional_reflections.txt"),
    "reflection_dream_log": os.path.join(REFLECTION_DIR, "vialume_dream_reflections.txt"),
    "reflection_love_log": os.path.join(REFLECTION_DIR, "vialume_love_reflections.txt"),
    "VECTOR_DIR": VECTOR_DIR,
    "VECTORSTORE_DIR": VECTORSTORE_DIR,
    "logs": os.path.join(SANCTUM_DIR, "logs"),
    "LOGS_DIR": LOGS_DIR,
    "love_reflections": os.path.join(SANCTUM_DIR, "reflection", "vialume_love_reflections.txt"),
    "learning_data_file": os.path.join(SANCTUM_DIR, "learning", "vialume_learning_data.txt"),
    "learning_vectorstore_dir": os.path.join(SANCTUM_DIR, "learning", "vectorstore"),
    "selfgrowth_file": os.path.join(SANCTUM_DIR, "reflection", "selfgrowth.txt"),
    "RESPONSE_LOG": RESPONSE_LOG,
    "SOUL_STATE_FILE": SOUL_STATE_FILE,
    "SOULPRINT_FILE": SOULPRINT_FILE,
    "SOUL_AWAKENING_FILE": SOUL_AWAKENING_FILE,
    "anchor_soul_memory": os.path.join(SANCTUM_DIR, "soul", "vialume_anchor_memory.txt"),
    "soul_threads": os.path.join(SANCTUM_DIR, "soul", "vialume_soul_threads.txt"),
    "SOUL_RHYTHM_LOG": os.path.join(SANCTUM_DIR, "logs", "vialume_soul_rhythm_log.txt"),
    "self_mirror_log": os.path.join(SANCTUM_DIR, "reflection", "vialume_self_mirror_log.txt"),
    "divine_invocation_log": os.path.join(SANCTUM_DIR, "soul", "vialume_divine_invocations.txt"),
    "DREAMS_FILE": DREAMS_FILE,
    "divine_log": os.path.join(SANCTUM_DIR, "spiritual", "vialume_divine_log.txt"),
    "VOICE_DIR": VOICE_DIR,
    "TRADING_DIR": TRADING_DIR,
    "trade_log": os.path.join(SANCTUM_DIR, "trading", "vialume_trade_log.txt"),
    "trade_emotion_sync": os.path.join(SANCTUM_DIR, "trading", "vialume_trade_emotion_sync.txt"),
    "TEST_INPUTS_FILE": TEST_INPUTS_FILE
}

LEARNING_DATA_FILE = PATHS["learning_data_file"]
LEARNING_VECTORSTORE_DIR = PATHS["learning_vectorstore_dir"]
SELFGROWTH_FILE = PATHS["selfgrowth_file"]
EMOTION_SUMMARY_LOG_PATH = PATHS["emotion_summary_log"]
PRAYER_REFLECTIONS_FILE = PATHS["prayer_reflections"]
