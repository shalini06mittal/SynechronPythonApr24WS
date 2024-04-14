import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime

df = pd.read_csv('prices.csv')
# print(df)
df = df.rename(columns={'Open':'Open','Date':'Date','Close':'Close','Low':'Low'})
# print(df)
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')
print(df)

plt.plot(df['Date'], df['Open'], label='Open')
plt.plot(df['Date'], df['Close'], label='Close')
plt.legend()
plt.show()
