import pandas as pd
import requests

def get_names(df_symbols):
    url = "https://min-api.cryptocompare.com/data/all/coinlist"
    response = requests.get(url)
    a = response.json()
    if a['Response'] == "Success":
    
        df_names = pd.DataFrame.from_dict(data = a['Data'],orient = 'index')
        df_symbols = pd.merge(df_symbols,
                              df_names[['Symbol','CoinName']],
                              how = 'left',
                              left_on = 'mappedBaseAsset',
                              right_on = 'Symbol'
                    )
        df_symbols.rename(columns = {'CoinName':'baseAssetName'},
                          inplace = True)
        
        df_symbols = pd.merge(df_symbols,
                              df_names[['Symbol','CoinName']],
                              how = 'left',
                              left_on = 'mappedQuoteAsset',
                              right_on = 'Symbol'
                    )
        df_symbols.rename(columns = {'CoinName':'quoteAssetName'},
                          inplace = True)
        df_symbols.drop(labels = ['Symbol_x','Symbol_y'],
                        inplace = True,
                        axis = 1)
        print(df_symbols.head())
        return a['Response'],df_symbols
    else:
        return a['Response'],df_symbols