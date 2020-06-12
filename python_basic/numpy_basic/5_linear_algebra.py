# 线性代数的运算
# https://numpy.org/doc/stable/reference/routines.linalg.html
import numpy as np
import matplotlib.pyplot as plt

# P1 矩阵和矢量的运算
arr1 = np.diag([1,2,3])
arr2 = np.array([[1],[2],[3]])
arr3 = np.ones((1,9))

# 矩阵的点乘
print(arr1.dot(arr2))
# print(np.dot(arr1,arr2))

# vdot函数是,先将输入的数组展平，然后对应位置求和
print(np.vdot(arr1,arr1))