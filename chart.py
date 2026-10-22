import csv
import matplotlib.pyplot as plt

totals = [0] * 10
yeses = [0] * 10
price_sums = [0] * 10

with open("markets.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        price = float(row["open_price"])
        bucket = min(int(price * 10), 6)
        totals[bucket] += 1
        price_sums[bucket] += price
        
        if row["result"] == "yes":
            yeses[bucket] += 1

xs = []
ys = []

for i in range(10):
    if totals[i] == 0:
        continue
    rate = yeses[i] / totals[i]
    xs.append(price_sums[i] / totals[i])
    ys.append(rate)
    if i == 6:
        print(f"{i*10}-{(i+4)*10}¢: {totals[i]} markets, {rate:.0%} yes")
    elif i < 6:
        print(f"{i*10}-{(i+1)*10}¢: {totals[i]} markets, {rate:.0%} yes")

plt.plot([0, 1], [0, 1], "--", color="gray", label="perfect calibration")
plt.plot(xs, ys, "o-", label="Kalshi temp")
plt.xlabel("Opening price")
plt.ylabel("Actual yes rate")
plt.title("Kalshi calibration: NYC + Chicago high temperature")
plt.legend()
plt.savefig("calibration.png")
plt.show()