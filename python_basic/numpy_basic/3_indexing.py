# 切片和常用的函数

# 常规索引
import numpy as np
arr1:np.ndarray = np.arange(0,9,dtype=np.int)
# P1.1 单个元素索引
print('单个元素索引 : ' + arr1[2].__str__()) # 通过索引的方式引用
print('单个元素索引 : ' + arr1[-1].__str__()) # 从后开始数的第1个数字

# P1.2 索引数组方式索引
x = np.arange(2,5)
print('索引数组方式索引 : ' + arr1[x].__str__())

# P1.3 切片方式索引
'''
切片操作基本表达式：object[start_index : end_index : step]

step：正负数均可，其绝对值大小决定了切取数据时的“步长”，而正负号决定了“切取方向”，正表示“从左往右”取值，负表示“从右往左”取值。当step省略时，默认为1，即从左往右以增量1取值。“切取方向非常重要！”“切取方向非常重要！”“切取方向非常重要！”，重要的事情说三遍！

start_index：表示起始索引（包含该索引本身）；该参数省略时，表示从对象“端点”开始取值，至于是从“起点”还是从“终点”开始，则由step参数的正负决定，step为正从“起点”开始，为负从“终点”开始。

end_index：表示终止索引（不包含该索引本身）；该参数省略时，表示一直取到数据”端点“，至于是到”起点“还是到”终点“，同样由step参数的正负决定，step为正时直到”终点“，为负时直到”起点“。
'''
print('切片方式索引 : ' + arr1[2:4].__str__()) # 从2-4（不含4）的所有数字
print('切片方式索引 : ' + arr1[-3:].__str__()) # 从倒数第3个开始到最后

print('切片方式索引 : ' + arr1[2:7:2].__str__()) #从2开始，到7，每次隔了2个步长

print('切片方式索引 : ' + arr1[::-1].__str__()) # 逆序

arr2:np.ndarray = arr1[:] # 返回1个浅拷贝的列表出来，其实改变arr2的数据，arr1的也变！！！
arr2[0] = 2
print('arr1 - ' + arr1.__str__())

arr3:np.ndarray = arr2.copy() # 为了避免浅拷贝的问题，用copy可以做深拷贝！！！
print('arr2 - ' + arr2.__str__())

# P1.4 索引多维数组
arr4:np.ndarray = np.arange(1,17).reshape(4,4)
x = np.array([0,2])
y = np.array([0,1])
print('索引多维数组 arr4 : \n'+arr4.__str__())
print(arr4[x,y]) # 分别用等长的x和y构成了索引的坐标；若这2者不等，则会异常

# P1.5 布尔或“掩码”索引数组
print('布尔或“掩码”索引数组 : \n'+arr4[arr4>10].__str__())

# P1.6 将索引数组与标量结合（利用了广播机制）
print('将索引数组与标量结合 : \n'+arr4[x,0].__str__()) # 这里的0会扩充成和x同样形状

# P1.7 将索引数组与切片组合（利用了广播机制）
print('将索引数组与切片组合 : \n'+arr4[x,0:3].__str__()) # 这你的0：3的每个数字都利用了广播特性；
                                                     # 实际上，切片被转换为索引数组 np.array([[0,1,2]]) (shape (1,3))，
                                                     # 它与索引数组一起广播以产生一个结果 shape(2,3) 的数组。


# P2 常用取元素的函数
# P2.1 产生索引数组
arr3:np.ndarray = arr1.reshape((3,3))

# where函数，条件为True，则用x中的值；为False，则用y中的值。(Return elements chosen from x or y depending on condition.)
arr3_res = np.where(arr3>3,arr3,np.zeros_like(arr3))
print(arr3_res)

# 使用diag_indices获取对角线的索引；ndim可设置维度diag_indices
print(np.diag_indices(3))
print(arr3[np.diag_indices(3)])

# diag_indices_from函数，根据数组来取得对角线的索引位置
print(np.diag_indices_from(arr3))

# 使用mask_indices函数，获取上三角的索引位
print(np.mask_indices(3,np.tril))

# 获取上或下三角索引位的专用函数
print(np.tril_indices(3))
print(np.tril_indices_from(arr3))
print(np.triu_indices(3))
print(np.triu_indices_from(arr3))


# P2.2 类似索引的操作(Indexing-like operations)
# take函数，先将数组arr3展平，然后根据index中的索引值取数，最后形成和index数组同样类型的数组
print(np.take(arr3,np.arange(0,4)))

# compress函数，根据条件从中筛选出数据；可指定筛选的轴
arr4 = np.compress([0,1],arr3) # 如果不指定axis的值，则先将数组展平，再筛选
print(arr4)

arr4 = np.compress([False,True],arr3,axis=0) # 指定只筛选第0轴的
print(arr4)

arr4 = np.compress([False,True],arr3,axis=1) # 指定只筛选第0轴的
print(arr4)

# select函数的使用（使得根据条件列表，从选项列表中选择值）
arr5 = np.arange(9)
condition_list = [arr5<3,arr5>5] # 条件列表
choices_list = [arr5,arr5**2] # 选项列表
print(np.select(condition_list,choices_list))

# P2.3 插入元素

# P2.4 Iterating over arrays