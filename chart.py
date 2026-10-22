import csv
import matplotlib.pyplot as plt

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

xs = []
ys = []

for i in range(10):
    if totals[i] == 0:
        continue
    rate = yeses[i] / totals[i]
    xs.append(i * 0.1 + 0.05)
    ys.append(rate)
    print(f"{i*10}-{(i+1)*10}¢: {totals[i]} markets, {rate:.0%} yes")

plt.plot([0, 1], [0, 1], "--", color="gray", label="perfect calibration")
plt.plot(xs, ys, "o-", label="Kalshi NYC temp")
plt.xlabel("Opening price")
plt.ylabel("Actual yes rate")
plt.title("Kalshi calibration: NYC high temperature")
plt.legend()
plt.savefig("calibration.png")
plt.show()