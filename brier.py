import csv

total = {}
count = {}
with open("markets.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        s = row["series"]
        price = float(row["open_price"])
        outcome = 0
        if row["result"] == "yes":
            outcome = 1
        if s not in total:
            total[s] = 0
            count[s] = 0
        total[s] += (price - outcome) ** 2
        count[s] += 1

for s in total:
    print(f"Brier score of {s}: {total[s] / count[s]:.4f} over {count[s]} markets")