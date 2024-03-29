import matplotlib.pyplot as plt
import numpy as np

# 数据按日期降序排列
df = np.loadtxt('data.csv',delimiter=',',skiprows=1,usecols=[1,5], dtype=float,unpack=True)

# Volumn-weighted Average Price
vwap = np.average(df[0],weights=df[1])
print("VWAP is : " + str(vwap))

# Average Price
mean = np.mean(df[0])
print("算数平均数: " + str(mean))

# Time-weighted Average Price
w = np.arange(1,len(df[0])+1)[::-1]
twap = np.average(df[0],weights=w)
print("TWAP is : " + str(twap))

# 简单收益率
arr = np.array([1,2,1.5,1.8,3])
print(np.diff(arr)/arr[:-1])

# 对数收益率
res2 = np.diff(np.log(arr))
print(res2)

# 判断哪些收益率为负
pos = np.where(res2<0)

# variance
var = np.var(df[0])
print("variance is : " + str(var))


# plot
x = np.zeros((len(df[0])))
plt.plot(x,df[0],'go',label='df[0]',alpha=0.2)
plt.plot([vwap],'ro',label='vwap')
plt.plot([mean],'bo',label='mean')
plt.plot([twap],'ko',label='twap')
plt.legend()
plt.show()
