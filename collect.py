import requests
from datetime import datetime

r = requests.get("https://api.elections.kalshi.com/trade-api/v2/markets", params={"status": "settled", "limit": 100, "series_ticker": "KXHIGHNY"})
database = r.json()
for market in database["markets"][:5]:
    start = int(datetime.fromisoformat(market["open_time"].replace("Z", "+00:00")).timestamp())
    end = int(datetime.fromisoformat(market["close_time"].replace("Z", "+00:00")).timestamp())

    url = f"https://api.elections.kalshi.com/trade-api/v2/series/KXHIGHNY/markets/{market['ticker']}/candlesticks"
    r2 = requests.get(url, params={"start_ts": start, "end_ts": end, "period_interval": 60})
    data = r2.json()

    if len(data["candlesticks"]) == 0:
        continue

    open_price = data["candlesticks"][0]["price"]["close_dollars"]
    print(market["ticker"], open_price, market["result"])