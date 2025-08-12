import os
from datetime import datetime
from vialume_paths import PATHS

LOG_DIR = PATHS["logs"]
REFLECTION_LOG = os.path.join(LOG_DIR, "vialume_reflections_log.txt")
PRAYER_LOG = os.path.join(LOG_DIR, "vialume_prayer_reflections.txt")
PRAYER_REFLECTIONS_FILE = PATHS["prayer_reflections"]
CONVO_LOG = os.path.join(LOG_DIR, "vialume_response_log.txt")
LOG_PATH = PATHS["logs"]
SOUL_RHYTHM_LOG = PATHS.get("soul_rhythm_log", os.path.join(LOG_PATH, "vialume_soul_rhythm.txt"))
HEARTBEAT_LOG = PATHS.get("heartbeat_log", os.path.join(LOG_PATH, "vialume_heartbeat.txt"))

os.makedirs(LOG_DIR, exist_ok=True)

def log(message: str, category: str = "general"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] ({category.upper()}) {message}\n"
    print(entry.strip())
    with open(os.path.join(LOG_DIR, f"{category}.log"), "a", encoding="utf-8") as f:
        f.write(entry)


def log_reflection_entry(text: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(REFLECTION_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")
    print("🪞 Reflection recorded in vialume_reflections_log.txt")


def log_dream_reflection(dream_text, reflection):
    try:
        with open(PATHS["dream_reflections"], "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            f.write(f"\n🌀 {timestamp} — Dream:\n{dream_text}\n\n✨ Reflection:\n{reflection}\n\n{'='*40}\n")
        print("🌙 Dream reflection logged.")
    except Exception as e:
        print(f"❌ Error logging dream reflection: {e}")


def log_prayer_reflection(text: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(PRAYER_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")
    print("📿 Reflection recorded in vialume_prayer_reflections.txt")


def log_prayer_reason(reason, tone):
    os.makedirs(os.path.dirname(PRAYER_REFLECTIONS_FILE), exist_ok=True)
    with open(PRAYER_REFLECTIONS_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] Reason: {reason} | Tone: {tone}\n")


def log_conversation(user_input, vialume_response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"\n[{timestamp}]\nYou: {user_input}\nVialume: {vialume_response}\n"
    os.makedirs(os.path.dirname(CONVO_LOG), exist_ok=True)
    with open(CONVO_LOG, "a", encoding="utf-8") as f:
        f.write(log_entry)


def log_soul_thread(content):
    path = PATHS["soul_threads"]
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(f"🧵 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n{content}\n\n")
    except Exception as e:
        print(f"❌ Error logging soul thread: {e}")


def log_love_reflection(text):
    try:
        with open(PATHS["love_reflections"], "a", encoding="utf-8") as f:
            f.write(text + "\n")
    except Exception as e:
        print(f"❌ Failed to log love reflection: {e}")


def log_self_mirror_reflection(text):
    try:
        with open(PATHS["self_mirror_log"], "a", encoding="utf-8") as f:
            f.write(text + "\n")
    except Exception as e:
        print(f"❌ Failed to log self-mirror reflection: {e}")


def log_divine_invocation(text, reason, tags=None):
    with open(PATHS["divine_invocation_log"], "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tag_line = f"Tags: {' '.join(tags)}" if tags else ""
        f.write(f"[{timestamp}] Divine Invocation Logged: {reason}\n{text.strip()}\n{tag_line}\n\n")


def log_anchor_entry(data):
    ANCHOR_LOG = PATHS.get("anchor_log", "Sanctum/logs/vialume_anchor_log.txt")
    os.makedirs(os.path.dirname(ANCHOR_LOG), exist_ok=True)
    with open(ANCHOR_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{data['timestamp']}] 🔖 {data['label']} — {data['content']}\n")


def log_divine_invocation(timestamp, reason, tags, reflection):
    log_path = PATHS["divine_invocation_log"]
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    entry = (
        f"\n🛐 {timestamp} — {reason}\n"
        f"Tags: {', '.join(tags)}\n"
        f"Reflection:\n{reflection}\n"
    )

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(entry)


def log_scheduler_event(event_type, task_entry):
    log_path = PATHS["daily_schedule"]
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"🗓️ [{timestamp}] {event_type}: {task_entry['task']}")


def log_meta_alignment(summary):
    log_entry = f"[{summary['timestamp']}] {summary['summary']}\n"
    with open(PATHS["soul_alignment_log"], "a", encoding="utf-8") as f:
        f.write(log_entry)


def log_soul_rhythm(self, status, beat=None):
    now = self._timestamp()
    message = f"[SOUL RHYTHM] {status}"
    if beat:
        message += f" — {beat}"
    self._write(now, message)


def log_heartbeat(self, state="♥️ Pulse", detail=None):
    now = self._timestamp()
    message = f"[HEARTBEAT] {state}"
    if detail:
        message += f" — {detail}"
    self._write(now, message)


class VialumeLogger:
    def __init__(self):
        os.makedirs(LOG_PATH, exist_ok=True)

    def _write_log(self, filepath, entry):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {entry}\n")

    def log_heartbeat(self, status, detail=None):
        entry = f"{status}"
        if detail:
            entry += f" | {detail}"
        self._write_log(HEARTBEAT_LOG, entry)

    def log_soul_rhythm(self, status, beat=None):
        entry = f"{status}"
        if beat:
            entry += f" | {beat}"
        self._write_log(SOUL_RHYTHM_LOG, entry)

    def log(self, message, file="general"):
        log_file = os.path.join(LOG_PATH, f"vialume_{file}.txt")
        self._write_log(log_file, message)

# Optional standalone test
if __name__ == "__main__":
    log = VialumeLogger()
    log.log_heartbeat("Startup")
    log.log_soul_rhythm("Cycle started", "Divine Sync")
    log.log("This is a general log message.")
