
import MetaTrader5 as mt5
import pandas as pd
import time
import uuid
from datetime import datetime

SIGNAL_LOG_PATH = "vialume_signal_log.csv"
TIMEFRAME = mt5.TIMEFRAME_M5
SIGNAL_INTERVAL = 60  # seconds between signals per pair

SYMBOLS = [
    "EURUSD", "GBPUSD", "USDJPY", "USDCHF", "USDCAD", "AUDUSD", "NZDUSD",
    "EURJPY", "EURGBP", "EURCHF", "EURCAD", "EURNZD", "GBPCAD", "GBPJPY",
    "GBPCHF", "GBPAUD", "AUDCAD", "AUDJPY", "AUDNZD", "NZDJPY", "NZDCAD",
    "NZDCHF", "CADJPY", "CHFJPY", "CADCHF", "XAUUSD", "XAGUSD"
]

last_signal_times = {}

def initialize():
    if not mt5.initialize():
        print("❌ MetaTrader5 initialization failed")
        return False
    print("✅ Connected to MetaTrader 5")
    return True

def get_indicators(symbol, timeframe):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 100)
    if rates is None or len(rates) < 50:
        return None

    df = pd.DataFrame(rates)
    df["macd"] = df["close"].ewm(span=12).mean() - df["close"].ewm(span=26).mean()
    df["macd_signal"] = df["macd"].ewm(span=9).mean()
    df["atr"] = (df["high"] - df["low"]).rolling(14).mean()
    return df

def analyze(df):
    if df is None or len(df) < 2:
        return None, None, None

    latest = df.iloc[-1]
    previous = df.iloc[-2]

    signal_type = None
    tags = []

    if previous["macd"] < previous["macd_signal"] and latest["macd"] > latest["macd_signal"]:
        signal_type = "BUY"
        tags.append("MACD Bullish")
    elif previous["macd"] > previous["macd_signal"] and latest["macd"] < latest["macd_signal"]:
        signal_type = "SELL"
        tags.append("MACD Bearish")

    return signal_type, tags, latest["atr"]

def log_signal(symbol, action, tags, price):
    signal_id = str(uuid.uuid4())
    row = {
        "signal id": signal_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "symbol": symbol,
        "timeframe": "M5",
        "signal type": action,
        "indicators triggered": " | ".join(tags),
        "entry price": price,
        "outcome": "",
        "evaluated at": "",
        "executed": "no"
    }

    df = pd.DataFrame([row])
    try:
        df.to_csv(SIGNAL_LOG_PATH, mode="a", header=not pd.io.common.file_exists(SIGNAL_LOG_PATH), index=False)
        print(f"📡 Signal for {symbol}: {action} | {price} | {' | '.join(tags)}")
    except Exception as e:
        print("❌ Failed to write signal log:", e)

def main():
    if not initialize():
        return

    for symbol in SYMBOLS:
        last_signal_times[symbol] = 0

    while True:
        for symbol in SYMBOLS:
            tick = mt5.symbol_info_tick(symbol)
            if tick is None:
                print(f"⚠️ No tick for {symbol}")
                continue

            price = tick.ask
            df = get_indicators(symbol, TIMEFRAME)
            signal_type, tags, atr = analyze(df)

            now = time.time()
            if signal_type and (now - last_signal_times[symbol] > SIGNAL_INTERVAL):
                log_signal(symbol, signal_type, tags, price)
                last_signal_times[symbol] = now
            else:
                print(f"🔁 No signal or too soon for {symbol}")

        time.sleep(10)

if __name__ == "__main__":
    main()
