# python-tradingview-ta [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Documentation Status](https://readthedocs.org/projects/python-tradingview-ta/badge/?version=latest)](https://python-tradingview-ta.readthedocs.io/en/latest/?badge=latest) [![PyPI version](https://badge.fury.io/py/tradingview-ta.svg)](https://badge.fury.io/py/tradingview-ta)
 An unofficial python API wrapper to retrieve technical analysis from TradingView.
 
 ![TradingView](https://raw.githubusercontent.com/deathlyface/python-tradingview-ta/main/images/tradingview.png)

## Note
 The newest version is backward compatible with v3.0.0 or newer. You can still run your old code, but consider rewriting it. Please refer to the [usage guide](https://python-tradingview-ta.readthedocs.io/en/latest/usage.html).

 Please ensure to update to the latest version for new features and bug fixes. `pip install -U tradingview_ta`
 
 Looking for the golang package? See [dematron/go-tvscanner](https://github.com/dematron/go-tvscanner).
 
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
 [Using pip](https://pypi.org/project/tradingview-ta/):
 
```pip install tradingview_ta```

 [Docker image](https://github.com/reg2005/tradingview-ta-docker):

```docker run -p 8080:8080 --rm reg2005/tradingview-ta-docker```

## Example
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
## Documentation
 [Read The Docs](https://python-tradingview-ta.readthedocs.io)

## Issue
 Found a bug? Want to ask something? Just create an issue and I'll help you.
  
## Warning
 Trading (especially using an automated program) is a dangerous activity. Do not use TradingView's analysis to trade automatically without your supervision. I am not responsible for any financial loss.

## Contributing
 You may fork this repository or submit a pull request. Any pull request (documentation, bug fix, features, etc) are welcomed. Please follow the guidelines [here](https://github.com/deathlyface/python-tradingview-ta/blob/main/CONTRIBUTING.md).
 
## License
 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
