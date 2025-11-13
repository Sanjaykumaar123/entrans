import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle(r"C:/Users/HP/ENTRANS/clean_sales.pkl")

start = pd.to_datetime(input("Enter start date (YYYY-MM): "))
end = pd.to_datetime(input("Enter end date (YYYY-MM): "))

df["Date"] = pd.to_datetime(df["Date"])

filtered = df[(df["Date"] >= start) & (df["Date"] <= end)]

if filtered.empty:
    print("No data found in this date range. Try another range.")
else:
    monthly = filtered.groupby(filtered["Date"].dt.to_period("M"))[["Revenue", "Profit"]].sum()
    monthly.plot()
    plt.savefig("trend.png")
    plt.close()
    print("Trend plot saved as trend.png")
