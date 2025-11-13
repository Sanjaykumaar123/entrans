import pandas as pd

df = pd.read_pickle(r"C:/Users/HP/ENTRANS/clean_sales.pkl")
df.to_excel(r"C:/Users/HP/ENTRANS/clean_sales.xlsx", index=False)
print("clean_sales.xlsx saved")
