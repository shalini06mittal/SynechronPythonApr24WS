import pandas as pd

df = pd.read_csv('employees.csv')
print(df)
print(df.head(n=3))

# df1 = pd.read_excel('data.xlsx',  index_col=0)
# print(df1)

print(df.describe())