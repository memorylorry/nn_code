import numpy as np
'''
# N维数组 (The N-dimensional array) (ndarray)

ndarray :每个ndarry通常是一个多维度的、具有相同数据类型、大小的容器。

形状(shape) : 维度数 和 数组中的项，被定义成shape，通常用1个元组（tuple）表示；如3*4的矩阵，其shape为（3，4）

数据类型(dtype) : 数据项的类型，被定义为 data-type object (dtype);表示数组中数据的类型。

'''
# 例子
x = np.array([[1,2,3],[4,5,6]],np.int)
print(type(x))
print(x.shape)
print(x.dtype)






# P2 使用ndarray(这种方法目前使用较少，暂时不展开描述！)
