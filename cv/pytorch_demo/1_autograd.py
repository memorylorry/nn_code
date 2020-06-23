import torch
import matplotlib.pyplot as plt

d_str = 'cuda' if torch.cuda.is_available() else 'cpu'
device = torch.device(d_str)
dt = torch.float

x = torch.randn(100,1,dtype=dt,device=device)
y = torch.randn(100,1,dtype=dt,device=device)
theta = torch.randn(1,1,dtype=dt,device=device,requires_grad=True)

losses = []

for i in range(300):
    y_pre = x.mm(theta)
    loss = (y_pre-y).pow(2).sum()
    # print(loss.item())
    losses.append(loss)
    loss.backward()

    with torch.no_grad():
        theta -= 1e-2 * theta.grad
        theta.grad.zero_()

plt.plot(losses,'r-')
plt.show()