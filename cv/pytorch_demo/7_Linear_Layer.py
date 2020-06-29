import torch
import numpy as np
import matplotlib.pyplot as plt

device = torch.device('cuda')
# load data
df = np.loadtxt('data.csv',delimiter=',',usecols=(2,3,4),skiprows=1)
x_r = df[:,0]
y_r = df[:,1]

device = torch.device('cuda')
x = torch.tensor(x_r,dtype=torch.float,device=device).reshape(-1,1)
y = torch.tensor(y_r,dtype=torch.float,device=device).reshape(-1,1)

# prepare model
learning_rage = 1e-6
line = torch.nn.Linear(1,1)
loss_fun = torch.nn.MSELoss(reduction='sum')
losses=[]

# line mode to cuda
line.to(device)

# enable inactive
plt.ion()
plt.show()

for i in range(1000):
    # predict
    y_pred = line(x)

    # count loss
    loss = loss_fun(y_pred,y)
    losses.append(loss.item())
    print(loss)

    # plot
    if i%10==0:
        plt.subplot(2,1,1)
        plt.scatter(x_r,y_r)
        yp = y_pred.clone().cpu().detach().numpy()
        plt.plot(x_r,yp,'r-')
        plt.subplot(2, 1, 2)
        plt.plot(losses,'r-')
        plt.pause(0.5)

    # count grad
    loss.backward()
    # update parameters
    with torch.no_grad():
        for param in line.parameters():
            param -= learning_rage*param.grad

        line.zero_grad()

plt.ioff()