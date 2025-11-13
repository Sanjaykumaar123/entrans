import pandas as pd

df = pd.read_excel("../sales_data.xlsx")
print(df.isnull().sum())
df.drop_duplicates(inplace=True)
print(df.dtypes)
df.to_pickle("../clean_sales.pkl")
print("done")
