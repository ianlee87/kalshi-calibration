import requests
from datetime import datetime
import csv
import time


r = requests.get("https://api.elections.kalshi.com/trade-api/v2/markets", params={"status": "settled", "limit": 100, "series_ticker": "KXHIGHNY"})
database = r.json()

rows = []
for market in database["markets"]:
    time.sleep(0.2)
    start = int(datetime.fromisoformat(market["open_time"].replace("Z", "+00:00")).timestamp())
    end = int(datetime.fromisoformat(market["close_time"].replace("Z", "+00:00")).timestamp())

    url = f"https://api.elections.kalshi.com/trade-api/v2/series/KXHIGHNY/markets/{market['ticker']}/candlesticks"
    r2 = requests.get(url, params={"start_ts": start, "end_ts": end, "period_interval": 60})
    data = r2.json()

    if "candlesticks" not in data or len(data["candlesticks"]) == 0:
        print("skipped", market["ticker"], data)
        continue

    open_price = data["candlesticks"][0]["price"]["close_dollars"]
    rows.append([market["ticker"], open_price, market["result"]])

with open("markets.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ticker", "open_price", "result"])
    writer.writerows(rows)