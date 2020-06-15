import torch
import numpy as np

data = np.arange(5,dtype=np.float)
x = torch.tensor(data,requires_grad=True)

m = x.mean()
print(m)
m.backward()
print(x.grad)