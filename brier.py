import csv

total = 0
count = 0
with open("markets.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["open_price"])
        outcome = 0
        if row["result"] == "yes":
            outcome = 1
        total += (price - outcome) ** 2
        count += 1

print(f"Brier score: {total / count:.4f} over {count} markets")