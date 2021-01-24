# How it Works
This is not really important, but I'll explain how python-tradingview-ta gets the data and calculate the result.

## TradingView API
TradingView does not have any API, but a simple network scan with Chrome DevTools gives us this URL:
`https://scanner.tradingview.com/{screener}/scan`

And this POST data:
```
{"symbols":{"tickers":["{exchange}:{symbol}"],"query":{"types":[]}},"columns":["Recommend.Other","Recommend.All","Recommend.MA","RSI","RSI[1]","Stoch.K","Stoch.D","Stoch.K[1]","Stoch.D[1]","CCI20","CCI20[1]","ADX","ADX DI","ADX-DI","ADX DI[1]","ADX-DI[1]","AO","AO[1]","Mom","Mom[1]","MACD.macd","MACD.signal","Rec.Stoch.RSI","Stoch.RSI.K","Rec.WR","W.R","Rec.BBPower","BBPower","Rec.UO","UO","EMA5","close","SMA5","EMA10","SMA10","EMA20","SMA20","EMA30","SMA30","EMA50","SMA50","EMA100","SMA100","EMA200","SMA200","Rec.Ichimoku","Ichimoku.BLine","Rec.VWMA","VWMA","Rec.HullMA9","HullMA9","Pivot.M.Classic.S3","Pivot.M.Classic.S2","Pivot.M.Classic.S1","Pivot.M.Classic.Middle","Pivot.M.Classic.R1","Pivot.M.Classic.R2","Pivot.M.Classic.R3","Pivot.M.Fibonacci.S3","Pivot.M.Fibonacci.S2","Pivot.M.Fibonacci.S1","Pivot.M.Fibonacci.Middle","Pivot.M.Fibonacci.R1","Pivot.M.Fibonacci.R2","Pivot.M.Fibonacci.R3","Pivot.M.Camarilla.S3","Pivot.M.Camarilla.S2","Pivot.M.Camarilla.S1","Pivot.M.Camarilla.Middle","Pivot.M.Camarilla.R1","Pivot.M.Camarilla.R2","Pivot.M.Camarilla.R3","Pivot.M.Woodie.S3","Pivot.M.Woodie.S2","Pivot.M.Woodie.S1","Pivot.M.Woodie.Middle","Pivot.M.Woodie.R1","Pivot.M.Woodie.R2","Pivot.M.Woodie.R3","Pivot.M.Demark.S1","Pivot.M.Demark.Middle","Pivot.M.Demark.R1"]}
```
With a POST request to the URL, we can get this data:
```
{ "data":[{"s":"{exchange}:{symbol}","d":[-0.09090909,0.35454545,0.8,80.27059115,79.07576602,83.44041942,83.35010861,80.91202126,83.44706663,209.05076363,254.06777994,31.86385829,40.48322556,6.09244774,42.46627828,6.39088358,1036.47123529,808.25082353,1866.26,1761.84,375.60208608,171.78770341,0,94.65879142,0,-14.17468418,0,1829.63096398,0,67.33299272,10629.43224966,11078.25,10543.868,10208.458897,9997.764,9832.94151772,9607.9595,9672.04948813,9472.477,9493.86102459,9432.9932,9162.84942884,9236.6133,8810.53750529,8654.4865,0,10161.055,1,10030.86817126,-1,11205.12311111,6267.02333333,7865.65333333,8499.30666667,9464.28333333,10097.93666667,11062.91333333,12661.54333333,7865.65333333,8476.32999333,8853.60667333,9464.28333333,10074.95999333,10452.23667333,11062.91333333,8693.33675,8839.87783339,8986.41891661,9464.28333333,9279.50108339,9426.04216661,9572.58325,6738.945,7784.7875,8337.575,9383.4175,9936.205,10982.0475,11534.835,8182.48,9305.87,9781.11]}],"totalCount":1}
```

## Calculation
Determining whether to buy or sell is a hard decision. I am not a professional trader and don't even know about technical analysis. So, how does it compute whether to buy/sell?

I reverse engineered TradingView's [JS code](https://gist.github.com/deathlyface/f0bb91658c1f161cafe8990db1473bd6), which looks like this:
```javascript
signalComputationFunctions = {
    computeMASignal: function(e, t) {
        var o = n.NEUTRAL;
        return e < t && (o = n.BUY), e > t && (o = n.SELL), o
    },
    computeRSISignal: function(e, t) {
        var o = n.NEUTRAL;
        return e < 30 && t > e && (o = n.BUY), e > 70 && t < e && (o = n.SELL), o
    },
    computeStochSignal: function(e, t, o, r) {
        var i = n.NEUTRAL;
        return e < 20 && t < 20 && e > t && o < r && (i = n.BUY), e > 80 && t > 80 && e < t && o > r && (i = n.SELL), i
    },
    computeCCI20Signal: function(e, t) {
        var o = n.NEUTRAL;
        return e < -100 && e > t && (o = n.BUY), e > 100 && e < t && (o = n.SELL), o
    },
    computeADXSignal: function(e, t, o, r, i) {
        var a = n.NEUTRAL;
        return e > 20 && r < i && t > o && (a = n.BUY), e > 20 && r > i && t < o && (a = n.SELL), a
    },
    computeAOSignal: function(e, t) {
        var o = n.NEUTRAL;
        return (e > 0 && t < 0 || e > 0 && t > 0 && e > t) && (o = n.BUY), (e < 0 && t > 0 || e < 0 && t < 0 && e < t) && (o = n.SELL), o
    },
    computeMomSignal: function(e, t) {
        var o = n.NEUTRAL;
        return e < t && (o = n.BUY), e > t && (o = n.SELL), o
    },
    computeMACDSignal: function(e, t) {
        var o = n.NEUTRAL;
        return e > t && (o = n.BUY), e < t && (o = n.SELL), o
    },
    computeBBBuySignal: function(e, t) {
        var o = n.NEUTRAL;
        return e < t && (o = n.BUY), o
    },
    computeBBSellSignal: function(e, t) {
        var o = n.NEUTRAL;
        return e > t && (o = n.SELL), o
    },
    computePSARSignal: function(e, t) {
        var o = n.NEUTRAL;
        return e < t && (o = n.BUY), e > t && (o = n.SELL), o
    },
    computeRecommendSignal: function(e) {
        var t = void 0;
        return e >= -1 && e < -.5 && (t = n.STRONG_SELL), e >= -.5 && e < 0 && (t = n.SELL), 0 === e && (t = n.NEUTRAL), e > 0 && e <= .5 && (t = n.BUY), e > .5 && e <= 1 && (t = n.STRONG_BUY), t
    },
    computeSimpleSignal: function(e) {
        var t = n.NEUTRAL;
        return -1 === e && (t = n.SELL), 1 === e && (t = n.BUY), t
    }
}
```
I rewrote it using python and that's how the `technicals.py` module is created.

```python
# Tradingview Technical Analysis (tradingview-ta)
# Author: deathlyface (https://github.com/deathlyface)
# Rewritten from https://www.tradingview.com/static/bundles/technicals.f2e6e6a51aebb6cd46f8.js
# License: MIT

class Recommendation:
    buy = "BUY"
    strong_buy = "STRONG_BUY"
    sell = "SELL"
    strong_sell = "STRONG_SELL"
    neutral = "NEUTRAL"
    error = "ERROR"

class Compute:
    def MA(ma, close):
        """Compute Moving Average

        Args:
            ma (float): MA value
            close (float): Close value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (ma < close):
            return Recommendation.buy
        elif (ma > close):
            return Recommendation.sell
        else:
            return Recommendation.neutral

    def RSI(rsi, rsi1):
        """Compute Relative Strength Index

        Args:
            rsi (float): RSI value
            rsi1 (float): RSI[1] value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (rsi < 30 and rsi1 > rsi):
            return Recommendation.buy
        elif (rsi > 70 and rsi1 < rsi):
            return Recommendation.sell
        else:
            return Recommendation.neutral

    def Stoch(k, d, k1, d1):
        """Compute Stochastic

        Args:
            k (float): Stoch.K value
            d (float): Stoch.D value
            k1 (float): Stoch.K[1] value
            d1 (float): Stoch.D[1] value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (k < 20 and d < 20 and k > d and k1 < d1):
            return Recommendation.buy
        elif (k > 80 and d > 80 and k < d and k1 > d1):
            return Recommendation.sell
        else:
            return Recommendation.neutral

    def CCI20(cci20, cci201):
        """Compute Commodity Channel Index 20

        Args:
            cci20 (float): CCI20 value
            cci201 ([type]): CCI20[1] value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (cci20 < -100 and cci20 > cci201):
            return Recommendation.buy
        elif (cci20 > 100 and cci20 < cci201):
            return Recommendation.sell
        else:
            return Recommendation.neutral

    def ADX(adx, adxpdi, adxndi, adxpdi1, adxndi1):
        """Compute Average Directional Index

        Args:
            adx (float): ADX value
            adxpdi (float): ADX+DI value
            adxndi (float): ADX-DI value
            adxpdi1 (float): ADX+DI[1] value
            adxndi1 (float): ADX-DI[1] value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (adx > 20 and adxpdi1 < adxndi1 and adxpdi > adxndi):
            return Recommendation.buy
        elif (adx > 20 and adxpdi1 > adxndi1 and adxpdi < adxndi):
            return Recommendation.sell
        else:
            return Recommendation.neutral

    def AO(ao, ao1):
        """Compute Awesome Oscillator

        Args:
            ao (float): AO value
            ao1 (float): AO[1] value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (ao > 0 and ao1 < 0 or ao > 0 and ao1 > 0 and ao > ao1):
            return Recommendation.buy
        elif (ao < 0 and ao1 > 0 or ao < 0 and ao1 < 0 and ao < ao1):
            return Recommendation.sell
        else:
            return Recommendation.neutral

    def Mom(mom, mom1):
        """Compute Momentum

        Args:
            mom (float): Mom value
            mom1 (float): Mom[1] value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (mom < mom1):
            return Recommendation.buy
        elif (mom > mom1):
            return Recommendation.sell
        else:
            return Recommendation.neutral

    def MACD(macd, signal):
        """Compute Moving Average Convergence/Divergence

        Args:
            macd (float): MACD.macd value
            signal (float): MACD.signal value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (macd > signal):
            return Recommendation.buy
        elif (macd < signal):
            return Recommendation.sell
        else:
            return Recommendation.neutral
        
    def BBBuy(close, bblower):
        """Compute Bull Bear Buy

        Args:
            close (float): close value
            bblower (float): BB.lower value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (close < bblower):
            return Recommendation.buy
        else:
            return Recommendation.neutral

    def BBSell(close, bbupper):
        """Compute Bull Bear Sell

        Args:
            close (float): close value
            bbupper (float): BB.upper value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (close > bbupper):
            return Recommendation.sell
        else:
            return Recommendation.neutral

    def PSAR(psar, open):
        """Compute Parabolic Stop-And-Reverse

        Args:
            psar (float): P.SAR value
            open (float): open value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (psar < open):
            return Recommendation.buy
        elif (psar > open):
            return Recommendation.sell
        else:
            return Recommendation.neutral

    def Recommend(value):
        """Compute Recommend

        Args:
            value (float): recommend value

        Returns:
            string: "STRONG_BUY", "BUY", "NEUTRAL", "SELL", "STRONG_SELL", or "ERROR"
        """
        if (value >= -1 and value < -.5):
            return Recommendation.strong_sell
        elif (value >= -.5 and value < 0):
            return Recommendation.sell
        elif (value == 0):
            return Recommendation.neutral
        elif (value > 0 and value <= .5):
            return Recommendation.buy
        elif (value > .5 and value <= 1):
            return Recommendation.strong_buy
        else:
            return Recommendation.error

    def Simple(value):
        """Compute Simple

        Args:
            value (float): Rec.X value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (value == -1):
            return Recommendation.sell
        elif (value == 1):
            return Recommendation.buy
        else:
            return Recommendation.neutral

```

The rest is simple. Compute the data.
