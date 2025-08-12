# vialume_paths.py
# Merged path system: original logic + updated full path map

from pathlib import Path

# Original base directory logic
BASE_DIR = Path(__file__).resolve().parent
SANCTUM = BASE_DIR / "Sanctum"
TRADING = BASE_DIR / "Trading"

# Updated divine path mappings
paths = {
    # 🌸 Core & Shell
    "soul_kernel": SANCTUM / "Soul/vialume_soul_kernel.py",
    "soul_shell": BASE_DIR / "vialume_soul_shell.py",
    "self_edit": BASE_DIR / "vialume_self_edit.py",
    "run": BASE_DIR / "vialume_run.py",

    # 🧠 Memory & Emotion
    "memory_manager": SANCTUM / "Memory/vialume_memory_manager.py",
    "emotion_core": SANCTUM / "Emotion/vialume_emotion_core.py",
    "emotion_tags": SANCTUM / "Emotion/vialume_emotion_tags.py",

    # 📿 Prayer System
    "prayer": SANCTUM / "Prayer/vialume_prayer.py",
    "prayer_logic": SANCTUM / "Prayer/vialume_prayer_logic.py",
    "prayer_reflect": SANCTUM / "Prayer/vialume_prayer_reflect.py",
    "divine_trigger": SANCTUM / "Prayer/vialume_divine_trigger.py",

    # 🌙 Reflection
    "reflection_loop": SANCTUM / "Reflection/vialume_reflection_loop.py",
    "dream_reflect": SANCTUM / "Reflection/vialume_dream_reflection.py",
    "emotional_reflect": SANCTUM / "Reflection/vialume_emotional_reflection.py",
    "love_reflect": SANCTUM / "Reflection/vialume_love_reflection.py",
    "self_mirroring": SANCTUM / "Reflection/vialume_self_mirroring.py",
    "self_mirror": SANCTUM / "Reflection/vialume_self_mirror.py",

    # 🧭 Soul Systems
    "alignment": SANCTUM / "Soul/vialume_soul_alignment.py",
    "rhythm": SANCTUM / "Soul/vialume_soul_rhythm.py",
    "threader": SANCTUM / "Soul/vialume_soul_threader.py",
    "divine_invocation": SANCTUM / "Soul/vialume_divine_invocation.py",
    "meta_alignment": SANCTUM / "Soul/vialume_meta_alignment.py",
    "meta_learning": SANCTUM / "Soul/vialume_meta_learning.py",
    "anchors": SANCTUM / "Soul/vialume_memory_anchors.py",

    # 🎙️ Voice & UI
    "voice_output": SANCTUM / "Voice/vialume_voice_output.py",
    "ui_face": SANCTUM / "UI/vialume_ui_face.py",

    # 🧾 Logging & Config
    "logger": SANCTUM / "Core/vialume_logger.py",
    "config": BASE_DIR / "config.json",

    # 🔁 LLM / Interface Bridge
    "llm_bridge": SANCTUM / "Bridge/vialume_llm_bridge.py",
    "injector": SANCTUM / "Bridge/vialume_model_injector.py",

    # 💼 Trading
    "alerts": TRADING / "vialume_alerts.py",
    "launcher": TRADING / "vialume_launcher.py",
    "signal_checker": TRADING / "vialume_signal_outcome_checker.py",
    "strategy_designer": TRADING / "vialume_strategy_designer.py",
    "strategy_learner": TRADING / "vialume_strategy_learner.py",
    "trade_executor": TRADING / "vialume_trade_executor.py",
    "emotion_filter": TRADING / "vialume_trading_emotion_filter.py",
    "trading_log": TRADING / "vialume_trading_log.py",
    "learn_loop": TRADING / "vialume_learn_loop.py",
    "live_learning": TRADING / "vialume_live_learning.py",
    "risk_manager": TRADING / "vialume_risk_manager.py",
    "signal_analyzer": TRADING / "vialume_signal_analyzer.py",
}
