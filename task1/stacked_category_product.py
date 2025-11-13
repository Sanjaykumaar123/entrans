import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle(r"C:/Users/HP/ENTRANS/clean_sales.pkl")

t = df.groupby(["Product_Category", "Product"])["Revenue"].sum().unstack()
t.plot(kind="bar", stacked=True)
plt.title("Revenue by Category & Product")
plt.ylabel("Revenue")
plt.savefig("stacked_category_product.png")
plt.close()
print("Stacked bar saved as stacked_category_product.png")