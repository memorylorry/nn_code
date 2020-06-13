import numpy as np
import matplotlib.pyplot as plt

y1:np.ndarray = np.logspace(0,10,50)
x = np.linspace(0,10,50)
y2 = 10**x

plt.plot(x,y1,'rx',label='from logspace')
plt.plot(x,y2,'k-',alpha=0.5,label='from 10^x')
plt.legend()
plt.show()

# 由此例子可知，logspace是产生1个符合线性的数组，然后用这些值，算出了10^x，就形成了结果集