# Tradingview Technical Analysis (tradingview-ta)
# Author: deathlyface (https://github.com/deathlyface)
# License: MIT

import requests, json
from technicals import compute, analysis

class tradingview:
    scan_url = "https://scanner.tradingview.com/"
    indicators = ["Recommend.Other|interval","Recommend.All|interval","Recommend.MA|interval","RSI|interval","RSI[1]|interval","Stoch.K|interval","Stoch.D|interval","Stoch.K[1]|interval","Stoch.D[1]|interval","CCI20|interval","CCI20[1]|interval","ADX|interval","ADX+DI|interval","ADX-DI|interval","ADX+DI[1]|interval","ADX-DI[1]|interval","AO|interval","AO[1]|interval","Mom|interval","Mom[1]|interval","MACD.macd|interval","MACD.signal|interval","Rec.Stoch.RSI|interval","Stoch.RSI.K|interval","Rec.WR|interval","W.R|interval","Rec.BBPower|interval","BBPower|interval","Rec.UO|interval","UO|interval","EMA5|interval","close|interval","SMA5|interval","EMA10|interval","SMA10|interval","EMA20|interval","SMA20|interval","EMA30|interval","SMA30|interval","EMA50|interval","SMA50|interval","EMA100|interval","SMA100|interval","EMA200|interval","SMA200|interval","Rec.Ichimoku|interval","Ichimoku.BLine|interval","Rec.VWMA|interval","VWMA|interval","Rec.HullMA9|interval","HullMA9|interval","Pivot.M.Classic.S3|interval","Pivot.M.Classic.S2|interval","Pivot.M.Classic.S1|interval","Pivot.M.Classic.Middle|interval","Pivot.M.Classic.R1|interval","Pivot.M.Classic.R2|interval","Pivot.M.Classic.R3|interval","Pivot.M.Fibonacci.S3|interval","Pivot.M.Fibonacci.S2|interval","Pivot.M.Fibonacci.S1|interval","Pivot.M.Fibonacci.Middle|interval","Pivot.M.Fibonacci.R1|interval","Pivot.M.Fibonacci.R2|interval","Pivot.M.Fibonacci.R3|interval","Pivot.M.Camarilla.S3|interval","Pivot.M.Camarilla.S2|interval","Pivot.M.Camarilla.S1|interval","Pivot.M.Camarilla.Middle|interval","Pivot.M.Camarilla.R1|interval","Pivot.M.Camarilla.R2|interval","Pivot.M.Camarilla.R3|interval","Pivot.M.Woodie.S3|interval","Pivot.M.Woodie.S2|interval","Pivot.M.Woodie.S1|interval","Pivot.M.Woodie.Middle|interval","Pivot.M.Woodie.R1|interval","Pivot.M.Woodie.R2|interval","Pivot.M.Woodie.R3|interval","Pivot.M.Demark.S1|interval","Pivot.M.Demark.Middle|interval","Pivot.M.Demark.R1|interval"]
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
            data_interval = "1M"
        else:
            # Default, 1 Day
            data_interval = ""

        indicators_copy = tradingview.indicators
        for x in range(len(indicators_copy)):
            indicators_copy[x] = indicators_copy[x].replace("|interval", data_interval)
        data_json = {"symbols":{"tickers":[symbol.upper()],"query":{"types":[]}},"columns":indicators_copy}

        return data_json

class TA_Handler:
    screener = "america"
    exchange = "nasdaq"
    symbol = "aapl"
    interval = "1m"
    last_analysis = {}

    #Get analysis
    def get_analysis(self):
        ticker = self.exchange.upper() + ":" + self.symbol.upper()
        data = tradingview.data(ticker, self.interval)
        scan_url = tradingview.scan_url + self.screener + "/scan"
        response = requests.post(scan_url, json=data)

        # Return False if can't get data
        if response.status_code != 200:
            return False
        
        result = json.loads(response.text)["data"][0]
        indicator_values = result["d"]

        oscillators_counter = {"BUY": 0, "SELL": 0, "NEUTRAL": 0}
        computed_oscillators = {}

        # OSCILLATORS
        # RSI (14)
        if None not in indicator_values[3:5]:
            computed_oscillators["RSI"] = compute.RSI(indicator_values[3], indicator_values[4])
            oscillators_counter[computed_oscillators["RSI"]] += 1

        # Stoch %K
        if None not in indicator_values[5:9]:
            computed_oscillators["STOCH.K"] = compute.Stoch(indicator_values[5], indicator_values[6], indicator_values[7], indicator_values[8])
            oscillators_counter[computed_oscillators["STOCH.K"]] += 1
        # CCI (20)
        if None not in indicator_values[9:11]:
            computed_oscillators["CCI"] = compute.CCI20(indicator_values[9], indicator_values[10])
            oscillators_counter[computed_oscillators["CCI"]] += 1
        # ADX (14)
        if None not in indicator_values[11:16]:
            computed_oscillators["ADX"] = compute.ADX(indicator_values[11], indicator_values[12], indicator_values[13], indicator_values[14], indicator_values[15])
            oscillators_counter[computed_oscillators["ADX"]] += 1
        # AO
        if None not in indicator_values[16:18]:
            computed_oscillators["AO"] = compute.AO(indicator_values[16], indicator_values[17])
            oscillators_counter[computed_oscillators["AO"]] += 1
        # Mom (10)
        if None not in indicator_values[18:20]:
            computed_oscillators["Mom"] = compute.Mom(indicator_values[18], indicator_values[19])
            oscillators_counter[computed_oscillators["Mom"]] += 1
        # MACD
        if None not in indicator_values[20:22]:
            computed_oscillators["MACD"] = compute.MACD(indicator_values[20], indicator_values[21])
            oscillators_counter[computed_oscillators["MACD"]] += 1
        # Stoch RSI
        if indicator_values[23] != None:
            computed_oscillators["Stoch.RSI"] = compute.Simple(indicator_values[23])
            oscillators_counter[computed_oscillators["Stoch.RSI"]] += 1
        # W%R
        if indicator_values[25] != None:
            computed_oscillators["W%R"] = compute.Simple(indicator_values[25])
            oscillators_counter[computed_oscillators["W%R"]] += 1
        # BBP
        if indicator_values[27] != None:
            computed_oscillators["BBP"] = compute.Simple(indicator_values[27])
            oscillators_counter[computed_oscillators["BBP"]] += 1
        # UO
        if indicator_values[29] != None:
            computed_oscillators["UO"] = compute.Simple(indicator_values[29])
            oscillators_counter[computed_oscillators["UO"]] += 1

        # TODO: Summary and MA

        analysis = {"oscillators_counter": oscillators_counter, "oscillators_analysis": computed_oscillators}
        
        self.last_analysis = analysis
        return analysis