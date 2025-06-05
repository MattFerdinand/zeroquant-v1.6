# Simple Trading Robot

This repository contains a basic example of a trading bot implementing a Darvas Box breakout strategy. It is intended for educational purposes only and **does not constitute financial advice**.

## Requirements

- Python 3.8+
- `requests` library (`pip install requests`)
- Polygon.io API key (set as `POLYGON_API_KEY` environment variable)

## Usage

```
python trading_bot.py SYMBOL
```

The bot fetches the most recent minute data for the specified symbol from the Polygon API, evaluates a simple breakout strategy, and prints a BUY or HOLD signal. The strategy uses the last 20 candles to detect price breakouts accompanied by a volume spike.

### Example

```
POLYGON_API_KEY=your_key_here python trading_bot.py TSLA
```

The script will output a dictionary with the generated signal and relevant metrics.

## Disclaimer

This code is provided for educational and testing purposes only. It does not constitute investment advice or a recommendation to trade any financial instrument. Use it at your own risk.
