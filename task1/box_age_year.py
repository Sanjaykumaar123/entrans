import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_pickle(r"C:/Users/HP/ENTRANS/clean_sales.pkl")

sns.boxplot(x="Age_Group", y="Revenue", hue="Year", data=df)
plt.title("Revenue Distribution by Age Group & Year")
plt.savefig("box_age_year.png")
plt.close()
print("Box plot saved as box_age_year.png")