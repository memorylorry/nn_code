import numpy as np
import matplotlib.pyplot as plt
import torch

data = np.loadtxt('house.csv',delimiter=' ')
x_r:np.ndarray = data[:,0]
y_r:np.ndarray = data[:,3]

# 选取计算设备
device_str = 'cuda' if torch.cuda.is_available() else 'cpu'
device = torch.device(device_str)
# 取出计算的值，并作放缩
dt = torch.float
x = torch.tensor(np.column_stack((np.ones(x_r.size),x_r/np.max(x_r))),dtype=dt,device=device)
y = torch.tensor(y_r/np.max(y_r).reshape(-1,1),dtype=dt,device=device)

theta = torch.randn(2,1,dtype=dt,device=device)
learning_rate = 2e-1
lo = []

# 迭代法梯度下降
for i in range(2):
    y_pre = x.mm(theta)

    # count loss
    loss = (y_pre - y).pow(2).sum().item()
    lo.append(loss)
    if i%10 == 0:
        print(i,loss)

    # count grad
    grad_theta = 2*x.T.mm((y_pre-y))

    # update weights using gradient
    theta -= learning_rate*theta

# 绘图
plt.plot(lo,'r-')
plt.show()