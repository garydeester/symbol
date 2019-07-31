import pandas as pd
import requests

def get_mapping(exchange):
    
    url = "https://min-api.cryptocompare.com/data/pair/mapping/exchange?e="
    response_mapping = requests.get(url+exchange)
    b = response_mapping.json()
    df_map = pd.DataFrame(data = b['Data'])
    
    return df_map

def merge_map(df,df_map):
    df = pd.merge(df,
                  df_map,
                  left_on = 'symbol',
                  right_on = 'symbol'
    )
    df.rename(columns = {'fsym':'mappedBaseAsset',
                         'tsym':'mappedQuoteAsset',
                         'last_update':'lastMappingUpdate'
                    },
              inplace = True
    )
    
    return df
    
def get_symbols_binance(base_url,symbol_call,exchange):
    
    try:
        response = requests.get(base_url+symbol_call)
        a = response.json()
        df = pd.DataFrame(data = a['symbols'])
        
        df_map = get_mapping(exchange)
        df_map['symbol'] = df_map['exchange_fsym'] + df_map['exchange_tsym']
        
        df = merge_map(df,df_map)
        df['exchange'] = exchange
        return df[["symbol","baseAsset","quoteAsset","mappedBaseAsset","mappedQuoteAsset","lastMappingUpdate","exchange"]]
    except:
        print("%s symbol retrieve failed"%exchange)
        return pd.DataFrame(data = None)

def get_symbols_bitfinex(base_url,symbol_call,exchange):
    
    try:
        response = requests.get(base_url+symbol_call)

        a = response.json()
        df = pd.DataFrame(data = a,columns = ['symbol'])
        df['baseAsset'] = df['symbol'].str[0:3]
        df['quoteAsset'] = df['symbol'].str[3:6]
        
        df_map = get_mapping(exchange)
        df_map['exchange_fsym'] = df_map['exchange_fsym'].str.lower()
        df_map['exchange_tsym'] = df_map['exchange_tsym'].str.lower()
        df_map['symbol'] = df_map['exchange_fsym'] + df_map['exchange_tsym']
        
        df = merge_map(df,df_map)
        df['exchange'] = exchange
        return df[["symbol","baseAsset","quoteAsset","mappedBaseAsset","mappedQuoteAsset","lastMappingUpdate","exchange"]]
    except:
        print("%s symbol retrieve failed"%exchange)
        return pd.DataFrame(data = None)
    
def get_symbols_upbit(base_url,symbol_call,exchange):
    
    try:
        response = requests.get(base_url+symbol_call)
        
        a = response.json()
        df = pd.DataFrame(data = a)
        df.drop(columns = ['english_name','korean_name'],inplace = True)
        df_bq = df['market'].str.split('-',expand = True)
        df_bq.columns = ['quoteAsset','baseAsset']
        df = df.join(df_bq)
        df.rename(columns = {'market':'symbol'},inplace = True)
        
        df_map = get_mapping(exchange)
        df_map['symbol'] = df_map['exchange_tsym'] + '-' + df_map['exchange_fsym']
        df = merge_map(df,df_map)
        df['exchange'] = exchange
        return df[["symbol","baseAsset","quoteAsset","mappedBaseAsset","mappedQuoteAsset","lastMappingUpdate","exchange"]]
    except:
        print("%s symbol retrieve failed"%exchange)
        return pd.DataFrame(data = None)
    
def get_symbols_huobi(base_url,symbol_call,exchange):
    
    try:
        response = requests.get(base_url+symbol_call)
        
        a = response.json()
        df = pd.DataFrame(data = a['data'])
        df.rename(columns = {"base-currency":"baseAsset","quote-currency":"quoteAsset"},
                  inplace = True
        )
        
        #No mapping for huobi
        #df_map = get_mapping(exchange)
        #df_map['symbol'] = df_map['exchange_fsym'] + df_map['exchange_tsym']
        #
        #df = merge_map(df,df_map)
        return df[["symbol","baseAsset","quoteAsset"]]
    except:
        print("%s symbol retrieve failed"%exchange)
        return pd.DataFrame(data = None)

def get_symbols_coinbase(base_url,symbol_call,exchange):
    
    try:
        response = requests.get(base_url+symbol_call)
        
        a = response.json()
        df = pd.DataFrame(data = a)
        df.rename(columns = {"base_currency":"baseAsset",
                             "quote_currency":"quoteAsset",
                             "id":"symbol"
                        },
                  inplace = True
        )
        
        df_map = get_mapping(exchange)
        df_map['symbol'] = df_map['exchange_fsym'] +'-'+df_map['exchange_tsym']
        df = merge_map(df,df_map)
        df['exchange'] = exchange
        return df[["symbol","baseAsset","quoteAsset","mappedBaseAsset","mappedQuoteAsset","lastMappingUpdate","exchange"]]
    except:
        print("%s symbol retrieve failed"%exchange)
        return pd.DataFrame(data = None)

def get_symbols_liquid(base_url,symbol_call,exchange):
    
    try:
        response = requests.get(base_url+symbol_call)
    
        a = response.json()
        df = pd.DataFrame(data = a)
        df.rename(columns = {'symbol':'currency_symbol',
                             'currency_pair_code':'symbol',
                             'base_currency':'baseAsset',
                             'quoted_currency':'quoteAsset'
                        },
                  inplace = True
        )
        
        df_map = get_mapping(exchange)
        df_map['symbol'] = df_map['exchange_fsym'] + df_map['exchange_tsym']
        df = merge_map(df,df_map)
        df['exchange'] = exchange
        return df[["symbol","baseAsset","quoteAsset","mappedBaseAsset","mappedQuoteAsset","lastMappingUpdate","exchange"]]
    except:
        print("%s symbol retrieve failed"%exchange)
        return pd.DataFrame(data = None)

def get_symbols_okex(base_url,symbol_call,exchange):
    
    try:
        response = requests.get(base_url+symbol_call)
        
        a = response.json()
        df = pd.DataFrame(data = a)
        df.rename(columns = {"base_currency":"baseAsset",
                             "quote_currency":"quoteAsset",
                             "instrument_id":"symbol"
                        },
                  inplace = True
        )
        
        df_map = get_mapping(exchange)
        df_map['symbol'] = df_map['exchange_fsym'] +'-'+ df_map['exchange_tsym']
        df = merge_map(df,df_map)
        df['exchange'] = exchange
        return df[["symbol","baseAsset","quoteAsset","mappedBaseAsset","mappedQuoteAsset","lastMappingUpdate","exchange"]]
    except:
        print("%s symbol retrieve failed"%exchange)
        return pd.DataFrame(data = None)

def get_symbols_kraken(base_url,symbol_call,exchange):
    
    try:
        response = requests.get(base_url+symbol_call)
        
        a = response.json()
        df = pd.DataFrame.from_dict(data = a['result'], orient = 'index')
        df['symbol'] = df.index
        df = df.reset_index()
        df.rename(columns = {'base':'baseAsset',
                             'quote':'quoteAsset'
                        },
                  inplace = True
        )
        
        df_map = get_mapping(exchange)
        df_map['symbol'] = df_map['exchange_fsym'] + df_map['exchange_tsym']
        df = merge_map(df,df_map)
        df['exchange'] = exchange
        return df[["symbol","baseAsset","quoteAsset","mappedBaseAsset","mappedQuoteAsset","lastMappingUpdate","exchange"]]
    except:
        print("%s symbol retrieve failed"%exchange)
        return pd.DataFrame(data = None)

def get_symbols_bitstamp(base_url,symbol_call,exchange):
    
    try:
        response = requests.get(base_url + symbol_call)
        
        a = response.json()
        df = pd.DataFrame(data = a)
        basequote = df['name'].str.split('/',expand = True)
        basequote.columns = ['baseAsset','quoteAsset']
        df = df.join(basequote)
        df.rename(columns = {'url_symbol':'symbol'},
                  inplace = True
            )
        
        df_map = get_mapping(exchange)
        df_map['symbol'] = df_map['exchange_fsym'].str.lower() + df_map['exchange_tsym'].str.lower()
        df = merge_map(df,df_map)
        df['exchange'] = exchange
        return df[["symbol","baseAsset","quoteAsset","mappedBaseAsset","mappedQuoteAsset","lastMappingUpdate","exchange"]]
    except:
        print("%s symbol retrieve failed"%exchange)
        return pd.DataFrame(data = None)
        
def get_symbols_bithumb(base_url,symbol_call,exchange):
    
    try:
        response = requests.get(base_url + symbol_call)
        
        a = response.json()
        b = a['data']
        df = pd.DataFrame(data = a['data']).T
        df['baseAsset'] = df.index
        df['quoteAsset'] = 'KRW'
        df['symbol'] = df['baseAsset'] + df['quoteAsset']
        
        df_map = get_mapping(exchange)
        df_map['symbol'] = df_map['exchange_fsym']+ df_map['exchange_tsym']
        df = merge_map(df,df_map)
        df['exchange'] = exchange
        
        return df[["symbol","baseAsset","quoteAsset","mappedBaseAsset","mappedQuoteAsset","lastMappingUpdate","exchange"]]
    except:
        print("%s symbol retrieve failed"%exchange)
        return pd.DataFrame(data = None)

