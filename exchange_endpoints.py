

def get_endpoints(exchange):
    if exchange == 'binance':
        """ Only contains symbol information. No names"""
        
        documentation = "https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md"
        
        return "https://api.binance.com/","api/v1/exchangeInfo"
    
    elif exchange == 'bitfinex':
        """ Only contains symbol information. No names"""
        
        documentation = "https://docs.bitfinex.com/docs"
        
        return "https://api.bitfinex.com/v1/","symbols"
    
    elif exchange == 'upbit':
        """ Has a field called English name in market/all but only for base currency
            Currently only has 4 quote currencies ['KRW' 'BTC' 'ETH' 'USDT']
        """
        
        documentation = "https://docs.upbit.com/v1.0.4/reference"
        
        return "https://api.upbit.com/v1/","market/all"
    
    elif exchange == 'huobi':
        """ Only contains symbol information. No names"""
        
        documentation = "https://huobi.readme.io/reference#get_v1-common-symbols"
        
        return "https://api.huobi.pro/","v1/common/symbols"
    
    elif exchange == 'okex':
        """ Only contains symbol information. No names"""
        
        documentation = "https://www.okex.com/docs/en/#spot-currency"
        
        return "https://www.okex.com/","api/spot/v3/instruments"
    
    elif exchange == 'coinbase':
        """ Has name information in a seperate call: /currencies"""
        
        documentation = "https://docs.pro.coinbase.com/#products"
        
        return "https://api.pro.coinbase.com/","products"
    
    elif exchange == 'kraken':
        """ Only contains symbol information. No names"""
        
        documentation = "https://www.kraken.com/features/api"
        
        return "https://api.kraken.com/0/","public/AssetPairs"
    
    elif exchange == 'liquid':
        """ Only contains symbol information. No names"""
        
        documentation = "https://developers.liquid.com/#products"
        
        return "https://api.liquid.com/","products"
    
    elif exchange == 'bitstamp':
        """ Has name information in the description field of the trading-pairs-info/ call"""
        
        documentation = "https://www.bitstamp.net/api/"
        
        return "https://www.bitstamp.net/api/v2/","trading-pairs-info/"
    
    elif exchange == 'bithumb':
        """ Only contains symbol information. No names"""
        
        documentation = "https://apidocs.bithumb.com/docs/ticker"
        
        return "https://api.bithumb.com/public/","ticker/ALL"
