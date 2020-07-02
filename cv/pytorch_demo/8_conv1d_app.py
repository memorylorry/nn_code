import torch
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

# load data
df = np.loadtxt('data.csv',delimiter=',',usecols=(2,3,4),skiprows=1)#[::-1]
# 取出收盘价
close = df[:,0]
f=torch.tensor(close.copy(),dtype=torch.float).reshape(1,1,-1)

# 定义一维的卷积核
k5=np.hstack((np.zeros(15),np.full((5),0.2))).reshape(1,-1)
k10=np.hstack((np.zeros(10),np.full(10,0.1))).reshape(1,-1)
k20=np.hstack((np.zeros(0),np.full(20,0.05))).reshape(1,-1)
k=np.stack((k5,k10,k20))
k=torch.tensor(k,dtype=torch.float)
# 开始运算
h=F.conv1d(f,k,stride=1)

# 绘图
# 取均线
ma = h.clone().numpy()
ma5 = ma[0][0]
ma10 = ma[0][1]
ma20 = ma[0][2]
# 构造close的x轴
x1 = np.arange(len(close))
# 构造MA的x轴
x5 = np.arange(len(ma5))
dif5 = len(x1) - len(x5)
x5 = x5 + dif5
x10 = np.arange(len(ma10))
dif10 = len(x1) - len(x10)
x10 = x10 + dif10
x20 = np.arange(len(ma20))
dif20 = len(x1) - len(x20)
x20 = x20 + dif20
# 绘图
plt.figure(figsize=(7, 6))
plt.plot(x1,close,'x',color='#ff0000',label='raw',alpha=0.5)
plt.plot(x5,ma5,'-',color='#ffcc00',label='MA5')
plt.plot(x10,ma10,'-',color='#cc0099',label='MA10')
plt.plot(x20,ma20,'-',color='#00ff00',label='MA20')
plt.legend()
plt.xlabel('day of x')
plt.ylabel('price')

plt.show()
