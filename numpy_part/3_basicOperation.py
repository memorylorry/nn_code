import numpy as np

a = np.arange(1,6,1)
b = np.linspace(0.1,1,5)


#四则运算
print(a-b)
print(a+b)
print(a*b)
print(a/b)


print(a**b) #幂
print(a%b)  #取余
print(a//b) #取整


#三角函数
print(np.sin(b))
print(np.cos(b))
print(np.tan(b))

# 矩阵乘法
print(a.dot(b))

# 其它操作
print(np.exp(b))
print(np.sqrt(b))