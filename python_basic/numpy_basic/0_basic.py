# 基础知识
'''
NumPy的主要对象是同构多维数组。
它是一个元素表（通常是数字），所有类型都相同，由非负整数元组索引。
在NumPy维度中称为 轴 。

NumPy的数组类对应的是`ndarray`类，其常见的属性有：
. ndarray.ndim - 数组的轴（维度）的个数。在Python世界中，维度的数量被称为rank。
. ndarray.shape - 数组的维度。这是一个整数的元组，表示每个维度中数组的大小。对于有 n 行和 m 列的矩阵，shape 将是 (n,m)。因此，shape 元组的长度就是rank或维度的个数 ndim。
. ndarray.size - 数组元素的总数。这等于 shape 的元素的乘积。
. ndarray.dtype - 一个描述数组中元素类型的对象。可以使用标准的Python类型创建或指定dtype。另外NumPy提供它自己的类型。例如numpy.int32、numpy.int16和numpy.float64。
. ndarray.itemsize - 数组中每个元素的字节大小。例如，元素为 float64 类型的数组的 itemsize 为8（=64/8），而 complex32 类型的数组的 itemsize 为4（=32/8）。它等于 ndarray.dtype.itemsize 。
. ndarray.data - 该缓冲区包含数组的实际元素。通常，我们不需要使用此属性，因为我们将使用索引访问数组中的元素
'''

# 1个实例
import numpy as np
arr:np.ndarray = np.linspace(1,20,24).reshape(3,8)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.itemsize)
print(arr.dtype)
print(arr.data)