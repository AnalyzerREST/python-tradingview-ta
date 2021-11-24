Usage
=====

.. note:: Please install or update TradingView_TA to the latest version. Please read the `getting started <overview.rst>`_ guide before continuing.

.. warning:: TradingView_TA older than v3.2.0 is no longer supported. Please update using ``pip install tradingview_ta --upgrade``.

Importing TradingView_TA
------------------------

.. code-block:: python3

    from tradingview_ta import TA_Handler, Interval, Exchange
    import tradingview_ta


Checking the version
--------------------

Starting from version 3.1.3, you can retrieve the version of TradingView_TA through the ``__version__`` attribute.

.. code-block:: python3

    print(tradingview_ta.__version__)
    # Example output: 3.1.3

Instantiating TA_Handler
------------------------

.. code-block:: python3

    handler = TA_Handler(
        symbol="",
        exchange="",
        screener="",
        interval="",
        timeout=None
    )

Parameters: 

    .. tip::

        You can search on https://tvdb.brianthe.dev to see which symbol, exchange, and screener to use.

        .. image:: https://raw.githubusercontent.com/brian-the-dev/python-tradingview-ta/main/images/tv-list.png

    * symbol (``str``) – Ticker symbol (e.g., ``"AAPL"``, ``"TLKM"``, ``"USDEUR"``, ``"BTCUSDT"``).
    * exchange (``str``) – Exchange (e.g., ``"nasdaq"``, ``"idx"``, ``Exchange.FOREX``, ``"binance"``).
    * screener (``str``) – Screener (e.g., ``"america"``, ``"indonesia"``, ``"forex"``, ``"crypto"``).

        .. note::

            * If you're looking for stocks, enter the exchange's country as the screener.
            * If you're looking for cryptocurrency, enter ``"crypto"`` as the screener.
            * If you're looking for forex, enter ``"forex"`` as the screener.

    * interval (``str``) – Time frame

        .. note::

            Please see the Interval class for available intervals.

            .. code-block:: python3

                class Interval:
                    INTERVAL_1_MINUTE = "1m"
                    INTERVAL_5_MINUTES = "5m"
                    INTERVAL_15_MINUTES = "15m"
                    INTERVAL_30_MINUTES = "30m"
                    INTERVAL_1_HOUR = "1h"
                    INTERVAL_2_HOURS = "2h"
                    INTERVAL_4_HOURS = "4h"
                    INTERVAL_1_DAY = "1d"
                    INTERVAL_1_WEEK = "1W"
                    INTERVAL_1_MONTH = "1M"

    * timeout (``float``, optional) – How long to wait (in seconds) for the server to return a response.

Retrieving the analysis
-----------------------

.. code-block:: python3

    analysis = handler.get_analysis()

.. note::

    ``analysis`` is an instance of Analysis class. 
    It contains information such as the exchange, symbol, screener, interval, local time (datetime.datetime), etc.

Attributes:

    * symbol (``str``) – The symbol set earlier.
    * exchange (``str``) – The exchange set earlier.
    * screener (``str``) – The screener set earlier.
    * interval (``str``) – The interval set earlier.
    * time (``datetime.datetime``) – The time when the data is retrieved.
    * summary (``dict``) – Technical analysis (based on both oscillators and moving averages).

        .. code-block:: python3

            # Example
            {'RECOMMENDATION': 'BUY', 'BUY': 12, 'SELL': 7, 'NEUTRAL': 9}

    * oscillators (``dict``) – Technical analysis (based on oscillators).

        .. code-block:: python3

            # Example
            {'RECOMMENDATION': 'BUY', 'BUY': 2, 'SELL': 1, 'NEUTRAL': 8, 'COMPUTE': {'RSI': 'NEUTRAL', 'STOCH.K': 'NEUTRAL', 'CCI': 'NEUTRAL', 'ADX': 'NEUTRAL', 'AO': 'NEUTRAL', 'Mom': 'BUY', 'MACD': 'SELL', 'Stoch.RSI': 'NEUTRAL', 'W%R': 'NEUTRAL', 'BBP': 'BUY', 'UO': 'NEUTRAL'}}

    * moving_averages (``dict``) – Technical analysis (based on moving averages).

        .. code-block:: python3

            # Example
            {'RECOMMENDATION': 'BUY', 'BUY': 9, 'SELL': 5, 'NEUTRAL': 1, 'COMPUTE': {'EMA10': 'SELL', 'SMA10': 'SELL', 'EMA20': 'SELL', 'SMA20': 'SELL', 'EMA30': 'BUY', 'SMA30': 'BUY', 'EMA50': 'BUY', 'SMA50': 'BUY', 'EMA100': 'BUY', 'SMA100': 'BUY', 'EMA200': 'BUY', 'SMA200': 'BUY', 'Ichimoku': 'NEUTRAL', 'VWMA': 'SELL', 'HullMA': 'BUY'}}

    * indicators (``dict``) – Technical indicators.

        .. code-block:: python3

            # Example
            {'Recommend.Other': 0, 'Recommend.All': 0.26666667, 'Recommend.MA': 0.53333333, 'RSI': 60.28037412, 'RSI[1]': 58.58364778, 'Stoch.K': 73.80404453, 'Stoch.D': 79.64297643, 'Stoch.K[1]': 78.88160227, 'Stoch.D[1]': 85.97647064, 'CCI20': 46.58442886, 'CCI20[1]': 34.57058796, 'ADX': 35.78754863, 'ADX+DI': 23.16948389, 'ADX-DI': 13.82449817, 'ADX+DI[1]': 24.15991909, 'ADX-DI[1]': 13.87125505, 'AO': 6675.72158824, 'AO[1]': 7283.92420588, 'Mom': 1532.6, 'Mom[1]': 108.29, 'MACD.macd': 2444.73734978, 'MACD.signal': 2606.00138275, 'Rec.Stoch.RSI': 0, 'Stoch.RSI.K': 18.53740187, 'Rec.WR': 0, 'W.R': -26.05634845, 'Rec.BBPower': 0, 'BBPower': 295.52055898, 'Rec.UO': 0, 'UO': 55.68311917, 'close': 45326.97, 'EMA5': 45600.06414333, 'SMA5': 45995.592, 'EMA10': 45223.22433151, 'SMA10': 45952.635, 'EMA20': 43451.52018338, 'SMA20': 43609.214, 'EMA30': 41908.5944052, 'SMA30': 40880.391, 'EMA50': 40352.10222373, 'SMA50': 37819.3566, 'EMA100': 40356.09177879, 'SMA100': 38009.7808, 'EMA200': 39466.50411569, 'SMA200': 45551.36135, 'Rec.Ichimoku': 0, 'Ichimoku.BLine': 40772.57, 'Rec.VWMA': 1, 'VWMA': 43471.81729377, 'Rec.HullMA9': -1, 'HullMA9': 45470.37107407, 'Pivot.M.Classic.S3': 11389.27666667, 'Pivot.M.Classic.S2': 24559.27666667, 'Pivot.M.Classic.S1': 33010.55333333, 'Pivot.M.Classic.Middle': 37729.27666667, 'Pivot.M.Classic.R1': 46180.55333333, 'Pivot.M.Classic.R2': 50899.27666667, 'Pivot.M.Classic.R3': 64069.27666667, 'Pivot.M.Fibonacci.S3': 24559.27666667, 'Pivot.M.Fibonacci.S2': 29590.21666667, 'Pivot.M.Fibonacci.S1': 32698.33666667, 'Pivot.M.Fibonacci.Middle': 37729.27666667, 'Pivot.M.Fibonacci.R1': 42760.21666667, 'Pivot.M.Fibonacci.R2': 45868.33666667, 'Pivot.M.Fibonacci.R3': 50899.27666667, 'Pivot.M.Camarilla.S3': 37840.08, 'Pivot.M.Camarilla.S2': 39047.33, 'Pivot.M.Camarilla.S1': 40254.58, 'Pivot.M.Camarilla.Middle': 37729.27666667, 'Pivot.M.Camarilla.R1': 42669.08, 'Pivot.M.Camarilla.R2': 43876.33, 'Pivot.M.Camarilla.R3': 45083.58, 'Pivot.M.Woodie.S3': 21706.84, 'Pivot.M.Woodie.S2': 25492.42, 'Pivot.M.Woodie.S1': 34876.84, 'Pivot.M.Woodie.Middle': 38662.42, 'Pivot.M.Woodie.R1': 48046.84, 'Pivot.M.Woodie.R2': 51832.42, 'Pivot.M.Woodie.R3': 61216.84, 'Pivot.M.Demark.S1': 35369.915, 'Pivot.M.Demark.Middle': 38908.9575, 'Pivot.M.Demark.R1': 48539.915, 'open': 44695.95, 'P.SAR': 48068.64, 'BB.lower': 37961.23510877, 'BB.upper': 49257.19289123, 'AO[2]': 7524.31223529, 'volume': 32744.424503, 'change': 1.44612354, 'low': 44203.28, 'high': 45560}

        .. tip::

            Useful indicators:

            * Opening price: ``analysis.indicators["open"]``
            * Closing price: ``analysis.indicators["close"]``
            * Momentum: ``analysis.indicators["Mom"]``
            * RSI: ``analysis.indicators["RSI"]``
            * MACD: ``analysis.indicators["MACD.macd"]``

Retrieving multiple analysis
----------------------------

.. code-block:: python3

    from tradingview_ta import *
    analysis = get_multiple_analysis(screener="america", interval=Interval.INTERVAL_1_HOUR, symbols=["nasdaq:tsla", "nyse:docn", "nasdaq:aapl"])

.. note::

    You can't mix different screener and interval.

Parameters: 

* symbols (``list``) – List of exchange and ticker symbol separated by a colon. Example: ["NASDAQ:TSLA", "NYSE:DOCN"] or ["BINANCE:BTCUSDT", "BITSTAMP:ETHUSD"].
* screener (``str``) – Screener (e.g., ``"america"``, ``"indonesia"``, ``"forex"``, ``"crypto"``).
* timeout (``float``, optional) – How long to wait (in seconds) for the server to return a response.
* interval (``str``) – Time frame
  
    .. note::

        Please see the Interval class for available intervals.

        .. code-block:: python3

            class Interval:
                INTERVAL_1_MINUTE = "1m"
                INTERVAL_5_MINUTES = "5m"
                INTERVAL_15_MINUTES = "15m"
                INTERVAL_30_MINUTES = "30m"
                INTERVAL_1_HOUR = "1h"
                INTERVAL_2_HOURS = "2h"
                INTERVAL_4_HOURS = "4h"
                INTERVAL_1_DAY = "1d"
                INTERVAL_1_WEEK = "1W"
                INTERVAL_1_MONTH = "1M"

.. note::
    ``get_multiple_analysis()`` returns a dictionary with a format of {"EXCHANGE:SYMBOL": Analysis}.

    .. code-block:: python3
        
        # Example
        {'NYSE:DOCN': <tradingview_ta.main.Analysis object at 0x7f3a5ba49be0>, 'NASDAQ:TSLA': <tradingview_ta.main.Analysis object at 0x7f3a5ba65040>, 'NASDAQ:AAPL': <tradingview_ta.main.Analysis object at 0x7f3a5ba801c0>}

    Please use UPPERCASE letters when accessing the dictionary.

    If there is no analysis for a certain symbol, ``Analysis`` will be replaced with a ``None``. For example, ``BINANCE:DEXEUSDT`` does not have an analysis, but ``BINANCE:BTCUSDT`` has:

    .. code-block:: python3

        # Example
        {'BINANCE:DEXEUSDT': None, 'BINANCE:BTCUSDT': <tradingview_ta.main.Analysis object at 0x7f3561cdeb20>}

Proxy
-----
Simply add the ``proxies`` parameter if you wish to utilize a proxy. It's worth noting that a bad proxy could result in TradingView rejecting your request.

    .. code-block:: python3

        from tradingview_ta import TA_Handler, Interval, Exchange
        tesla = TA_Handler(
            symbol="TSLA",
            screener="america",
            exchange="NASDAQ",
            interval=Interval.INTERVAL_1_DAY,
            proxies={'http': 'http://0.0.0.0:8080', 'https': 'https://0.0.0.0:443'}
        )
        print(tesla.get_analysis().summary)
        # Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}
