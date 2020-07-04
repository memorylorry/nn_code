import numpy as np

# 日期增序的收盘价
close=np.loadtxt('data.csv',delimiter=',',skiprows=1,usecols=(3),unpack=True)[::-1]
dif = np.diff(close)
returns = dif/close[:-1]
print(np.std(returns))
