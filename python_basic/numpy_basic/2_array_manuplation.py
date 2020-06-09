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
ap1:np.ndarray = np.arange(1,13).reshape(3,4)
print('Transpose - ap1 : \n' + ap1.__str__())
print('Transpose - ap1.T : \n' + ap1.T.__str__()) # 使用T获取转置矩阵
print('Transpose - ap1.transpose() : \n' + ap1.transpose().__str__())


# P4 改变维度数(Changing number of dimensions)


# P5 改变array的种类


# P6 连接数组 (Joining arrays)
arr61:np.ndarray = np.arange(1,17).reshape(4,4)
arr62:np.ndarray = np.arange(18,34).reshape(4,4)

# 使用concatenate函数,沿着已存在的轴拼接数组（若横向拼接数组，其行数要一致；若纵向拼接，其列数要一致）(axis=0表示纵向拼接，=1表示横向拼接)
res1 = np.concatenate((arr61,arr62),axis=0)
print('concatenate - res1 : \n' + res1.__str__())

# 使用stack函数沿着1个新的轴拼接数组
res2 = np.stack((arr61,arr62),axis=0)
# res2 = np.stack((arr61,arr62),axis=1)
# res2 = np.stack((arr61,arr62),axis=2)
print(res2)

# 使用column_stack函数，将数组横向拼接成1个新的数组 （所有数组的行数要求相同）？？？
# res3 = np.column_stack((arr61,arr62))
# print(res3)

# 使用dstack函数

# 使用hstack函数进行水平合并
a1 = np.arange(1,4)
a2 = np.arange(6,9)
res3 = np.hstack((a1,a2))
print('hstack - res3 : ' + res3.__str__())
res3 = np.hstack((a1.reshape((-1,1)),a2.reshape((-1,1))))
print('hstack - res3 : \n' + res3.__str__())

# 使用vstack函数进行垂直合并
res4 = np.vstack((a1,a2))
print('vstack - res4 : \n' + res4.__str__())
res4 = np.vstack((a1.reshape((-1,1)),a2.reshape((-1,1))))
print('vstack - res4 : \n' + res4.__str__())

# 使用block函数

# P7 拆分数组


# P8 Tiling arrays


# P9 增加、删除元素


# P10 Rearranging elements
r1 = np.arange(10)
r2 = r1.reshape(2,5)
# 用roll函数对数组进行循环旋转
res5 = np.roll(r2,2) # 这里没有给axis的值，则采用默认方式，先将数组展平成1维数组，然后进行循环移动shift个位置
print('roll - res5 : \n' + res5.__str__())
res6 = np.roll(r2,1,axis=0) # 给定axis=0，即在第0个轴的基础上，进行移动;此处会将第2轴以上的内容当作1个整体元素移动
print('roll - res6 : \n' + res6.__str__())
res7 = np.roll(r2,1,axis=1) # 给定axis=1，即在第1个轴的基础上，并对每个组，分开进行循环移动
print('roll - res7 : \n' + res7.__str__())

# 用reshape函数，进行重新设定形状
res8 = np.reshape(r2,(5,2))
print('reshape - res8 : \n' + res8.__str__())

# 使用flip函数进行反序
r3 = np.arange(0,8).reshape(2,2,2)
res9 = np.flip(r1)
print('flip - res9 : \n' + res9.__str__())
res10 = np.flip(r3) # 如果不指定axis的值，则将所有轴的值都进行逆序
print('flip - res10 : \n' + res10.__str__())
res11 = np.flip(r3,axis=0)
print('flip - res11 : \n' + res11.__str__())

# 使用fliplr进行左右翻转
r4 = np.diag((1,2,3))
res12 = np.fliplr(r4)
print('fliplr - res12 : \n' + res12.__str__())

# 使用flipud进行上下翻转
res13 = np.flipud(r4)
print('flipud - res13 : \n' + res13.__str__())