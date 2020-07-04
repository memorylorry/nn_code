import numpy as np

x = np.arange(5)
v = np.array([0.1,0.2,0.3])

z = np.convolve(x,v,'full')
print(z)
'''
full: 窗口与边界有交叉
       f : 0   1   2   3   4  g : .1  .2  .3   g(-) : .3  .2  .1 
                          .3  .2  .1
           0  .1  .4   1 1.6 1.7 1.2 
       
same: 结果与原集合的长度一致，但还存在边界问题

valid: 窗口不出边界
'''