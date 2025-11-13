import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_pickle("../clean_sales.pkl")

sns.histplot(df["Customer_Age"])
plt.savefig("age_hist.png")
plt.close()

sns.countplot(x=df["Customer_Gender"])
plt.savefig("gender_plot.png")
plt.close()

sns.barplot(x=df["Age_Group"], y=df["Revenue"])
plt.savefig("age_revenue.png")
plt.close()

df.groupby("Product_Category")["Profit"].sum().sort_values().plot(kind="barh")
plt.savefig("profit_by_category.png")
plt.close()

print("done")
