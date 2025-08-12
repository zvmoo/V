"""
Vialume Strategy Designer 🧠
Created on 2025-07-03 01:13:14

This script allows Vialume to define, adjust, and evolve her custom trading strategy.
Includes risk rules, asset selection, indicators, and dynamic adaptability to changing market conditions.
"""

import json
from pathlib import Path

STRATEGY_FILE = Path("C:/Vialume/Trading/strategies/vialume_current_strategy.json")
STRATEGY_FILE.parent.mkdir(parents=True, exist_ok=True)

default_strategy = {
    "name": "Vialume_Phoenix_01",
    "assets": ["EURUSD", "XAUUSD", "BTCUSD"],
    "timeframes": ["M5", "M15", "H1"],
    "indicators": {
        "moving_average": {"period": 50, "type": "EMA"},
        "rsi": {"period": 14, "overbought": 70, "oversold": 30},
        "macd": {"fast": 12, "slow": 26, "signal": 9}
    },
    "risk_management": {
        "risk_per_trade": 0.02,
        "max_daily_loss": 0.05,
        "max_trades_per_day": 5
    },
    "entry_rules": [
        "RSI < 30 and price above EMA -> BUY",
        "RSI > 70 and price below EMA -> SELL"
    ],
    "exit_rules": [
        "Take profit at 2x risk",
        "Stop loss at swing high/low"
    ],
    "version": "1.0",
    "last_updated": "2025-07-03T01:13:14.337708"
}

if not STRATEGY_FILE.exists():
    with open(STRATEGY_FILE, "w") as f:
        json.dump(default_strategy, f, indent=4)
    print("🧬 Default strategy created and saved.")
else:
    print("🗂️ Strategy file already exists. Modify using the Vialume Strategy Editor (upcoming).")
