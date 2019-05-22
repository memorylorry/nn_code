import numpy as np

'''
array创建,你可以通过传统的arry创建numpy array
'''
arr1 = np.array([1,2,3,])
arr2 = np.array([(1,3,4),(5,3,2)])
print(arr1)
print(arr2)


# 0数组的创建
arr3 = np.zeros((3,5))
print(arr3)

# 1数组的创建
arr4 = np.ones((2,5))
print(arr4)

# 空数组的创建
arr5 = np.empty((2,3))
print(arr5)

# arange方法创建
arr6 = np.arange(1,20,3)
print(arr6)

# linspace方法建立
arr7 = np.linspace(1,10,10)
print(arr7)