import requests

r = requests.get("https://api.elections.kalshi.com/trade-api/v2/markets", params={"status": "settled", "limit": 100, "series_ticker": "KXHIGHNY"})
database = r.json()
for market in database["markets"]:
    print (market["ticker"], market["last_price_dollars"], market["result"])

yes_count = 0
for market in database["markets"]:
    if market["result"] == "yes":
        yes_count += 1
print("Number of markets with result YES:", yes_count, "out of ", len(database["markets"]))