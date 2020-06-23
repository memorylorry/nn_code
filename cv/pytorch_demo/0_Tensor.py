import torch

d_str = 'cuda' if torch.cuda.is_available() else 'cpu'
device = torch.device(d_str)
dt = torch.float

# 定义数据
x = torch.randn(3,3,device=device,dtype=dt,requires_grad=True)

# 用to方法转移计算的容器
y = x.to('cpu')
print(x)
print(y)


# requires_grad=True
x = torch.tensor([1,2,3],requires_grad=True,dtype=torch.float)
y = torch.mean(x ** 2 + x + 1)
y.backward() # 通过该方法🛫触发d(y)/d(x)
print(x.grad)