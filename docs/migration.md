# Migration
This guide will help you to migrate from v3.0.0 to v3.1.0. Refer to [Usage](usage.md) for a complete guide.

## What's different
In addition of setting the variable directly, you can now use functions.

## Symbol
```python
# v3.0.0
handler.symbol = "TSLA"
# v3.1.0
handler.set_symbol_as("TSLA")
```

## Exchange

```python
# STOCKS and CRYPTO
# v3.0.0
handler.exchange = "NASDAQ"
# v3.1.0
handler.set_exchange_as_crypto_or_stock("NASDAQ")
```

```python
# Forex
# v3.0.0
handler.exchange = "FX_IDC"
# v3.1.0
handler.set_exchange_as_forex()
```

```python
# CFD
# v3.1.0
handler.exchange = "TVC"
# v3.1.0
handler.set_exchange_as_cfd()
```

## Screener
```python
# Stocks
# v3.0.0
handler.screener = "america"
# v3.1.0
handler.set_screener_as_stock("america")
```

```python
# Crypto
# v3.0.0
handler.screener = "crypto"
# v3.1.0
handler.set_screener_as_crypto()
```

```python
# Forex
# v3.0.0
handler.screener = "forex"
# v3.1.0
handler.set_screener_as_forex()
```

```python
# CFD
# v3.0.0
handler.screener = "cfd"
# v3.1.0
handler.set_screener_as_cfd()
```

## Interval

Refer to [Usage](usage.html#setting-the-interval) for a complete interval list.

```python
# Interval
# v3.0.0
handler.interval = "1m"
# v3.1.0
handler.set_interval_as(interval.INTERVAL_1_MINUTE)
```
