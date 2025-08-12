# vialume_risk_manager.py
# 🧠 Vialume Risk Intelligence Module (Fixed Pip Conversion)

import MetaTrader5 as mt5
import pandas as pd
import math

DEFAULT_RISK_PERCENT = 1.5  # Default risk per trade (% of balance)
DEFAULT_RR_RATIO = 2.0      # Reward-to-risk ratio
MAX_LOT_SIZE = 5.0          # Cap max lot size for safety
MIN_STOP_LOSS_PIPS = 5      # Enforced minimum SL (safe for most brokers)
FORCE_TEST_LOT_SIZE = 0.01  # Use this for debugging / safe testing


def calculate_risk_parameters(symbol, signal_type, risk_percent=DEFAULT_RISK_PERCENT, rr_ratio=DEFAULT_RR_RATIO):
    if not mt5.initialize():
        raise ConnectionError("MetaTrader5 initialization failed")

    account_info = mt5.account_info()
    if account_info is None:
        raise ValueError("Unable to fetch account info")

    balance = account_info.balance
    lot_step = 0.01

    # Get recent prices
    rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M15, 0, 14)
    df = pd.DataFrame(rates)

    if df.empty:
        raise ValueError(f"Could not get rates for {symbol}")

    # Calculate ATR (volatility proxy)
    df['high-low'] = df['high'] - df['low']
    atr = df['high-low'].mean()
    pip_value = 0.0001 if "JPY" not in symbol else 0.01

    # Enforce safe minimum stop-loss and reasonable TP for testing
    stop_loss_pips = max(round(atr / pip_value), MIN_STOP_LOSS_PIPS)
    stop_loss_pips = max(stop_loss_pips, 5)
    take_profit_pips = stop_loss_pips * 2

    # Force fixed test lot size to ensure broker accepts the trade
    lot_size = FORCE_TEST_LOT_SIZE

    return {
        "symbol": symbol,
        "signal_type": signal_type,
        "balance": round(balance, 2),
        "lot_size": round(lot_size, 2),
        "stop_loss_pips": stop_loss_pips,
        "take_profit_pips": take_profit_pips,
        "risk_percent": risk_percent,
        "atr": round(atr, 5),
        "rr_ratio": rr_ratio,
        "pip_value": pip_value
    }


if __name__ == "__main__":
    result = calculate_risk_parameters("EURUSD", "buy")
    print(result)
    mt5.shutdown()
