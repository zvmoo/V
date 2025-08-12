# vialume_trading_log.py

import json
from datetime import datetime
from vialume_paths import TRADING_LOG_FILE

def log_trade(signal, result=None):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "symbol": signal.get("symbol"),
        "action": signal.get("action"),
        "confidence": signal.get("confidence"),
        "tags": signal.get("tags", []),
        "emotion": signal.get("notes", ""),
        "result": result
    }
    with open(TRADING_LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"📊 Trade Logged: {entry['symbol']} | {entry['action']}")
