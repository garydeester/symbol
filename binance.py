import pandas as pd
import requests

base = "https://api.binance.com/"
exch_info = "api/v1/exchangeInfo"

response = requests.get(base+exch_info)

a = response.json()
df = pd.DataFrame(data = a['symbols'])
print(df[["symbol","baseAsset","quoteAsset"]].head(10))