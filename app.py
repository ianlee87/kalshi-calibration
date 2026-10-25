import streamlit as st
import csv
import matplotlib.pyplot as plt

totals = [0] * 10
yeses = [0] * 10
price_sums = [0] * 10
brier_total = 0
brier_count = 0

st.title("Kalshi Calibration Dashboard")
st.write("Do Kalshi prices match how often markets actually resolve Yes?")

choice = st.selectbox("Series", ["Both", "KXHIGHNY", "KXHIGHCHI"])
with open("markets.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if choice != "Both" and row["series"] != choice:
                continue
        price = float(row["open_price"])
        bucket = min(int(price * 10), 6)
        totals[bucket] += 1
        price_sums[bucket] += price

        outcome = 0
        if row["result"] == "yes":
            yeses[bucket] += 1
            outcome = 1
        brier_total += (price - outcome) ** 2
        brier_count += 1
        

xs = []
ys = []
table = []

for i in range(10):
    if totals[i] == 0:
        continue
    rate = yeses[i] / totals[i]
    xs.append(price_sums[i] / totals[i])
    ys.append(rate)
    if i == 6:
        label = "60-100¢"
    elif i < 6:
        label = f"{i*10}-{(i+1)*10}¢"
        table.append({"Bucket": label, "Markets": totals[i], "Yes rate": f"{rate:.0%}"})

fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1], "--", color="gray", label="perfect calibration")
ax.plot(xs, ys, "o-", label="Kalshi temp")
ax.set_xlabel("Opening price")
ax.set_ylabel("Actual yes rate")
ax.set_title("Kalshi calibration")
ax.legend()
st.metric("Brier score", f"{brier_total / brier_count:.4f}")
st.pyplot(fig)
st.table(table)