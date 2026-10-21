import requests

r = requests.get("https://api.elections.kalshi.com/trade-api/v2/markets", params={"status": "settled", "limit": 5})
database = r.json()
for market in database["markets"]:
    print (market["ticker"], market["last_price_dollars"], market["result"])