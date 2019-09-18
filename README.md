# symbol

A script that gathers symbol information for cryptocurrencies featured on trusted exchanges, see https://www.bti.live for the definition and methodology to determine whether wash trading is present on an exchange.\

Supported exchanges:\

binance\
bitfinex\
bithumb\
bitstamp\
coinbase\
kraken\
liquid\
okex\
upbit\

# output
The script generates a pandas dataframe with the following columns:\
"symbol" : Pair symbol recognised by the exchange\
"baseAsset" : Base currency recognised by the exchange\
"quoteAsset" : Quote currency recognised by the exchange\
"mappedBaseAsset" : Base asset mapped to a common symbol (using mapping generated by crypto compare)\
"mappedQuoteAsset" : Quote asset mapped to a common symbol (using mapping generated by crypto compare)\
"lastMappingUpdate" : Last update applied to the mapping\
"exchange" : exchange name\

File is written to csv excluding all records that do not have complete naming information.

# future work

Add support for additional exchanges.\
Accumulate 24 hr volume data for each pair symbol.\

