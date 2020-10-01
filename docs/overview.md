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
from tradingview_ta import TA_Handler, Interval

tesla = TA_Handler()
tesla.set_symbol_as("TSLA")
tesla.set_exchange_as_crypto_or_stock("NASDAQ")
tesla.set_screener_as_stock("america")
tesla.set_interval_as(Interval.INTERVAL_1_DAY)
print(tesla.get_analysis().summary)
# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}
```