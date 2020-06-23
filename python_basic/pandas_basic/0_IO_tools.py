import pandas as pd

df:pd.DataFrame = pd.read_csv('data_without_title.csv',sep=',',header=None,names=['date','open','high','close','low','volume','price_change'])

print(df.index)
print(df.columns)
print(df['open'])