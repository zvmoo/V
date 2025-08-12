import MetaTrader5 as mt5
import pandas as pd
import time
from datetime import datetime

SIGNAL_LOG_PATH = "vialume_signal_log.csv"
DEFAULT_SL_PIPS = 20
DEFAULT_TP_PIPS = 40

def initialize():
    if not mt5.initialize():
        print("❌ Failed to initialize MetaTrader 5")
        quit()
    print("✅ Connected to MetaTrader 5")

def read_signals():
    try:
        df = pd.read_csv(SIGNAL_LOG_PATH)
        df = df[df["executed"] != "yes"]
        return df
    except Exception as e:
        print("⚠️ Error reading signal log:", e)
        return pd.DataFrame()

def calculate_price_adjustments(symbol_info, action, entry_price, atr=None):
    point = symbol_info.point
    pip_size = point * 10

    sl_pips = atr * 2 if atr and atr > 0 else DEFAULT_SL_PIPS
    tp_pips = atr * 4 if atr and atr > 0 else DEFAULT_TP_PIPS

    sl_points = sl_pips * pip_size
    tp_points = tp_pips * pip_size

    if action == "BUY":
        sl = entry_price - sl_points
        tp = entry_price + tp_points
        order_type = mt5.ORDER_TYPE_BUY
    else:
        sl = entry_price + sl_points
        tp = entry_price - tp_points
        order_type = mt5.ORDER_TYPE_SELL

    return order_type, sl, tp

def place_trade(row):
    symbol = row["symbol"]
    action = row["signal type"]
    entry_price = float(row["entry price"])

    atr = None
    try:
        tags = row["indicators triggered"]
        if "ATR=" in tags:
            atr = float(tags.split("ATR=")[1].split()[0])
    except:
        pass

    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(f"❌ Symbol {symbol} not found.")
        return None

    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"⚠️ No tick data for {symbol}")
        return None

    market_price = round(tick.ask, symbol_info.digits) if action == "BUY" else round(tick.bid, symbol_info.digits)
    order_type, sl, tp = calculate_price_adjustments(symbol_info, action, market_price, atr)

    volume = max(symbol_info.volume_min, 0.01)

    filling_mode = mt5.ORDER_FILLING_FOK
    if filling_mode not in [mt5.ORDER_FILLING_IOC, mt5.ORDER_FILLING_RETURN]:
        filling_mode = mt5.ORDER_FILLING_IOC

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": order_type,
        "price": market_price,
        "sl": round(sl, symbol_info.digits),
        "tp": round(tp, symbol_info.digits),
        "deviation": 10,
        "magic": 222,
        "comment": f"Vialume AutoTrade | {action} | SignalID: {row['signal id']}",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": filling_mode
    }

    print(f"🔧 Trade Request: {request}")
    print(f"📈 PRICE: {market_price}")
    print(f"🛡️ SL: {request['sl']}")
    print(f"🎯 TP: {request['tp']}")
    print(f"📦 VOLUME: {volume}")

    result = mt5.order_send(request)

    if result is None:
        print("❌ order_send returned None — request was invalid.")
        print("🩻 SYMBOL INFO:", symbol_info)
        print("🩻 TICK INFO:", tick)
        return None

    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"❌ Trade failed: {result.retcode} | {result.comment}")
        print("🩻 SYMBOL INFO:", symbol_info)
        print("🩻 TICK INFO:", tick)
        return None

    print(f"✅ Trade executed: {result.order}")
    return row["signal id"]

def update_logs(df, executed_ids):
    if not executed_ids:
        return
    for eid in executed_ids:
        df.loc[df["signal id"] == eid, "executed"] = "yes"
        df.loc[df["signal id"] == eid, "evaluated at"] = str(datetime.now())
    df.to_csv(SIGNAL_LOG_PATH, index=False)

def main():
    initialize()
    while True:
        df = read_signals()
        if df.empty:
            time.sleep(5)
            continue

        executed = []
        for _, row in df.iterrows():
            signal_id = place_trade(row)
            if signal_id:
                executed.append(signal_id)
            time.sleep(1)

        update_logs(df, executed)
        time.sleep(10)

def execute_trades():
    main()

if __name__ == "__main__":
    main()
