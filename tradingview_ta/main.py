# Tradingview Technical Analysis (tradingview-ta)
# Author: deathlyface (https://github.com/deathlyface)
# License: MIT

import requests, json, datetime, warnings
from .technicals import Compute

__version__ = "3.2.6"

class Analysis(object):
    exchange = ""
    symbol = ""
    screener = ""
    time = ""
    interval = ""
    summary = {}
    oscillators = {}
    moving_averages = {}
    indicators = {}

class Interval:
    INTERVAL_1_MINUTE = "1m"
    INTERVAL_5_MINUTES = "5m"
    INTERVAL_15_MINUTES = "15m"
    INTERVAL_1_HOUR = "1h"
    INTERVAL_4_HOURS = "4h"
    INTERVAL_1_DAY = "1d"
    INTERVAL_1_WEEK = "1W"
    INTERVAL_1_MONTH = "1M"

class Exchange:
    FOREX = "FX_IDC"
    CFD = "TVC"


class TradingView:
    # Note: Please DO NOT modify the order or DELETE existing indicators, it will break the technical analysis. You may APPEND custom indicator to the END of the list.
    indicators = ["Recommend.Other","Recommend.All","Recommend.MA","RSI","RSI[1]","Stoch.K","Stoch.D","Stoch.K[1]","Stoch.D[1]","CCI20","CCI20[1]","ADX","ADX+DI","ADX-DI","ADX+DI[1]","ADX-DI[1]","AO","AO[1]","Mom","Mom[1]","MACD.macd","MACD.signal","Rec.Stoch.RSI","Stoch.RSI.K","Rec.WR","W.R","Rec.BBPower","BBPower","Rec.UO","UO","close","EMA5","SMA5","EMA10","SMA10","EMA20","SMA20","EMA30","SMA30","EMA50","SMA50","EMA100","SMA100","EMA200","SMA200","Rec.Ichimoku","Ichimoku.BLine","Rec.VWMA","VWMA","Rec.HullMA9","HullMA9","Pivot.M.Classic.S3","Pivot.M.Classic.S2","Pivot.M.Classic.S1","Pivot.M.Classic.Middle","Pivot.M.Classic.R1","Pivot.M.Classic.R2","Pivot.M.Classic.R3","Pivot.M.Fibonacci.S3","Pivot.M.Fibonacci.S2","Pivot.M.Fibonacci.S1","Pivot.M.Fibonacci.Middle","Pivot.M.Fibonacci.R1","Pivot.M.Fibonacci.R2","Pivot.M.Fibonacci.R3","Pivot.M.Camarilla.S3","Pivot.M.Camarilla.S2","Pivot.M.Camarilla.S1","Pivot.M.Camarilla.Middle","Pivot.M.Camarilla.R1","Pivot.M.Camarilla.R2","Pivot.M.Camarilla.R3","Pivot.M.Woodie.S3","Pivot.M.Woodie.S2","Pivot.M.Woodie.S1","Pivot.M.Woodie.Middle","Pivot.M.Woodie.R1","Pivot.M.Woodie.R2","Pivot.M.Woodie.R3","Pivot.M.Demark.S1","Pivot.M.Demark.Middle","Pivot.M.Demark.R1", "open", "P.SAR", "BB.lower", "BB.upper", "AO[2]", "volume"]

    scan_url = "https://scanner.tradingview.com/"

    def data(symbols, interval, indicators):
        """Format TradingView's Scanner Post Data

        Args:
            symbols (list): List of EXCHANGE:SYMBOL (ex: ["NASDAQ:AAPL"] or ["BINANCE:BTCUSDT"])
            interval (string): Time Interval (ex: 1m, 5m, 15m, 1h, 4h, 1d, 1W, 1M)

        Returns:
            string: JSON object as a string.
        """
        if interval == "1m":
            # 1 Minute
            data_interval = "|1"
        elif interval == "5m":
            # 5 Minutes
            data_interval = "|5"
        elif interval == "15m":
            # 15 Minutes
            data_interval = "|15"
        elif interval == "1h":
            # 1 Hour
            data_interval = "|60"
        elif interval == "4h":
            # 4 Hour
            data_interval = "|240"
        elif interval == "1W":
            # 1 Week
            data_interval = "|1W"
        elif interval == "1M":
            # 1 Month
            data_interval = "|1M"
        else:
            if interval != '1d':
                warnings.warn("Interval is empty or not valid, defaulting to 1 day.")
            # Default, 1 Day
            data_interval = ""
            
        data_json = {"symbols":{"tickers":[symbol.upper() for symbol in symbols],"query":{"types":[]}},"columns":[x + data_interval for x in indicators]}

        return data_json

def calculate(indicators, indicators_key, screener, symbol, exchange, interval):
    oscillators_counter, ma_counter = {"BUY": 0, "SELL": 0, "NEUTRAL": 0}, {"BUY": 0, "SELL": 0, "NEUTRAL": 0}
    computed_oscillators, computed_ma = {}, {}

    indicators = list(indicators.values())

    # RECOMMENDATIONS
    recommend_oscillators = Compute.Recommend(indicators[0])
    recommend_summary = Compute.Recommend(indicators[1])
    recommend_moving_averages = Compute.Recommend(indicators[2])

    # OSCILLATORS
    # RSI (14)
    if None not in indicators[3:5]:
        computed_oscillators["RSI"] = Compute.RSI(indicators[3], indicators[4])
        oscillators_counter[computed_oscillators["RSI"]] += 1
    # Stoch %K
    if None not in indicators[5:9]:
        computed_oscillators["STOCH.K"] = Compute.Stoch(indicators[5], indicators[6], indicators[7], indicators[8])
        oscillators_counter[computed_oscillators["STOCH.K"]] += 1
    # CCI (20)
    if None not in indicators[9:11]:
        computed_oscillators["CCI"] = Compute.CCI20(indicators[9], indicators[10])
        oscillators_counter[computed_oscillators["CCI"]] += 1
    # ADX (14)
    if None not in indicators[11:16]:
        computed_oscillators["ADX"] = Compute.ADX(indicators[11], indicators[12], indicators[13], indicators[14], indicators[15])
        oscillators_counter[computed_oscillators["ADX"]] += 1
    # AO
    if None not in indicators[16:18] and indicators[86] != None:
        computed_oscillators["AO"] = Compute.AO(indicators[16], indicators[17], indicators[86])
        oscillators_counter[computed_oscillators["AO"]] += 1
    # Mom (10)
    if None not in indicators[18:20]:
        computed_oscillators["Mom"] = Compute.Mom(indicators[18], indicators[19])
        oscillators_counter[computed_oscillators["Mom"]] += 1
    # MACD
    if None not in indicators[20:22]:
        computed_oscillators["MACD"] = Compute.MACD(indicators[20], indicators[21])
        oscillators_counter[computed_oscillators["MACD"]] += 1
    # Stoch RSI
    if indicators[22] != None:
        computed_oscillators["Stoch.RSI"] = Compute.Simple(indicators[22])
        oscillators_counter[computed_oscillators["Stoch.RSI"]] += 1
    # W%R
    if indicators[24] != None:
        computed_oscillators["W%R"] = Compute.Simple(indicators[24])
        oscillators_counter[computed_oscillators["W%R"]] += 1
    # BBP
    if indicators[26] != None:
        computed_oscillators["BBP"] = Compute.Simple(indicators[26])
        oscillators_counter[computed_oscillators["BBP"]] += 1
    # UO
    if indicators[28] != None:
        computed_oscillators["UO"] = Compute.Simple(indicators[28])
        oscillators_counter[computed_oscillators["UO"]] += 1

    # MOVING AVERAGES
    ma_list = ["EMA10","SMA10","EMA20","SMA20","EMA30","SMA30","EMA50","SMA50","EMA100","SMA100","EMA200","SMA200"]
    close = indicators[30]
    ma_list_counter = 0
    for index in range(33, 45):
        if indicators[index] != None:
            computed_ma[ma_list[ma_list_counter]] = Compute.MA(indicators[index], close)
            ma_counter[computed_ma[ma_list[ma_list_counter]]] += 1
            ma_list_counter += 1
        
    # MOVING AVERAGES, pt 2
    # ICHIMOKU
    if indicators[45] != None:
        computed_ma["Ichimoku"] = Compute.Simple(indicators[45])
        ma_counter[computed_ma["Ichimoku"]] += 1
    # VWMA
    if indicators[47] != None:
        computed_ma["VWMA"] = Compute.Simple(indicators[47])
        ma_counter[computed_ma["VWMA"]] += 1
    # HullMA (9)
    if indicators[49] != None:
        computed_ma["HullMA"] = Compute.Simple(indicators[49])
        ma_counter[computed_ma["HullMA"]] += 1

    analysis = Analysis()
    analysis.screener = screener
    analysis.exchange = exchange
    analysis.symbol = symbol
    analysis.interval = interval
    analysis.time = datetime.datetime.now()

    for x in range(len(indicators)):
        analysis.indicators[indicators_key[x]] = indicators[x]

    analysis.indicators = analysis.indicators.copy()

    analysis.oscillators = {"RECOMMENDATION": recommend_oscillators, "BUY": oscillators_counter["BUY"], "SELL": oscillators_counter["SELL"], "NEUTRAL": oscillators_counter["NEUTRAL"], "COMPUTE": computed_oscillators}
    analysis.moving_averages = {"RECOMMENDATION": recommend_moving_averages, "BUY": ma_counter["BUY"], "SELL": ma_counter["SELL"], "NEUTRAL": ma_counter["NEUTRAL"], "COMPUTE": computed_ma}
    analysis.summary = {"RECOMMENDATION": recommend_summary, "BUY": oscillators_counter["BUY"] + ma_counter["BUY"], "SELL": oscillators_counter["SELL"] + ma_counter["SELL"], "NEUTRAL": oscillators_counter["NEUTRAL"] + ma_counter["NEUTRAL"]}

    return analysis

class TA_Handler(object):
    screener = ""
    exchange = ""
    symbol = ""
    interval = ""
    timeout = None

    indicators = TradingView.indicators.copy()

    def __init__(self, screener="", exchange="", symbol="", interval="", timeout=None):
        """Create an instance of TA_Handler class

        Args:
            screener (str, required): Screener (see documentation and tradingview's site).
            exchange (str, required): Exchange (see documentation and tradingview's site).
            symbol (str, required): Abbreviation of a stock or currency (see documentation and tradingview's site).
            interval (str, optional): See the interval class and the documentation. Defaults to 1 day.
            timeout (float, optional): Timeout for requests (in seconds). Defaults to None.
        """
        self.screener = screener
        self.exchange = exchange
        self.symbol = symbol
        self.interval = interval
        self.timeout = timeout

    # Set functions
    def set_screener_as_stock(self, country):
        """Set the screener as a country (for stocks). 

        Args:
            country (string): Stock's country (ex: If NFLX or AAPL, then "america" is the screener)
        """
        self.screener = country

    def set_screener_as_crypto(self):
        """Set the screener as crypto (for cryptocurrencies).
        """
        self.screener = "crypto"

    def set_screener_as_cfd(self):
        """Set the screener as cfd (contract for differences).
        """
        self.screener = "cfd"

    def set_screener_as_forex(self):
        """Set the screener as forex.
        """
        self.screener = "forex"

    def set_exchange_as_crypto_or_stock(self, exchange):
        """Set the exchange

        Args:
            exchange (string): Stock/Crypto's exchange (NASDAQ, NYSE, BINANCE, BITTREX, etc).
        """
        self.exchange = exchange

    def set_exchange_as_forex(self):
        """Set the exchange as FX_IDC for forex.
        """
        self.exchange = "FX_IDC"
    
    def set_exchange_as_cfd(self):
        """Set the exchange as TVC for cfd.
        """
        self.exchange = "TVC"

    def set_interval_as(self, intvl):
        """Set the interval.

        Refer to: https://python-tradingview-ta.readthedocs.io/en/latest/usage.html#setting-the-interval

        Args:
            intvl (string): interval. You can use values from the Interval class. 

        """
        self.interval = intvl

    def set_symbol_as(self, symbol):
        """Set the symbol.

        Refer to: https://python-tradingview-ta.readthedocs.io/en/latest/usage.html#setting-the-symbol

        Args:
            symbol (string): abbreviation of a stock or currency (ex: NFLX, AAPL, BTCUSD).
        """
        self.symbol = symbol

    def get_indicators(self, indicators=[]):
        """Just the indicators, please. See valid indicators on https://pastebin.com/1DjWv2Hd.

        Args:
            indicators (list, optional): List of string of indicators (ex: ["RSI7", "open"]). Defaults to self.indicators.

        Returns:
            dict: A dictionary with a format of {"indicator": value}.
        """
        if len(indicators) == 0:
            indicators = self.indicators

        if self.screener == "" or type(self.screener) != str:
            raise Exception("Screener is empty or not valid.")
        elif self.exchange == "" or type(self.exchange) != str:
            raise Exception("Exchange is empty or not valid.")
        elif self.symbol == "" or type(self.symbol) != str:
            raise Exception("Symbol is empty or not valid.")

        exchange_symbol = f"{self.exchange}:{self.symbol}"
        data = TradingView.data([exchange_symbol], self.interval, indicators)
        scan_url = f"{TradingView.scan_url}{self.screener.lower()}/scan"
        headers = {"User-Agent": "tradingview_ta/{}".format(__version__)}
        response = requests.post(scan_url,json=data, headers=headers, timeout=self.timeout)

        # Return False if can't get data
        if response.status_code != 200:
            raise Exception("Can't access TradingView's API. HTTP status code: {}. Check for invalid symbol, exchange, or indicators.".format(response.status_code))
        
        result = json.loads(response.text)["data"]
        if result != []:
            indicators_val = {}
            for x in range(len(indicators)):
                indicators_val[indicators[x]] = result[0]["d"][x]
            return indicators_val
        else:
            raise Exception("Exchange or symbol not found.")

    # Add custom indicators
    def add_indicators(self, indicators):
        """Add custom indicators. See valid indicators on https://pastebin.com/1DjWv2Hd.

        Args:
            indicators (list): List of strings of indicators. (ex: ["RSI7", "VWMA"])
        """
        self.indicators += indicators

    # Get analysis
    def get_analysis(self):
        """Get analysis from TradingView and compute it.

        Returns:
            Analysis: Contains information about the analysis.
        """

        return calculate(indicators=self.get_indicators(), indicators_key=self.indicators, screener=self.screener, symbol=self.symbol, exchange=self.exchange, interval=self.interval)
        
def get_multiple_analysis(screener, interval, symbols, timeout=None):
    """Retrieve multiple technical analysis at once. Note: You can't mix different screener and interval

    Args:
        screener (str, required): Screener (see documentation and tradingview's site).   
        interval (str, optional): See the interval class and the documentation. Defaults to 1 day.
        symbols (list): List of exchange and ticker symbol separated by a colon. Example: ["NASDAQ:TSLA", "NYSE:DOCN"] or ["BINANCE:BTCUSDT", "BITSTAMP:ETHUSD"].
        timeout (float, optional): Timeout for requests (in seconds). Defaults to None.

    Returns:
        dict: dictionary with a format of {"EXCHANGE:SYMBOL": Analysis}.
    """
    if screener == "" or type(screener) != str:
        raise Exception("Screener is empty or not valid.")
    if len(symbols) == 0 or type(symbols) != list:
        raise Exception("Symbols is empty or not valid.")
    for symbol in symbols:
        if len(symbol.split(":")) != 2 or "" in symbol.split(":"):
            raise Exception("One or more symbol is invalid. Symbol should be a list of exchange and ticker symbol separated by a colon. Example: [\"NASDAQ:TSLA\", \"NYSE:DOCN\"] or [\"BINANCE:BTCUSDT\", \"BITSTAMP:ETHUSD\"].")

    indicators_key = TradingView.indicators.copy()

    data = TradingView.data(symbols, interval, indicators_key)
    scan_url = f"{TradingView.scan_url}{screener.lower()}/scan"
    headers = {"User-Agent": "tradingview_ta/{}".format(__version__)}
    response = requests.post(scan_url,json=data, headers=headers, timeout=timeout)

    result = json.loads(response.text)["data"]
    final = {}

    for analysis in result:
        # Convert list to dict
        indicators = {}
        for x in range(len(analysis["d"])):
            indicators[indicators_key[x]] = analysis["d"][x]
        
        final[analysis["s"]] = calculate(indicators=indicators, indicators_key=indicators_key, screener=screener, symbol=analysis["s"].split(":")[1], exchange=analysis["s"].split(":")[0], interval=interval)

    return final
