import pandas as pd

def load_prices(path):
    #df of adjusted close prices
    #index: date
    #columns: assets
    prices = pd.read_csv(path, index_col=0, parse_dates=True)
    return prices

def create_data(path, tickers):
    import yfinance as yf
    import pandas_market_calendars as mcal
    from pathlib import Path
    import pandas as pd

    tickers = tickers
    Period = '24mo'

    #download daily prices
    raw = yf.download(tickers=tickers, period=Period, interval='1d', auto_adjust=True, progress=False,)

    #keep close prices only
    prices = raw['Close'].copy()
    prices = prices[tickers]
    prices.index = pd.to_datetime(prices.index)
    prices = prices.sort_index()

    #enforce NYSE trading calendar (no gaps)

    nyse = mcal.get_calendar('NYSE')
    schedule = nyse.schedule(
        start_date=prices.index.min(),
        end_date=prices.index.max()
    )

    trading_days = pd.DatetimeIndex(schedule.index)

    #reindex to official trading days and drop incomplete rows
    prices = prices.reindex(trading_days).dropna(how='any')

    #save to CSV
    prices.index.name = 'Date'
    prices.to_csv(path)

    print(f'Saved {len(prices)} rows to {path}')
    return prices.tail()