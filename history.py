import requests
url = "https://api.elections.kalshi.com/trade-api/v2/series/KXHIGHNY/markets/KXHIGHNY-26OCT19-B62.5/candlesticks"
r = requests.get(url, params={"start_ts": 1792332000, "end_ts": 1792472400, "period_interval": 60})
data = r.json()
for candle in data["candlesticks"]:
    print(candle["end_period_ts"], candle["price"]["close_dollars"])