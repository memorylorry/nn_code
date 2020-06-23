import numpy as np
import matplotlib.pyplot as plt
import torch

# raw data
data = np.loadtxt('data.csv',delimiter=',',usecols=(2,3),skiprows=1)
x_r:np.ndarray = data[:,0]
y_r:np.ndarray = data[:,1]
x_op = x_r/np.max(x_r)
y_op = y_r/np.max(y_r)

# 选取计算设备
device_str = 'cuda' if torch.cuda.is_available() else 'cpu'
device = torch.device(device_str)
# 取出计算的值，并作放缩
dt = torch.float
x = torch.tensor(np.column_stack((np.ones(x_r.size),x_op)),dtype=dt,device=device)
y = torch.tensor(y_op.reshape(-1,1),dtype=dt,device=device)

theta = torch.tensor([[0],[0]],dtype=dt,device=device,requires_grad=True)
learning_rate = 0.3
losses = []

for i in range(1000):
    # predit
    y_pre = x.mm(theta)
    # count loss
    loss = (y_pre-y).pow(2).mean()
    losses.append(loss.item())

    loss.backward()
    # update grad
    with torch.no_grad():
        theta -= learning_rate*theta.grad
        theta.grad.zero_()
        # print(theta)


plt.subplot(3,1,1)
plt.plot(losses,'r-')
plt.ylabel('loss')
plt.xlabel('iter times')
plt.subplot(3,1,2)
plt.plot(x_op,y_op,'rx')
plt.plot(x_op,y_pre.cpu().detach().numpy(),'b-')
plt.legend(['real','predict'])
plt.subplot(3,1,3)
plt.plot(x_r,y_r,'rx')
plt.show()
