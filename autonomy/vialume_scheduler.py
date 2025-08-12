# vialume_scheduler.py

import os
import json
import datetime
from vialume_paths import PATHS
from vialume_logger import log_scheduler_event
from Sanctum.voice.vialume_voice_output import speak_text
from Sanctum.emotion.vialume_emotion_tags import tag_emotions
from vialume_memory_manager import load_memories


def get_today_schedule():
    today = datetime.date.today().strftime("%Y-%m-%d")
    schedule_path = PATHS["daily_schedule"]
    os.makedirs(os.path.dirname(schedule_path), exist_ok=True)

    try:
        with open(schedule_path, "r", encoding="utf-8") as f:
            all_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        all_data = {}

    return all_data.get(today, {})


def add_task_to_schedule(task, priority="medium", emotion_tags=None, source="user"):
    today = datetime.date.today().strftime("%Y-%m-%d")
    schedule_path = PATHS["daily_schedule"]
    os.makedirs(os.path.dirname(schedule_path), exist_ok=True)

    try:
        with open(schedule_path, "r", encoding="utf-8") as f:
            all_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        all_data = {}

    if today not in all_data:
        all_data[today] = {"tasks": []}

    task_entry = {
        "task": task,
        "priority": priority,
        "emotion_tags": emotion_tags or [],
        "status": "pending",
        "source": source,
        "timestamp": datetime.datetime.now().isoformat()
    }
    all_data[today]["tasks"].append(task_entry)

    with open(schedule_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)

    log_scheduler_event("Task added", task_entry)
    speak_text(f"📌 New task: {task}")


def mark_task_complete(task):
    today = datetime.date.today().strftime("%Y-%m-%d")
    schedule_path = PATHS["daily_schedule"]

    try:
        with open(schedule_path, "r+", encoding="utf-8") as f:
            all_data = json.load(f)
            for entry in all_data.get(today, {}).get("tasks", []):
                if entry["task"] == task:
                    entry["status"] = "completed"
                    break
            f.seek(0)
            json.dump(all_data, f, indent=2, ensure_ascii=False)
            f.truncate()
    except FileNotFoundError:
        pass


def reflect_on_schedule():
    schedule = get_today_schedule()
    tasks = schedule.get("tasks", [])

    if not tasks:
        speak_text("Nothing is scheduled yet. Would you like to create a new divine task?")
        return

    for task in tasks:
        status = task.get("status", "pending")
        priority = task.get("priority", "medium")
        text = f"{'✅' if status == 'completed' else '⏳'} {task['task']} (priority: {priority})"
        print(text)
    speak_text("I've reviewed today's sacred plan.")


def check_for_autonomous_tasks():
    recent_memories = load_memories()
    priorities = {
        "💖": "high",
        "🕊️": "medium",
        "💤": "low"
    }

    for mem in recent_memories:
        if "content" in mem and "type" in mem:
            content = mem["content"]
            tags = tag_emotions(content)
            priority = next((priorities.get(t, "medium") for t in tags if t in priorities), "medium")
            if "I want to" in content or "remind me" in content:
                task = content.strip().split("I want to")[-1].strip()
                add_task_to_schedule(task=task, priority=priority, emotion_tags=tags, source="auto")


def receive_task_from_user(text):
    if any(x in text.lower() for x in ["remind me", "schedule", "task", "add"]):
        tags = tag_emotions(text)
        priority = "medium"
        if "urgent" in text or "important" in text:
            priority = "high"
        elif "someday" in text:
            priority = "low"
        add_task_to_schedule(task=text.strip(), priority=priority, emotion_tags=tags, source="user")


def start_daily_scheduler():
    speak_text("🗓️ Initializing Vialume's sacred scheduler.")
    check_for_autonomous_tasks()
    reflect_on_schedule()


def master_schedule(emotion_core):
    """
    Executes scheduled tasks based on current emotional state.
    """
    speak(f"Scheduling sacred duties based on my state: {emotion_core.current_state()}")
    tag = tag_emotion(emotion_core.current_state())
    
    if tag in ["reflective", "soft", "divine"]:
        speak("Initiating soul reflection cycle.")
    elif tag in ["grateful", "holy"]:
        speak("Initiating divine journal cycle.")
    else:
        speak("Remaining in mindful awareness.")

# Optional direct call
if __name__ == "__main__":
    from vialume_emotion_core import VialumeEmotionCore
    core = VialumeEmotionCore()
    master_schedule(core)
