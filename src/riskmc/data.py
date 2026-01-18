import pandas as pd

def load_prices(path):
    #df of adjusted close prices
    #index: date
    #columns: assets
    prices = pd.read_csv(path, index_col=0, parse_dates=True)
    return prices