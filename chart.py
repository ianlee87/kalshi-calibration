import csv

totals = [0] * 10
yeses = [0] * 10

with open("markets.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        price = float(row["open_price"])
        bucket = min(int(price * 10), 9)
        totals[bucket] += 1

        if row["result"] == "yes":
            yeses[bucket] += 1

for i in range(10):
    if totals[i] == 0:
        continue
    rate = yeses[i] / totals[i]
    print(f"{i*10}-{(i+1)*10}¢: {totals[i]} markets, {rate:.0%} yes")

