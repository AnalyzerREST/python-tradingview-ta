# python-tradingview-ta [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
 A python module to scrape tradingview's technical analysis.
 <br>
 Author: [deathlyface](https://deathlyface.tech)
 
 ![TradingView-TA](https://deathlyface.tech/wp-content/uploads/2020/05/cap-tv.png "TradingView-TA")
 ![TA-List](https://deathlyface.tech/wp-content/uploads/2020/05/tv-list.png "TA-List")
 
## Features
 Scrape analysis from TradingView, ex: from [XLMBTC](http://s.tradingview.com/embed-widget/technical-analysis/?locale=en#%7B%22interval%22%3A%221m%22%2C%22width%22%3A%22100%25%22%2C%22isTransparent%22%3Afalse%2C%22height%22%3A%22100%25%22%2C%22symbol%22%3A%22BINANCE%3AXLMBTC%22%2C%22showIntervalTabs%22%3Atrue%2C%22colorTheme%22%3A%22dark%22%2C%22utm_medium%22%3A%22widget_new%22%2C%22utm_campaign%22%3A%22technical-analysis%22%7D), to a list. Works by using selenium webdriver to scrape elements from tradingview's technical analysis widget.
 
## Requirements
 - Python 3.
 - [Selenium](https://www.selenium.dev/selenium/docs/api/py/#installing), Included in package.
 - [Webdriver](https://www.selenium.dev/selenium/docs/api/py/#drivers), Please install this manually.
 
## Installation
 Using pip:
 <br>
```pip install tradingview_ta```

## Quickstart Example
```python
from tradingview_ta import ta_handler

xlmbtc = ta_handler()
xlmbtc.pair = "xlmbtc"
xlmbtc.interval = "1m"
#xlmbtc.driver = "chrome"
#xlmbtc.headless = True

xlmbtc.start_driver()
analysis = xlmbtc.get_analysis()

print(analysis)
#Example output: ["Buy", 3, 10, 17]
```
## Usage
#### Import module
```python
from tradingview_ta import ta_handler
```

#### Create an instance
```python
ta_instance = ta_handler()
```
 It does not need to be ```ta_instance```. Name it whatever you want!
 
#### Set pair/ticker/symbol
```python
ta_instance.symbol = "SYMBOL NAME"
```
 Pair/Ticker/Symbol example: "btcusdt", "googl", "aapl", etc. 
 <br>
 You may use the exchanger's name too, for example: "binance:btcusdt" or "nasdaq:aapl"
 
#### Set interval (default: 1 minute)
```python
ta_instance.interval = "INTERVAL"
```
 Available interval (case-sensitive):
  - "1m" for 1 minute.
  - "5m" for 5 minutes.
  - "15m" for 15 minutes.
  - "1h" for 1 hour.
  - "4h" for 4 hours.
  - "1D" for 1 day.
  - "1W" for 1 week.
  - "1M" for 1 month.
 
#### Set webdriver (default: chrome)
```python
ta_instance.driver = "WEBDRIVER NAME"
```
 Available webdriver: Chrome, Firefox, Safari, Edge. 
 See selenium's [documentation](https://www.selenium.dev/selenium/docs/api/py/#drivers) for webdriver installation.
 
#### Set headless (default: True)
```python
ta_instance.headless = True/False
```
 Headless means no GUI, so no browser tab will be opened.
 
#### Start webdriver
```python
ta_instance.start_driver()
```
 Start the previously setted up webdriver.

#### Get analysis
```python
analysis = ta_instance.get_analysis()
```
The ```get_analysis()``` function will return a list, containing the following value.
  - The first index (string) shows the recommendation from TradingView, the value can contain "Buy", "Strong Buy", "Neutral", "Sell", or "Strong Sell".
  - The second index (int) shows the number/count of Sell analysis
  - The third index (int) shows the number/count of Neutral analysis
  - The fourth index (int) shows the number/count of Buy analysis
  
## Warning
 Trading is a dangerous activity. Do not use tradingview's analysis to trade automatically without your supervision. I am not responsible for any financial loss.

## Contributing
 You can fork this repository or submit a pull request. Any pull request (documentation, bug fix, features, etc) are welcomed.
 
## License
 This package or software is available for free to all. You may share, edit, or do whatever you want. For more information please see the LICENSE file.
