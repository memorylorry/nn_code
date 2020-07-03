import torch
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

# 原始数据
x=torch.arange(0,16,dtype=torch.float).reshape(1,1,4,4)
print(x)

# 定义池化层
maxPooling=torch.nn.MaxPool2d(2,stride=2, return_indices=True)
avgPooling=torch.nn.AvgPool2d(2,stride=2)
# 定义最大的反池化层
unpooling=torch.nn.MaxUnpool2d(2,stride=2)
# 使用池化层
y1,idx1=maxPooling(x)
y2=avgPooling(x)

# 输出
print('MAXPooling',y1)
print('AVGPooling',y2)
# print(unpooling(y1,idx1))