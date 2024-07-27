import pandas as pd
df = pd.read_csv("Data Cleaning and Preprocessing.csv")
print(df)
df_new = df[df["BF-CMratio"]>100]
print(df_new)
df.info()
df.fillna(130,inplace=True)
df.info()
print(df.describe())
dd = df.dropna()
print(dd)