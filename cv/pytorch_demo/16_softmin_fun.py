import torch
import torch.nn.functional as F

# 准备数据
x = torch.tensor([
    [1,3,8],
    [3,7,5]
],dtype=torch.float)

# 使用 softmin 函数计算每个特征的概率,最小的概率最大
y= F.softmin(x,dim=1)
print(y)

# 利用max可以取出某个轴的最大值
print(torch.max(y,1))