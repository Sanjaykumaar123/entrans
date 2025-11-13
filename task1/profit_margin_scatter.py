import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle(r"C:/Users/HP/ENTRANS/clean_sales.pkl")
df["Profit_Margin"] = df["Profit"] / df["Revenue"]
plt.scatter(df["Profit_Margin"], df["Profit"])
plt.xlabel("Profit Margin")
plt.ylabel("Profit")
plt.title("Profit Margin vs Profit")
plt.savefig("profit_margin.png")
plt.close()
print("Profit margin scatter saved as profit_margin.png")