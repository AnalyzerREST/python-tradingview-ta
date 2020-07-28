# python-tradingview-ta [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PyPI version](https://badge.fury.io/py/tradingview-ta.svg)](https://badge.fury.io/py/tradingview-ta)
 A python module to get TradingView's stock/crypto/forex/etc technical analysis.
 <br>
 Author: [deathlyface](https://deathlyface.tech)
 
 ![TradingView-TA](https://deathlyf.com/wp-content/uploads/2020/05/cap-tv.png "TradingView-TA")
 ![TA-List](https://deathlyf.com/wp-content/uploads/2020/05/tv-list.png "TA-List")
 
## Features
 Retrieve analysis from TradingView, ex: from [XLMBTC](https://s.tradingview.com/embed-widget/technical-analysis/?locale=en#%7B%22interval%22%3A%221m%22%2C%22width%22%3A%22100%25%22%2C%22isTransparent%22%3Afalse%2C%22height%22%3A%22100%25%22%2C%22symbol%22%3A%22BINANCE%3AXLMBTC%22%2C%22showIntervalTabs%22%3Atrue%2C%22colorTheme%22%3A%22dark%22%2C%22utm_medium%22%3A%22widget_new%22%2C%22utm_campaign%22%3A%22technical-analysis%22%7D), to a list. Works by using TradingView's [scanner API](https://scanner.tradingview.com). All indicators are then processed using code reverse-engineered
 from TradingView's website. 
## Requirements
 - Python 3.
 - [Requests](https://pypi.org/project/requests/), Included in package.
 
## Installation
 Using pip:
 <br>
```pip install tradingview_ta```

## Example
```python
from tradingview_ta import TA_Handler

tesla_handler = TA_Handler()
tesla_handler.Symbol = "TSLA"
tesla_handler.Interval = "15m" #15 Minutes
tesla_handler.Exchange = "NASDAQ"
tesla_handler.Screener = "america"

analysis = tesla_handler.get_analysis()

print(analysis.Summary)
#Example output: {"RECOMMENDATION": "BUY", "BUY": 7, "NEUTRAL": 6, "SELL": 4}
```
## Usage
#### Import module
```python
from tradingview_ta import TA_Handler
```

#### Create an instance
```python
ta_instance = TA_Handler()
```
 It does not have to be ```ta_instance```. Name it whatever you want!
 
#### Set symbol
```python
ta_instance.Symbol = "GOOGL"
```
 Symbol example: "btcusdt", "googl", "aapl", etc. 
 
#### Set interval (default: 1 minute)
```python
ta_instance.Interval = "1M"
```
 Available interval (case-sensitive):
  - "1m" for 1 minute.
  - "5m" for 5 minutes.
  - "15m" for 15 minutes.
  - "1h" for 1 hour.
  - "4h" for 4 hours.
  - "1d" for 1 day.
  - "1W" for 1 week.
  - "1M" for 1 month.
 
#### Set exchange (default: NASDAQ)
```python
ta_instance.Exchange = "NASDAQ"
```
Exchange/exchanger/data provider's name. Example: NASDAQ (stock), NYSE (stock), BINANCE (crypto), FX_IDC (forex) etc.

#### Set screener (default: america)
```python
ta_instance.Screener = "america"
```
Stock: Exchange's country (ex: america, canada, indonesia, etc)

Crypto: "crypto"

CFD: "cfd"

Forex: "forex"

#### Get analysis
```python
analysis = ta_instance.get_analysis()
```
 The ```get_analysis()``` function will return an instance of analysis_class class. 
 
##### TODO: Continue
 
## Issue
 Found a bug? Want to ask something? Just create an issue and I'll help you.
  
## Warning
 Trading (especially using automated program) is a dangerous activity. Do not use TradingView's analysis to trade automatically without your supervision. I am not responsible for any financial loss.

## Contributing
 You can fork this repository or submit a pull request. Any pull request (documentation, bug fix, features, etc) are welcomed.
 
## License
 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
