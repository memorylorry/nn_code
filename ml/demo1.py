import numpy as np
import pandas as pd
from sklearn import linear_model

import matplotlib.pyplot as plt

def train(x,f):
    reg = linear_model.LinearRegression()
    if(f>2):
        for i in range(2, f):
            # 维度数
            x_i = (x1 ** i).reshape(-1, 1)
            x = np.hstack((x, x_i))

    reg.fit(x, close)
    res = reg.predict(x)
    dev = np.sum((res - close) ** 2) / len(close)
    # print(str(f) + " : " + str(dev))
    return dev

def train2(x,y,f):
    reg = linear_model.LinearRegression()
    x_base = x
    y_base = y
    if(f>2):
        for i in range(2, f):
            # 维度数
            x_i = (x_base ** i).reshape(-1, 1)
            x = np.hstack((x, x_i))
            y_i = (y_base ** i).reshape(-1, 1)
            y = np.hstack((y, y_i))

    reg.fit(x, close)
    res = reg.predict(y)
    return res


df = pd.read_csv('../data.csv',header=0)[::-1]
close = df['close']

x1 = np.arange(1,len(close)+1).reshape(-1,1)

arr = []

# for i in range(1,20):
#     dev = train(x1,i)
#     arr.append(dev)

# print(np.min(arr))

x2 = np.arange(1,85).reshape(-1,1)
res = train2(x1,x2,12)
print(x2)

# plt.plot(x1,close,'rx')
# plt.plot(x2,res,'g-')
# plt.show()