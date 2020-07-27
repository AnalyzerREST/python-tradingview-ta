class analysis:
    buy = "BUY"
    strong_buy = "STRONG_BUY"
    sell = "SELL"
    strong_sell = "STRONG_SELL"
    neutral = "NEUTRAL"
    error = "ERROR"

class compute:
    def MA(ma, close):
        """Compute Moving Average

        Args:
            ma (float): MA value
            close (float): Close value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (ma < close):
            return analysis.buy
        elif (ma > close):
            return analysis.sell
        else:
            return analysis.neutral

    def RSI(rsi, rsi1):
        """Compute Relative Strength Index

        Args:
            rsi (float): RSI value
            rsi1 (float): RSI[1] value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (rsi < 30 and rsi1 > rsi):
            return analysis.buy
        elif (rsi > 70 and rsi1 < rsi):
            return analysis.sell
        else:
            return analysis.neutral

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
            return analysis.buy
        elif (k > 80 and d > 80 and k < d and k1 > d1):
            return analysis.sell
        else:
            return analysis.neutral

    def CCI20(cci20, cci201):
        """Compute Commodity Channel Index 20

        Args:
            cci20 (float): CCI20 value
            cci201 ([type]): CCI20[1] value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (cci20 < -100 and cci20 > cci201):
            return analysis.buy
        elif (cci20 > 100 and cci20 < cci201):
            return analysis.sell
        else:
            return analysis.neutral

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
            return analysis.buy
        elif (adx > 20 and adxpdi1 > adxndi1 and adxpdi < adxndi):
            return analysis.sell
        else:
            return analysis.neutral

    def AO(ao, ao1):
        """Compute Awesome Oscillator

        Args:
            ao (float): AO value
            ao1 (float): AO[1] value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (ao > 0 and ao1 < 0 or ao > 0 and ao1 > 0 and ao > ao1):
            return analysis.buy
        elif (ao < 0 and ao1 > 0 or ao < 0 and ao1 < 0 and ao < ao1):
            return analysis.sell
        else:
            return analysis.neutral

    def Mom(mom, mom1):
        """Compute Momentum

        Args:
            mom (float): Mom value
            mom1 (float): Mom[1] value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (mom > mom1):
            return analysis.buy
        elif (mom < mom1):
            return analysis.sell
        else:
            return analysis.neutral

    def MACD(macd, signal):
        """Compute Moving Average Convergence/Divergence

        Args:
            macd (float): MACD.macd value
            signal (float): MACD.signal value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (macd > signal):
            return analysis.buy
        elif (macd < signal):
            return analysis.sell
        else:
            return analysis.neutral
        
    def BBBuy(close, bblower):
        """Compute Bull Bear Buy

        Args:
            close (float): close value
            bblower (float): BB.lower value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (close < bblower):
            return analysis.buy
        else:
            return analysis.neutral

    def BBSell(close, bbupper):
        """Compute Bull Bear Sell

        Args:
            close (float): close value
            bbupper (float): BB.upper value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (close > bbupper):
            return analysis.sell
        else:
            return analysis.neutral

    def PSAR(psar, open):
        """Compute Parabolic Stop-And-Reverse

        Args:
            psar (float): P.SAR value
            open (float): open value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (psar < open):
            return analysis.buy
        elif (psar > open):
            return analysis.sell
        else:
            return analysis.neutral

    def Recommend(value):
        """Compute Recommend

        Args:
            value (float): recommend value

        Returns:
            string: "STRONG_BUY", "BUY", "NEUTRAL", "SELL", "STRONG_SELL", or "ERROR"
        """
        if (value >= -1 and value < -.5):
            return analysis.strong_sell
        elif (value >= -.5 and value < 0):
            return analysis.sell
        elif (value == 0):
            return analysis.neutral
        elif (value > 0 and e <= .5):
            return analysis.buy
        elif (value > .5 and e <= 1):
            return analysis.strong_buy
        else:
            return analysis.error

    def Simple(value):
        """Compute Simple

        Args:
            value (float): Rec.X value

        Returns:
            string: "BUY", "SELL", or "NEUTRAL"
        """
        if (value == -1):
            return analysis.sell
        elif (value == 1):
            return analysis.buy
        else:
            return analysis.neutral
