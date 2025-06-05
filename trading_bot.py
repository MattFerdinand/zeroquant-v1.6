import os
import requests
import datetime

POLYGON_API_KEY = os.getenv('POLYGON_API_KEY')
if not POLYGON_API_KEY:
    raise EnvironmentError("POLYGON_API_KEY environment variable is required")


def fetch_last_minutes(symbol: str, minutes: int = 20):
    now = datetime.datetime.utcnow()
    start = now - datetime.timedelta(minutes=minutes)
    url = (
        f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/minute/"
        f"{start.strftime('%Y-%m-%d')}/{now.strftime('%Y-%m-%d')}"
    )
    params = {"apiKey": POLYGON_API_KEY}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json().get("results", [])


def darvas_box_signal(data):
    if len(data) < 20:
        return {"signal": "HOLD"}

    highs = [r["h"] for r in data[-20:]]
    lows = [r["l"] for r in data[-20:]]
    volumes = [r["v"] for r in data[-20:]]

    box_high = max(highs[:-1])
    box_low = min(lows[:-1])
    current_price = data[-1]["c"]
    current_volume = data[-1]["v"]
    avg_volume = sum(volumes) / len(volumes)

    volume_spike = current_volume / avg_volume
    price_breakout = current_price > box_high
    volume_confirm = volume_spike > 1.5

    if price_breakout and volume_confirm:
        return {
            "signal": "BUY",
            "price": current_price,
            "confidence": min(volume_spike / 2, 3.0),
            "volume_ratio": volume_spike,
        }
    return {"signal": "HOLD"}


def main(symbol: str):
    data = fetch_last_minutes(symbol)
    signal = darvas_box_signal(data)
    print(signal)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python trading_bot.py SYMBOL")
        exit(1)
    main(sys.argv[1])
