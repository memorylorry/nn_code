import torch
import numpy as np
import matplotlib.pyplot as plt

x_r = np.arange(-10,10,0.5)
y_r = (x_r)**2 + 10*np.random.rand(len(x_r))

# define nn
class MyReLUNet(torch.nn.Module):
    def __init__(self):
        super(MyReLUNet, self).__init__()
        self.line1 = torch.nn.Linear(1,1,True)
        self.line2 = torch.nn.Linear(1, 1,True)
        self.line3 = torch.nn.Linear(1, 1, True)
        self.relu = torch.nn.ReLU()

    def forward(self,x):
        y1 = self.line1(self.relu(x-3))
        y2 = self.line2(x)
        y3 = self.line3(self.relu(-x-3))
        return y1+y2+y3

net = MyReLUNet()

x = torch.tensor(x_r,dtype=torch.float)
y = torch.tensor(y_r,dtype=torch.float)

loss_fn=torch.nn.MSELoss(reduction='mean')
optimizer=torch.optim.SGD(net.parameters(),lr=2e-3)
losses =[]

plt.ion()

for i in range(8000):
    # predict
    y_pred = net(x.reshape(-1,1))
    # count loss
    loss = loss_fn(y_pred.reshape(-1),y)
    losses.append(loss.item())
    print(loss.item())
    # plot
    if i%10==0:
        plt.subplot(2, 1, 1)
        y_p = y_pred.clone().reshape(-1).detach().numpy()
        plt.plot(x_r, y_r, 'rx')
        plt.plot(x_r, y_p, 'k-')
        plt.subplot(2, 1, 2)
        plt.plot(losses, 'rx')
        plt.show()
        plt.pause(0.5)
    # update weight
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

plt.show()