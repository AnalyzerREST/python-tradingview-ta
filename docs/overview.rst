Getting Started
===============

This guide will help you understand the basics of TradingView_TA package.

Requirements
------------

* Python 3.6 or newer
* Internet access

Installation
------------

TradingView_TA is available on `PyPI <https://pypi.org/project/tradingview-ta/>`_.

.. code-block:: console

    pip install tradingview-ta

Quick Start
-----------

.. code-block:: python3

    from tradingview_ta import TA_Handler, Interval, Exchange

    tesla = TA_Handler(
        symbol="TSLA",
        screener="america",
        exchange="NASDAQ",
        interval=Interval.INTERVAL_1_DAY
    )
    print(tesla.get_analysis().summary)
    # Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}