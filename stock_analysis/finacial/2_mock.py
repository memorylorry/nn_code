import numpy as np
import matplotlib.pyplot as plt

base = 20 # 本金
rate = 0.5 # 每年用于投资的比例
inc = 0.3 # 年增长率
years = 20 # 投资年限
salary = 7 # 年工资剩余

# 计算复利
x = np.arange(1,years+1)
y = [base]
for i in range(1,years):
    get = y[-1]*rate*inc + y[-1] + salary
    y.append(get)

# 绘图
plt.plot(x,y,'rx')
plt.plot(x,y,'k-')
plt.xlabel('years')
plt.ylabel('m(w)')
plt.show()



