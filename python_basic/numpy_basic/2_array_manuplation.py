import numpy as np
# 数组的常用操作
# P1 基础操作
arr1:np.ndarray = np.arange(1,25).reshape(3,8)
# arr2 = np.zeros(5)

# copy ?????
# np.copyto(arr2,arr1)
# shape函数的使用，类似shape属性
print(np.shape(arr1)) # 返回数组的形状


# P2 改变数组形状
# 使用reshape改变形状（不改变数据本身）
arr2 = arr1.reshape(4,6) # arr1本身不会改变！！！
print(arr2.shape)

# 使用ravel将数组降为1维数组（返回的对象，共享以前的数据）
arr3 = arr1.ravel()
arr3[0] = 333 # ！改变arr3的第0个元素
print('ravel - arr1 : ' + arr1.__str__())   # ！！！第一个数组的0号位的数据改变了
print('ravel - arr3 : ' + arr3.__str__())   #  arr3的0号位数据肯定为333

# 使用flat属性(返回1个1维数组的迭代器)
res = 'flat : '
for i in arr1.flat:
    res += str(i) + ' '
print(res)

# 使用flatten将数组降为1维数组(返回的对象，拷贝地以前的数据)
arr4 = arr1.flatten()
arr4[0] = 444
print('flatten - arr1 : ' + arr1.__str__())
print('flatten - arr4 : ' + arr4.__str__())


# P3 类转置操作(Transpose-like operations)


# P4 改变维度数(Changing number of dimensions)


# P5 改变array的种类


# P6 连接数组


# P7 拆分数组


# P8 Tiling arrays


# P9 增加、删除元素


# P10 Rearranging elements

