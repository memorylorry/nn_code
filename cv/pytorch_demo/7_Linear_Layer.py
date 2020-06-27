import torch
import numpy as np
import matplotlib.pyplot as plt

# load data
df = np.loadtxt('data.csv',delimiter=',',usecols=(2,3,4),skiprows=1)
x_r = df[:,0]
y_r = df[:,1]

device = torch.device('cpu')
x = torch.tensor(x_r,device=device,dtype=torch.float).reshape(-1,1)
y = torch.tensor(y_r,device=device,dtype=torch.float).reshape(-1,1)

# prepare model
learning_rage = 1e-6
line = torch.nn.Linear(1,1)
loss_fun = torch.nn.MSELoss(reduction='sum')

for i in range(100):
    # predict
    y_pred = line(x)

    # count loss
    loss = loss_fun(y_pred,y)
    print(loss.item())

    # count grad
    loss.backward()
    # update parameters
    with torch.no_grad():
        for param in line.parameters():
            param -= learning_rage*param.grad

        line.zero_grad()


# plot
plt.plot(x_r,y_r,'rx')
yx = y_pred.clone().detach().numpy()
plt.plot(x_r,yx,'k-')
plt.show()