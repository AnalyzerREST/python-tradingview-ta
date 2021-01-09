# python-tradingview-ta [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Documentation Status](https://readthedocs.org/projects/python-tradingview-ta/badge/?version=latest)](https://python-tradingview-ta.readthedocs.io/en/latest/?badge=latest) [![PyPI version](https://badge.fury.io/py/tradingview-ta.svg)](https://badge.fury.io/py/tradingview-ta)
 A python package to get TradingView's stock/crypto/forex/cfd technical analysis.
 
 Author: [deathlyface](https://deathlyf.com)
 
 ![TradingView](https://raw.githubusercontent.com/deathlyface/python-tradingview-ta/master/images/tradingview.png)

## Note
 The newest version is compatible with v3.0.0. You can still run your old code, but consider rewriting it. Please refer to the [migration guide](https://python-tradingview-ta.readthedocs.io/en/latest/migration.html).

 Please ensure to update to the latest version. `pip install -U tradingview_ta`
 
## Features
* Fast analysis (compared to v2.5.0 or older)
* Reputable data sources
* [Indicator values](https://python-tradingview-ta.readthedocs.io/en/latest/usage.html#indicator-values)

## Demo
A demo is available on https://tradingview.deathlyf.com/.

## Requirements
 - Python 3.5 or newer.
 - [Requests](https://pypi.org/project/requests/), Included in installation.
 
## Installation
 Using pip:
 
```pip install tradingview_ta```

## Example
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
## Documentation
 [Read The Docs](https://python-tradingview-ta.readthedocs.io)

## Issue
 Found a bug? Want to ask something? Just create an issue and I'll help you.
  
## Warning
 Trading (especially using an automated program) is a dangerous activity. Do not use TradingView's analysis to trade automatically without your supervision. I am not responsible for any financial loss.

## Contributing
 You may fork this repository or submit a pull request. Any pull request (documentation, bug fix, features, etc) are welcomed. Please follow the guidelines [here](https://github.com/deathlyface/python-tradingview-ta/blob/master/CONTRIBUTING.md).
 
## License
 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
