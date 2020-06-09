import numpy as np

# 构造数组
# P1 构造0矩阵和1矩阵 (Ones and Zeros)
a1 = np.empty((3,4)) # 返回1个指定类型的数组，未指定初始化的数据
print(a1)
a2 = np.eye(3) # 返回1个单位矩阵
print(a2)
a3 = np.ones((3,4)) # 返回值都为1的矩阵
print(a3)
a4 = np.zeros((3,4)) # 返回值都为0的矩阵
print(a4)
a5 = np.full((3,4),2) # 返回值都为'指定值'的矩阵
print(a5)
a6 = np.zeros_like(a1) # 创建一个和a1相同形状的0矩阵
print(a6)
a7 = np.ones_like(a1) # 创建一个和a1相同形状的1矩阵
print(a7)
a8 = np.empty_like(a4)  # 创建一个和a4相同形状的空矩阵
print(a8)
a9 = np.full_like(a4,9) # 创建一个和a4相同形状的9矩阵
print(a9)

# P2 用已有数据构造数组 (From existing data)
arr1 = [[1,2,3],[4,5,6]]
arr2 = ([1,2,3],[4,5,6],[7,8,9])
arr3 = [(1,2,3),(4,5,6)]
arr4 = ((1,2,3),(4,5,6))
nn = [arr1,arr2,arr3,arr4]

for n in nn:
    res = np.array(n) # Create an array.
    # res = np.asarray(n) # Convert the input to an array.
    # res = np.copy(n) # Return an array copy of the given object.
    # print(res)
    # print(type(res))
    # print(res.dtype)

# Construct an array from data in a text or binary file.
ff = np.fromfile('one_d_array.txt', sep=',', dtype=np.int)
print(ff)

# Construct an array by executing a function over each coordinate.
ffun1 = np.fromfunction(lambda i,j:i==j,shape=(3,3))
ffun2 = np.fromfunction(lambda i,j:i+j,shape=(3,3))
ffun3 = np.fromfunction(lambda i:i,shape=(7,))
print(ffun1)
print(ffun2)
# print(ffun3)

# Create a new 1-dimensional array from an iterable object.
iter = range(0,5)
it = np.fromiter(iter,np.int)
print(it)

# A new 1-D array initialized from text data in a string.
str = '1,2,3,4,5,6'
n_str = np.fromstring(str,sep=',',dtype=np.int)
print(n_str)

# Load data from a text file.
n_txt = np.loadtxt('two_d_array.txt',skiprows=1,delimiter=',',dtype=np.float)
print(n_txt)


# P3 Creating record arrays (numpy.rec)


# P4 Creating character arrays (numpy.char)#


# P5 Numerical ranges
ar1 = np.arange(3) # Return evenly spaced values within a given interval.
ar1 = np.arange(1,10,1) # arange([start,] stop[, step,], dtype=None)
print(ar1)

ar2 = np.linspace(0,10,20) # Return evenly spaced numbers over a specified interval.
print(ar2)

ar3 = np.logspace(0,10,20)
print(ar3)

ar4 = np.linspace((-1,-2),(1,2))
# print(ar4)

# P6 Building matrices
arr1 = np.diag((1,2,3)) # 创建对角矩阵
print(arr1)
arr2 = np.diag((1,2,3),k=1) # 指定k值后（k>0），表示值相对主角线，向上偏k个位置；反则，向下偏。

arr3 = np.diagflat([[1,2],[3,4]]) # 使用diagflat函数，先将数组摊平成1维数组，然后生成对角矩阵;也可以指定k值
print(arr3)

# 用已有矩阵，生成上三角、下三角矩阵
arr4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.tril(arr4)) # 用tril生成下三角的矩阵
print(np.triu(arr4)) # 用triu生成上三角的矩阵

# 用vander函数生成范德蒙行列式(vandermonde matrix)
arr5 = np.vander((1,2,3,4),increasing=True) # 指定increasing=True，则幂的数字，从左向右增长；不指定，则从右向左
print(np.flipud(arr5.transpose()))


# P7 The Matrix class