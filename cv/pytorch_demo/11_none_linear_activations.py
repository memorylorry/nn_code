import torch
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

# 使用非线性激励
x = torch.arange(-10,10,1,dtype=torch.float).reshape(2,-1)
x_r = F.elu(x)
# print(x)
# print(x_r)

z=x.view(4,5)
z[0][0]=999
print(z)
print(x)
