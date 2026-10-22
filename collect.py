import requests
from datetime import datetime
import csv
import time

all_markets = []
cursor = None

while True:
    params = {"status": "settled", "limit": 1000, "series_ticker": "KXHIGHNY"}
    if cursor:
        params["cursor"] = cursor

    r = requests.get("https://api.elections.kalshi.com/trade-api/v2/markets", params=params)
    database = r.json()
    all_markets.extend(database["markets"])

    cursor = database.get("cursor")
    if not cursor:
        break
print(len(all_markets))

rows = []
for market in all_markets:
    time.sleep(0.2)
    start = int(datetime.fromisoformat(market["open_time"].replace("Z", "+00:00")).timestamp())
    end = int(datetime.fromisoformat(market["close_time"].replace("Z", "+00:00")).timestamp())

    url = f"https://api.elections.kalshi.com/trade-api/v2/series/KXHIGHNY/markets/{market['ticker']}/candlesticks"
    r2 = requests.get(url, params={"start_ts": start, "end_ts": end, "period_interval": 60})
    data = r2.json()

    if "candlesticks" not in data or len(data["candlesticks"]) == 0:
        print("skipped", market["ticker"], data)
        continue

    open_price = None
    for candle in data["candlesticks"]:
        if "close_dollars" in candle["price"]:
            open_price = candle["price"]["close_dollars"]
            break
    if open_price is None:
        continue
    rows.append([market["ticker"], open_price, market["result"]])
print(len(rows))

with open("markets.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ticker", "open_price", "result"])
    writer.writerows(rows)