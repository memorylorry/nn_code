import numpy as np

'''
基础内容
'''
# numpy array，它是array的一种衍生，但却不同于标准的array
arr = np.arange(10).reshape(2,5)
print(arr)

# 打印维度数
print(arr.ndim)
# 打印类型
print(arr.shape)
# 打印数据类型
print(arr.dtype)
# 打印每个数据长度
print(arr.itemsize)
# 打印数据
print(arr.data)


