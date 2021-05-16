FAQ
===

Is the data delayed?
--------------------

Yes and no. Quoted from TradingView:

    We provide real-time data for free whenever we're allowed. However, some data is delayed due to specific exchange regulations. Because of this, real-time data must be purchased separately using the page below. US stock market data is real-time and provided by CBOE BZX.

.. note:: TradingView_TA does not support paid real-time data at the moment.

.. note:: Please refer to `TradingView's website <https://www.tradingview.com/gopro/#markets>`_ to see whether the data is delayed or not.

How do I get past data?
-----------------------

Retrieving past data is currently not supported.

How do I create a trading bot?
------------------------------

.. warning:: Trading (especially using bots) is very risky. I won't be responsible for any financial loss. You have been warned.

The pseudocode below should help you get started in creating your own trading bot.

.. code-block:: python3

    # Import packages.
    from tradingview_ta import TA_Handler, Interval, Exchange
    import time

    # Store the last order.
    last_order = "sell"

    # Instantiate TA_Handler.
    handler = TA_Handler(
        symbol="SYMBOL",
        exchange="EXCHANGE",
        screener="SCREENER",
        interval="INTERVAL",
    )

    # Repeat forever.
    while True:
        # Retrieve recommendation.
        rec = handler.get_analysis()["RECOMMENDATION"]

        # Create a buy order if the recommendation is "BUY" or "STRONG_BUY" and the last order is "sell".
        # Create a sell order if the recommendation is "SELL" or "STRONG_SELL" and the last order is "buy".
        if "BUY" in rec and last_order == "sell":
            # REPLACE COMMENT: Create a buy order using your exchange's API.

            last_order = "buy"
        elif "SELL" in rec and last_order == "buy":
            # REPLACE COMMENT: Create a sell order using your exchange's API.

            last_order = "sell"

        # Wait for x seconds before retrieving new analysis.
        # The time should be the same as the interval.
        time.sleep(x)


.. warning:: ``last_order`` won't be saved when the program exit. When the bot restarts, it will always create a new buy order.

.. tip:: Always paper trade before risking your money.

How can I get involved?
-----------------------

If you found a bug, please `create an issue <https://github.com/brian-the-dev/python-tradingview-ta/issues>`_ on the GitHub repository.

You can contribute (new features, bug fix, typo, etc) through the `GitHub repository <https://github.com/brian-the-dev/python-tradingview-ta>`_. Please follow the `guidelines <https://github.com/brian-the-dev/python-tradingview-ta/blob/main/CONTRIBUTING.md>`_ and don't send spammy pull requests.

How does TradingView_TA works?
------------------------------

A simple network inspection on TradingView's website revealed that the data is retrieved through an `undocumented API <https://scanner.tradingview.com/america/scan>`_.

TradingView_TA works by calculating similar data using `algorithms <https://github.com/brian-the-dev/python-tradingview-ta/blob/main/tradingview_ta/technicals.py>`_ reverse-engineered from their `JavaScript code <https://gist.github.com/brian-the-dev/f0bb91658c1f161cafe8990db1473bd6>`_.