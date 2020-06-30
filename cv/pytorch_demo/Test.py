import torch
import torch.utils.data as Data
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

x = torch.unsqueeze(torch.linspace(-10,10,200),dim=1)
y = 1/(torch.exp(-x)+1) - 1/2

# dataset divide into mini batch
trainset = Data.TensorDataset(x,y)
loader = Data.DataLoader(dataset=trainset,batch_size=1000,shuffle=False,num_workers=4)

# define model
net = torch.nn.Sequential(
    torch.nn.Linear(1,40),
    torch.nn.ReLU(),
    torch.nn.Linear(40,1)
)
# lossFn and optimizer
lossFn = torch.nn.MSELoss()
optimizer = torch.optim.SGD(net.parameters(),lr=0.005)

plt.ion()
plt.show()

try:
    sd=torch.load('ff.pkl')
    net.load_state_dict(sd)
except Exception:
    pass

for epoch in range(5000):
    y_pred: torch.Tensor = net(x)
    loss = lossFn(y_pred, y)
    # print('batch-', idx, 'loss-', loss.item())

    if epoch % 500 == 0:
        x_s = x.clone().detach().numpy()
        y_s = y.clone().detach().numpy()
        y_p_s = y_pred.clone().detach().numpy()
        plt.cla()
        plt.scatter(x_s, y_s)
        plt.plot(x_s, y_p_s, 'r-')
        plt.pause(0.5)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

torch.save(net.state_dict(),'ff.pkl')
#
# for epoch in range(5):
#     for idx, (batch_x, batch_y) in enumerate(loader):
#         y_pred: torch.Tensor = net(batch_x)
#         loss = lossFn(y_pred, batch_y)
#         print('batch-', idx, 'loss-', loss.item())
#
#         if idx % 5 == 0:
#             x_s = batch_x.clone().detach().numpy()
#             y_s = batch_y.clone().detach().numpy()
#             y_p_s = y_pred.clone().detach().numpy()
#             plt.cla()
#             plt.scatter(x_s, y_s)
#             plt.plot(x_s, y_p_s, 'r-')
#             plt.pause(0.5)
#
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()






# plt.scatter(x,y)
# plt.show()
plt.ioff()
