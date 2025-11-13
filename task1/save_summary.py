import pandas as pd

df = pd.read_pickle(r"C:/Users/HP/ENTRANS/clean_sales.pkl")
df.describe(include="all").to_csv("summary_stats.csv")
print("summary_stats.csv saved as summary_stats.csv")
