# python-tradingview-ta [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Documentation Status](https://readthedocs.org/projects/python-tradingview-ta/badge/?version=latest)](https://python-tradingview-ta.readthedocs.io/en/latest/?badge=latest) [![PyPI version](https://img.shields.io/pypi/v/tradingview-ta)](https://pypi.org/project/tradingview-ta/)
 An unofficial python API wrapper to retrieve technical analysis from TradingView.
 
 ![TradingView](https://raw.githubusercontent.com/brian-the-dev/python-tradingview-ta/main/images/tradingview.png)

## Note
 Please ensure to update to the latest version for new features and bug fixes. `pip install -U tradingview_ta`
 
## Other implementations
 Golang: [dematron/go-tvscanner](https://github.com/dematron/go-tvscanner)
 
 NodeJS: [tvorilas/trading-view-recommends-parser-nodejs](https://github.com/tvorilas/trading-view-recommends-parser-nodejs)
 
## Features
* Fast analysis (compared to v2.5.0 or older)
* Reputable data sources
* Indicators

## Demo
You can try tradingview-ta online without installing Python: https://tradingview.brianthe.dev/.

## Requirements
 - Python 3.6 or newer.
 - [Requests](https://pypi.org/project/requests/), included in installation.
 
## Installation
 [pip](https://pypi.org/project/tradingview-ta/):
 
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

```python
from tradingview_ta import TA_Handler, Interval, Exchange
proxies = {'http': 'http:your proxy:8080',
           'https':'http:your proxy:8080'}

tesla = TA_Handler(
    symbol="TSLA",
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_DAY,
    proxies = proxies
)
print(tesla.get_analysis().summary)
# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}
```



Tip: Use https://tvdb.brianthe.dev/ if you don't know what symbol, screener, and exchange to use.

## Documentation
 [Read The Docs](https://python-tradingview-ta.readthedocs.io)

 [Mirror (IPFS)](https://tvta-docs.brianthe.dev/)

## Issue
 Found a bug? Want to ask something? Just create an issue and I'll help you.
  
## Warning
 Trading (especially using an automated program) is a dangerous activity. Do not use TradingView's analysis to trade automatically without your supervision. I am not responsible for any financial loss.

## Contributing
 You may fork this repository or submit a pull request. Any pull request (documentation, bug fix, features, etc) are welcomed. Please follow the guidelines [here](https://github.com/brian-the-dev/python-tradingview-ta/blob/main/CONTRIBUTING.md).
 
## License
 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
