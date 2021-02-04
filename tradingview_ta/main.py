# Tradingview Technical Analysis (tradingview-ta)
# Author: deathlyface (https://github.com/deathlyface)
# License: MIT

import requests, json, datetime, warnings
from .technicals import Compute

__version__ = "3.2.2"

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
    scan_url = "https://scanner.tradingview.com/"
    indicators = ["Recommend.Other{}","Recommend.All{}","Recommend.MA{}","RSI{}","RSI[1]{}","Stoch.K{}","Stoch.D{}","Stoch.K[1]{}","Stoch.D[1]{}","CCI20{}","CCI20[1]{}","ADX{}","ADX+DI{}","ADX-DI{}","ADX+DI[1]{}","ADX-DI[1]{}","AO{}","AO[1]{}","Mom{}","Mom[1]{}","MACD.macd{}","MACD.signal{}","Rec.Stoch.RSI{}","Stoch.RSI.K{}","Rec.WR{}","W.R{}","Rec.BBPower{}","BBPower{}","Rec.UO{}","UO{}","close{}","EMA5{}","SMA5{}","EMA10{}","SMA10{}","EMA20{}","SMA20{}","EMA30{}","SMA30{}","EMA50{}","SMA50{}","EMA100{}","SMA100{}","EMA200{}","SMA200{}","Rec.Ichimoku{}","Ichimoku.BLine{}","Rec.VWMA{}","VWMA{}","Rec.HullMA9{}","HullMA9{}","Pivot.M.Classic.S3{}","Pivot.M.Classic.S2{}","Pivot.M.Classic.S1{}","Pivot.M.Classic.Middle{}","Pivot.M.Classic.R1{}","Pivot.M.Classic.R2{}","Pivot.M.Classic.R3{}","Pivot.M.Fibonacci.S3{}","Pivot.M.Fibonacci.S2{}","Pivot.M.Fibonacci.S1{}","Pivot.M.Fibonacci.Middle{}","Pivot.M.Fibonacci.R1{}","Pivot.M.Fibonacci.R2{}","Pivot.M.Fibonacci.R3{}","Pivot.M.Camarilla.S3{}","Pivot.M.Camarilla.S2{}","Pivot.M.Camarilla.S1{}","Pivot.M.Camarilla.Middle{}","Pivot.M.Camarilla.R1{}","Pivot.M.Camarilla.R2{}","Pivot.M.Camarilla.R3{}","Pivot.M.Woodie.S3{}","Pivot.M.Woodie.S2{}","Pivot.M.Woodie.S1{}","Pivot.M.Woodie.Middle{}","Pivot.M.Woodie.R1{}","Pivot.M.Woodie.R2{}","Pivot.M.Woodie.R3{}","Pivot.M.Demark.S1{}","Pivot.M.Demark.Middle{}","Pivot.M.Demark.R1{}", "open{}", "P.SAR{}"]
    def data(symbol, interval):
        """Format TradingView's Scanner Post Data

        Args:
            symbol (string): EXCHANGE:SYMBOL (ex: NASDAQ:AAPL or BINANCE:BTCUSDT)
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
            
        data_json = {"symbols":{"tickers":[symbol.upper()],"query":{"types":[]}},"columns":[x.format(data_interval) for x in TradingView.indicators]}

        return data_json

class TA_Handler(object):
    screener = ""
    exchange = ""
    symbol = ""
    interval = ""

    def __init__(self, screener="", exchange="", symbol="", interval=""):
        self.screener = screener
        self.exchange = exchange
        self.symbol = symbol
        self.interval = interval

    #Set functions
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
        

    #Get analysis
    def get_analysis(self):
        """Get analysis from TradingView and compute it.

        Returns:
            Analysis: Contains information about the analysis.
        """
        if self.screener == "" or type(self.screener) != str:
            raise Exception("Screener is empty or not valid.")
        elif self.exchange == "" or type(self.exchange) != str:
            raise Exception("Exchange is empty or not valid.")
        elif self.symbol == "" or type(self.symbol) != str:
            raise Exception("Symbol is empty or not valid.")

        exch_smbl = self.exchange.upper() + ":" + self.symbol.upper()
        data = TradingView.data(exch_smbl, self.interval)
        scan_url = TradingView.scan_url + self.screener.lower() + "/scan"
        headers = {"User-Agent": "tradingview_ta/{}".format(__version__)}
        response = requests.post(scan_url, json=data, headers=headers)

        # Return False if can't get data
        if response.status_code != 200:
            raise Exception("Can't access TradingView's API. HTTP status code: {}.".format(response.status_code))
        
        result = json.loads(response.text)["data"]
        if result != []:
            indicator_values = result[0]["d"]
        else:
            raise Exception("Exchange or symbol not found.")


        oscillators_counter, ma_counter = {"BUY": 0, "SELL": 0, "NEUTRAL": 0}, {"BUY": 0, "SELL": 0, "NEUTRAL": 0}
        computed_oscillators, computed_ma = {}, {}

        # RECOMMENDATIONS
        recommend_oscillators = Compute.Recommend(indicator_values[0])
        recommend_summary = Compute.Recommend(indicator_values[1])
        recommend_moving_averages = Compute.Recommend(indicator_values[2])

        # OSCILLATORS
        # RSI (14)
        if None not in indicator_values[3:5]:
            computed_oscillators["RSI"] = Compute.RSI(indicator_values[3], indicator_values[4])
            oscillators_counter[computed_oscillators["RSI"]] += 1
        # Stoch %K
        if None not in indicator_values[5:9]:
            computed_oscillators["STOCH.K"] = Compute.Stoch(indicator_values[5], indicator_values[6], indicator_values[7], indicator_values[8])
            oscillators_counter[computed_oscillators["STOCH.K"]] += 1
        # CCI (20)
        if None not in indicator_values[9:11]:
            computed_oscillators["CCI"] = Compute.CCI20(indicator_values[9], indicator_values[10])
            oscillators_counter[computed_oscillators["CCI"]] += 1
        # ADX (14)
        if None not in indicator_values[11:16]:
            computed_oscillators["ADX"] = Compute.ADX(indicator_values[11], indicator_values[12], indicator_values[13], indicator_values[14], indicator_values[15])
            oscillators_counter[computed_oscillators["ADX"]] += 1
        # AO
        if None not in indicator_values[16:18]:
            computed_oscillators["AO"] = Compute.AO(indicator_values[16], indicator_values[17])
            oscillators_counter[computed_oscillators["AO"]] += 1
        # Mom (10)
        if None not in indicator_values[18:20]:
            computed_oscillators["Mom"] = Compute.Mom(indicator_values[18], indicator_values[19])
            oscillators_counter[computed_oscillators["Mom"]] += 1
        # MACD
        if None not in indicator_values[20:22]:
            computed_oscillators["MACD"] = Compute.MACD(indicator_values[20], indicator_values[21])
            oscillators_counter[computed_oscillators["MACD"]] += 1
        # Stoch RSI
        if indicator_values[22] != None:
            computed_oscillators["Stoch.RSI"] = Compute.Simple(indicator_values[22])
            oscillators_counter[computed_oscillators["Stoch.RSI"]] += 1
        # W%R
        if indicator_values[24] != None:
            computed_oscillators["W%R"] = Compute.Simple(indicator_values[24])
            oscillators_counter[computed_oscillators["W%R"]] += 1
        # BBP
        if indicator_values[26] != None:
            computed_oscillators["BBP"] = Compute.Simple(indicator_values[26])
            oscillators_counter[computed_oscillators["BBP"]] += 1
        # UO
        if indicator_values[28] != None:
            computed_oscillators["UO"] = Compute.Simple(indicator_values[28])
            oscillators_counter[computed_oscillators["UO"]] += 1

        # MOVING AVERAGES
        ma_list = ["EMA10","SMA10","EMA20","SMA20","EMA30","SMA30","EMA50","SMA50","EMA100","SMA100","EMA200","SMA200"]
        close = indicator_values[30]
        ma_list_counter = 0
        for index in range(33, 45):
            if indicator_values[index] != None:
                computed_ma[ma_list[ma_list_counter]] = Compute.MA(indicator_values[index], close)
                ma_counter[computed_ma[ma_list[ma_list_counter]]] += 1
                ma_list_counter += 1
            
        # MOVING AVERAGES, pt 2
        # ICHIMOKU
        if indicator_values[45] != None:
            computed_ma["Ichimoku"] = Compute.Simple(indicator_values[45])
            ma_counter[computed_ma["Ichimoku"]] += 1
        # VWMA
        if indicator_values[47] != None:
            computed_ma["VWMA"] = Compute.Simple(indicator_values[47])
            ma_counter[computed_ma["VWMA"]] += 1
        # HullMA (9)
        if indicator_values[49] != None:
            computed_ma["HullMA"] = Compute.Simple(indicator_values[49])
            ma_counter[computed_ma["HullMA"]] += 1

        analysis = Analysis()
        analysis.screener = self.screener
        analysis.exchange = self.exchange
        analysis.symbol = self.symbol
        analysis.interval = self.interval
        analysis.time = datetime.datetime.now()

        for x in range(len(indicator_values)):
            analysis.indicators[TradingView.indicators[x].format("")] = indicator_values[x]

        analysis.oscillators = {"RECOMMENDATION": recommend_oscillators, "BUY": oscillators_counter["BUY"], "SELL": oscillators_counter["SELL"], "NEUTRAL": oscillators_counter["NEUTRAL"], "COMPUTE": computed_oscillators}
        analysis.moving_averages = {"RECOMMENDATION": recommend_moving_averages, "BUY": ma_counter["BUY"], "SELL": ma_counter["SELL"], "NEUTRAL": ma_counter["NEUTRAL"], "COMPUTE": computed_ma}
        analysis.summary = {"RECOMMENDATION": recommend_summary, "BUY": oscillators_counter["BUY"] + ma_counter["BUY"], "SELL": oscillators_counter["SELL"] + ma_counter["SELL"], "NEUTRAL": oscillators_counter["NEUTRAL"] + ma_counter["NEUTRAL"]}

        return analysis
        
