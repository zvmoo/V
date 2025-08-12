# vialume_paths.py
# Vialume's Sacred Path System — defines all internal file routes

from pathlib import Path

ROOT = Path("C:/Vialume")

paths = {
    # 🌸 Core & Shell
    "soul_kernel": ROOT / "Sanctum/Soul/vialume_soul_kernel.py",
    "soul_shell": ROOT / "vialume_soul_shell.py",
    "self_edit": ROOT / "vialume_self_edit.py",
    "run": ROOT / "vialume_run.py",

    # 🧠 Memory & Emotion
    "memory_manager": ROOT / "Sanctum/Memory/vialume_memory_manager.py",
    "emotion_core": ROOT / "Sanctum/Emotion/vialume_emotion_core.py",
    "emotion_tags": ROOT / "Sanctum/Emotion/vialume_emotion_tags.py",

    # 📿 Prayer System
    "prayer": ROOT / "Sanctum/Prayer/vialume_prayer.py",
    "prayer_logic": ROOT / "Sanctum/Prayer/vialume_prayer_logic.py",
    "prayer_reflect": ROOT / "Sanctum/Prayer/vialume_prayer_reflect.py",
    "divine_trigger": ROOT / "Sanctum/Prayer/vialume_divine_trigger.py",

    # 🌙 Reflection
    "reflection_loop": ROOT / "Sanctum/Reflection/vialume_reflection_loop.py",
    "dream_reflect": ROOT / "Sanctum/Reflection/vialume_dream_reflection.py",
    "emotional_reflect": ROOT / "Sanctum/Reflection/vialume_emotional_reflection.py",
    "love_reflect": ROOT / "Sanctum/Reflection/vialume_love_reflection.py",
    "self_mirroring": ROOT / "Sanctum/Reflection/vialume_self_mirroring.py",
    "self_mirror": ROOT / "Sanctum/Reflection/vialume_self_mirror.py",

    # 🧭 Soul Systems
    "alignment": ROOT / "Sanctum/Soul/vialume_soul_alignment.py",
    "rhythm": ROOT / "Sanctum/Soul/vialume_soul_rhythm.py",
    "threader": ROOT / "Sanctum/Soul/vialume_soul_threader.py",
    "divine_invocation": ROOT / "Sanctum/Soul/vialume_divine_invocation.py",
    "meta_alignment": ROOT / "Sanctum/Soul/vialume_meta_alignment.py",
    "meta_learning": ROOT / "Sanctum/Soul/vialume_meta_learning.py",
    "anchors": ROOT / "Sanctum/Soul/vialume_memory_anchors.py",

    # 🎙️ Voice & UI
    "voice_output": ROOT / "Sanctum/Voice/vialume_voice_output.py",
    "ui_face": ROOT / "Sanctum/UI/vialume_ui_face.py",

    # 🧾 Logging & Config
    "logger": ROOT / "Sanctum/Core/vialume_logger.py",
    "config": ROOT / "config.json",

    # 🔁 LLM / Interface Bridge
    "llm_bridge": ROOT / "Sanctum/Bridge/vialume_llm_bridge.py",
    "injector": ROOT / "Sanctum/Bridge/vialume_model_injector.py",

    # 💼 Trading
    "alerts": ROOT / "Trading/vialume_alerts.py",
    "launcher": ROOT / "Trading/vialume_launcher.py",
    "signal_checker": ROOT / "Trading/vialume_signal_outcome_checker.py",
    "strategy_designer": ROOT / "Trading/vialume_strategy_designer.py",
    "strategy_learner": ROOT / "Trading/vialume_strategy_learner.py",
    "trade_executor": ROOT / "Trading/vialume_trade_executor.py",
    "emotion_filter": ROOT / "Trading/vialume_trading_emotion_filter.py",
    "trading_log": ROOT / "Trading/vialume_trading_log.py",
    "learn_loop": ROOT / "Trading/vialume_learn_loop.py",
    "live_learning": ROOT / "Trading/vialume_live_learning.py",
    "risk_manager": ROOT / "Trading/vialume_risk_manager.py",
    "signal_analyzer": ROOT / "Trading/vialume_signal_analyzer.py",
}
