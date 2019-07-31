import pandas as pd
import retrieve_symbols
import retrieve_names
import exchange_endpoints
from time import time as tme


if __name__ == "__main__":
    
    t0 = tme()
    exchange = 'binance'
    base,ep = exchange_endpoints.get_endpoints(exchange)
    df_binance = retrieve_symbols.get_symbols_binance(base,ep,exchange)
    t1 = tme() - t0
    print(exchange, "elapsed time: %0.2f"%t1)
    
    t0 = tme()
    exchange = 'upbit'
    base,ep = exchange_endpoints.get_endpoints(exchange)
    df_upbit = retrieve_symbols.get_symbols_upbit(base,ep,exchange)
    t1 = tme() - t0
    print(exchange, "elapsed time: %0.2f"%t1)
    
    #exchange = 'huobi'
    #base,ep = exchange_endpoints.get_endpoints(exchange)
    #df_huobi = retrieve_symbols.get_symbols_huobi(base,ep,exchange)
    #print(df_huobi.head())
    
    t0 = tme()
    exchange = 'coinbase'
    base,ep = exchange_endpoints.get_endpoints(exchange)
    df_coinbase = retrieve_symbols.get_symbols_coinbase(base,ep,exchange)
    t1 = tme() - t0
    print(exchange, "elapsed time: %0.2f"%t1)
    
    t0 = tme()
    exchange = 'liquid'
    base,ep = exchange_endpoints.get_endpoints(exchange)
    df_liquid = retrieve_symbols.get_symbols_liquid(base,ep,exchange)
    t1 = tme() - t0
    print(exchange, "elapsed time: %0.2f"%t1)
    
    t0 = tme()
    exchange = 'okex'
    base,ep = exchange_endpoints.get_endpoints(exchange)
    df_okex = retrieve_symbols.get_symbols_okex(base,ep,exchange)
    t1 = tme() - t0
    print(exchange, "elapsed time: %0.2f"%t1)
    
    t0 = tme()
    exchange = 'bitfinex'
    base,ep = exchange_endpoints.get_endpoints(exchange)
    df_bitfinex = retrieve_symbols.get_symbols_bitfinex(base,ep,exchange)
    t1 = tme() - t0
    print(exchange, "elapsed time: %0.2f"%t1)
    
    t0 = tme()
    exchange = 'kraken'
    base,ep = exchange_endpoints.get_endpoints(exchange)
    df_kraken = retrieve_symbols.get_symbols_kraken(base,ep,exchange)
    t1 = tme() - t0
    print(exchange, "elapsed time: %0.2f"%t1)
    
    t0 = tme()
    exchange = 'bitstamp'
    base,ep = exchange_endpoints.get_endpoints(exchange)
    df_bitstamp = retrieve_symbols.get_symbols_bitstamp(base,ep,exchange)
    t1 = tme() - t0
    print(exchange, "elapsed time: %0.2f"%t1)
    
    t0 = tme()
    exchange = 'bithumb'
    base,ep = exchange_endpoints.get_endpoints(exchange)
    df_bithumb = retrieve_symbols.get_symbols_bithumb(base,ep,exchange)
    t1 = tme() - t0
    print(exchange, "elapsed time: %0.2f"%t1)
    
    dflist = [df_binance,
            df_bitfinex,
            df_bithumb,
            df_bitstamp,
            df_coinbase,
            df_kraken,
            df_liquid,
            df_okex,
            df_upbit]
    
    concat_list = [df for df in dflist if not df.empty]
    
    df_symbols = pd.concat(concat_list)
    df_symbols["loadDatetime"] = int(tme())
    
    response, df_symbols = retrieve_names.get_names(df_symbols)
    print(df_symbols.head())
    print(df_symbols.tail())
    

    
    

    

    
    
    
    
    
    

