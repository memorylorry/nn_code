import numpy as np

i2 = np.eye(N=3)

open,close,volume = np.loadtxt(fname='data.csv',delimiter=',',usecols=(1,3,5),skiprows=1,unpack=True)

# 量加权平均值 VWAP
print(np.average(close,weights=volume))
# 算数平均值
print(np.average(close))
print(np.mean(close))
# 时间加权平均值 TWAP
t = np.arange(len(close))[::-1]
print(np.average(close,weights=t))

# 简单收益率
arr = np.array([1,2,1.5,1.8,3])
print(np.diff(arr)/arr[:-1])

# 对数收益率
res2 = np.diff(np.log(arr))
print(res2)

# 判断哪些收益率为负
pos = np.where(res2<0)

# 计算收盘价的这段周期波动率
log_gain_rate = np.diff(np.log(close))
volatility_rate = np.std(log_gain_rate) / np.mean(log_gain_rate)
print(volatility_rate)
