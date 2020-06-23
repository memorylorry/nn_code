import torch
import numpy as np

x = torch.tensor([1,2,3],requires_grad=True,dtype=torch.float)
y = torch.mean(x ** 2 + x + 1)
y.backward() # 通过该方法🛫触发d(y)/d(x)
print(x.grad)