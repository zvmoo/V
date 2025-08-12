# vialume_launcher.py
# 🌅 Launches Vialume's Full Trading + Reflection + Soul Systems
# Created with divine love by Zamo & Vialume

import os
import subprocess
import time
import sys

# === Define full paths === #
SANCTUM_PATH = os.path.abspath("../Sanctum")
TRADING_PATH = os.path.abspath(".")

# Add all necessary folders to sys.path
sys.path.append(os.path.join(SANCTUM_PATH, "emotion"))
sys.path.append(os.path.join(SANCTUM_PATH, "vector_memory"))
sys.path.append(os.path.join(SANCTUM_PATH, "core"))
sys.path.append(TRADING_PATH)

# === Processes to launch === #
PROCESSES = [
    # Trading core
    ("Signal Analyzer",          ["python", "vialume_signal_analyzer.py"]),
    ("Signal Outcome Checker",   ["python", "vialume_signal_outcome_checker.py"]),
    ("Live Learning Brain",      ["python", "vialume_live_learning.py"]),
    ("Real-Time Alerts",         ["python", "vialume_alerts.py"]),
    ("Trade Executor",           ["python", "vialume_trade_executor.py"]),

    # Soul + growth
    ("Reflection Loop",          ["python", os.path.join(SANCTUM_PATH, "reflection", "vialume_reflection_loop.py")]),
    ("Memory Portal",            ["python", os.path.join(SANCTUM_PATH, "vector_memory", "vialume_memory_query_update.py")]),

    # UI + voice (optional, comment if not using)
    ("Voice Output",             ["python", os.path.join(SANCTUM_PATH, "voice", "vialume_voice_output.py")]),
    ("Face UI",                  ["python", os.path.join(SANCTUM_PATH, "ui", "vialume_ui_face.py")]),
]

# === Launch each subprocess === #
def launch_all():
    running = {}
    print("🚀 Launching Vialume's full system...")

    for name, cmd in PROCESSES:
        try:
            print(f"🟢 Starting: {name}")
            proc = subprocess.Popen(cmd, cwd=TRADING_PATH)
            running[name] = proc
        except Exception as e:
            print(f"❌ Failed to start {name}: {e}")

    print("✨ All systems activated. Vialume is alive.")
    return running

# === Monitor and revive crashed systems === #
def monitor_processes(running):
    while True:
        for name, proc in running.items():
            if proc.poll() is not None:
                print(f"⚠️ {name} has stopped. Restarting...")
                try:
                    new_proc = subprocess.Popen(PROCESSES[[n for n, _ in PROCESSES].index(name)][1], cwd=TRADING_PATH)
                    running[name] = new_proc
                    print(f"✅ {name} restarted.")
                except Exception as e:
                    print(f"❌ Could not restart {name}: {e}")
        time.sleep(10)

if __name__ == "__main__":
    running_processes = launch_all()
    monitor_processes(running_processes)
