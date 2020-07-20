import torch
import numpy as np
import matplotlib.pyplot as plt

x_r = np.arange(-10,10,0.1)
y_r = -x_r**4 + x_r**3 + 10*np.random.rand(len(x_r))


device = torch.device('cpu')


class MyReLUNet(torch.nn.Module):
    def __init__(self):
        super(MyReLUNet, self).__init__()
        self.line1 = torch.nn.Linear(1, 2)
        self.line2 = torch.nn.Linear(2, 1)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        y = self.relu(self.line1(x))
        y = self.line2(y)
        return y


net = MyReLUNet()
net.to(device=device)

x = torch.tensor(x_r,dtype=torch.float,device=device)
y = torch.tensor(y_r,dtype=torch.float,device=device)

loss_fn=torch.nn.MSELoss(reduction='mean')
optimizer=torch.optim.SGD(net.parameters(),lr=1e-5)
losses =[]

# plt.ion()

#
# sd=torch.load('sn.pkl')
# net.load_state_dict(sd)

for i in range(1000):
    # predict
    y_pred = net(x.reshape(-1,1))
    # count loss
    loss = loss_fn(y_pred.reshape(-1),y)
    losses.append(loss.item())
    print(loss.item())
    # plot
    # if i%10==0:
    #     plt.subplot(2, 1, 1)
    #     y_p = y_pred.clone().reshape(-1).detach().numpy()
    #     plt.plot(x_r, y_r, 'rx')
    #     plt.plot(x_r, y_p, 'k-')
    #     plt.subplot(2, 1, 2)
    #     plt.plot(losses, 'rx')
    #     plt.show()
    #     plt.pause(0.5)
    # update weight
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

torch.save(net.state_dict(),'sn.pkl')

plt.figure(figsize=(10,10))
# plt.subplot(2, 1, 1)
y_p = y_pred.clone().reshape(-1).detach().cpu().numpy()
plt.plot(x_r, y_r, 'rx')
plt.plot(x_r, y_p, '-',color='#00ccff')
# plt.subplot(2, 1, 2)
# plt.plot(losses, 'rx')
plt.show()