Usage
=====

.. note:: Please install or update TradingView_TA to the latest version. Please read the `getting started <overview.rst>`_ guide before continuing.

.. warning:: TradingView_TA older than v3.2.0 is no longer supported. Please update using ``pip install tradingview_ta --upgrade``.

Importing TradingView_TA
------------------------

.. code-block:: python3

    from tradingview_ta import TA_Handler, Interval, Exchange


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
                    INTERVAL_1_HOUR = "1h"
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
            {'Recommend.Other': 0.09090909, 'Recommend.All': 0.17878788, 'Recommend.MA': 0.26666667, 'RSI': 51.35657473, 'RSI[1]': 56.0809039, 'Stoch.K': 40.83410422, 'Stoch.D': 36.71946441, 'Stoch.K[1]': 31.67255276, 'Stoch.D[1]': 39.57313164, 'CCI20': -52.17234223, 'CCI20[1]': 4.5072255, 'ADX': 35.60476973, 'ADX+DI': 28.49583595, 'ADX-DI': 25.60684839, 'ADX+DI[1]': 29.85479333, 'ADX-DI[1]': 26.11840839, 'AO': 8.26394676, 'AO[1]': 12.62397794, 'Mom': -15.22, 'Mom[1]': -2.67, 'MACD.macd': 7.00976885, 'MACD.signal': 10.30480624, 'Rec.Stoch.RSI': 0, 'Stoch.RSI.K': 9.72185595, 'Rec.WR': 0, 'W.R': -62.00277521, 'Rec.BBPower': 1, 'BBPower': -6.09964786, 'Rec.UO': 0, 'UO': 50.27359668, 'EMA5': 376.90090141, 'close': 373.01, 'SMA5': 376.636, 'EMA10': 378.95440164, 'SMA10': 382.691, 'EMA20': 375.62919667, 'SMA20': 379.2195, 'EMA30': 369.05104155, 'SMA30': 371.84066667, 'EMA50': 355.34346605, 'SMA50': 353.6286, 'EMA100': 330.92744806, 'SMA100': 313.3713, 'EMA200': 300.82801448, 'SMA200': 298.2719, 'Rec.Ichimoku': 0, 'Ichimoku.BLine': 375.485, 'Rec.VWMA': -1, 'VWMA': 378.72121396, 'Rec.HullMA9': 1, 'HullMA9': 370.20948148, 'Pivot.M.Classic.S3': 241.12333333, 'Pivot.M.Classic.S2': 296.29333333, 'Pivot.M.Classic.S1': 330.54666667, 'Pivot.M.Classic.Middle': 351.46333333, 'Pivot.M.Classic.R1': 385.71666667, 'Pivot.M.Classic.R2': 406.63333333, 'Pivot.M.Classic.R3': 461.80333333, 'Pivot.M.Fibonacci.S3': 296.29333333, 'Pivot.M.Fibonacci.S2': 317.36827333, 'Pivot.M.Fibonacci.S1': 330.38839333, 'Pivot.M.Fibonacci.Middle': 351.46333333, 'Pivot.M.Fibonacci.R1': 372.53827333, 'Pivot.M.Fibonacci.R2': 385.55839333, 'Pivot.M.Fibonacci.R3': 406.63333333, 'Pivot.M.Camarilla.S3': 349.62825, 'Pivot.M.Camarilla.S2': 354.6855, 'Pivot.M.Camarilla.S1': 359.74275, 'Pivot.M.Camarilla.Middle': 351.46333333, 'Pivot.M.Camarilla.R1': 369.85725, 'Pivot.M.Camarilla.R2': 374.9145, 'Pivot.M.Camarilla.R3': 379.97175, 'Pivot.M.Woodie.S3': 282.365, 'Pivot.M.Woodie.S2': 299.7875, 'Pivot.M.Woodie.S1': 337.535, 'Pivot.M.Woodie.Middle': 354.9575, 'Pivot.M.Woodie.R1': 392.705, 'Pivot.M.Woodie.R2': 410.1275, 'Pivot.M.Woodie.R3': 447.875, 'Pivot.M.Demark.S1': 341.005, 'Pivot.M.Demark.Middle': 356.6925, 'Pivot.M.Demark.R1': 396.175, 'P.SAR': 379.2321, 'open': 375.32}

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
                INTERVAL_1_HOUR = "1h"
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
