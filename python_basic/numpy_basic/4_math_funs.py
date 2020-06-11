# 数学相关的函数
# https://numpy.org/doc/stable/reference/routines.math.html
import numpy as np
import matplotlib.pyplot as plt

arr1 = np.arange(0,10) * np.pi/2
# P1 三角函数
# 常用三角函数
arr2_1 = np.sin(arr1)
arr2_2 = np.cos(arr1)
arr2_3 = np.tan(arr1)
print(np.around(arr2_1))
print(np.around(arr2_2))
print(np.tan(arr1))
print(np.arcsin(arr2_1))
print(np.arccos(arr2_1))
print(np.arctan(arr2_3))

# 弧度、角度互转
print(np.deg2rad(90))
print(np.rad2deg(np.pi/2))


# P2 双曲余弦、正弦函数


# P3 舍入运算
arr2 = np.arange(-3,3.1,0.25)
print('raw arr2 : \n' + arr2.__str__())
# around 可用于舍入运算 | round_函数和这个一样
print('around : \n' + np.around(arr2).__str__()) # 四舍、比五多入；对于为5的，就近的偶数进行取舍
print('around : \n' + np.around(2.167,2).__str__()) # 指定小数位，过5进位（不含5）

# floor、ceil取整
print('floor : \n' + np.floor(arr2).__str__()) # floor向下取整
print('ceil : \n' + np.ceil(arr2).__str__()) # ceil向上取整

# trunc截取
print('trunc : \n' + np.trunc(arr2).__str__())

# fix 取该数字最靠近0那边的数字
print('fix : \n' + np.fix(arr2).__str__())

# rint 取该数字最近的整数
print('rint : \n' + np.rint(arr2).__str__())


# P4 求和, products, differences
# 使用sum函数
arr3 = np.arange(9).reshape(3,3)
print('raw arr3 : \n' + arr3.__str__())
print('sum without axis : \n' + np.sum(arr3).__str__()) # 如果不指定axis，则算整个数组的和
print('sum 0 axis : \n' + np.sum(arr3,axis=0).__str__()) # 指定0轴，则按0轴方向进行求和
print('sum 1 axis : \n' + np.sum(arr3,axis=1).__str__()) # 指定1轴，则按照1轴方向球和


# P5 指数和对数运算
# exp函数
print(np.exp(1)) # 求e^1次方
print(np.exp2(3)) # 求2^3次方
print(np.expm1(2)) # 求e^2 - 1

# log函数
print(np.log2(2)) # 求log[2](x)的值
print(np.log(np.e)) # 求ln(x)的值
print(np.log10(10)) # 求log[10](x)的值
print(np.log1p(np.e-1)) # 求ln(x+1)的值
print(np.logaddexp(2,1)) # 求ln(exp(x1) + exp(x2))
print(np.logaddexp2(2,1)) # 求ln(2^x1 + 2^x2)

# P6 其它特别的函数

# P7 浮点数运算常用的函数

# P8 Rational routines

# P9 算术操作

# P10 复数的处理

# P11 其它运算（Miscellaneous）