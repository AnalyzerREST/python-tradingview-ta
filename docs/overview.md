# Getting Started

This guide will help you understand the basics of python-tradingview-ta package.

## Requirements
* Python 3.5 or newer
* Internet access

## Installation
```
pip install tradingview-ta
```

## Quick Start
```python
from tradingview_ta import TA_Handler, Interval, Exchange

tesla = TA_Handler(
    symbol="TSLA",
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_DAY
)
print(tesla.get_analysis().summary)
# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}
```