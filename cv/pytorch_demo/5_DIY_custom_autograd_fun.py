import numpy as np
import torch

class MyReLU(torch.autograd.Function):
    @staticmethod
    def forward(ctx,input:torch.Tensor):
        print('DIY forward')
        ctx.save_for_backward(input)
        return input.clamp(min=0)

    @staticmethod
    def backward(ctx, g_output):
        print('DIY backward',g_output)
        input, = ctx.saved_tensors
        grad_input = g_output.clone()
        grad_input[input<0] = 0
        return grad_input


d_str = 'cuda' if torch.cuda.is_available() else 'cpu'
device = torch.device(d_str)


relu = MyReLU.apply

x_r = np.arange(-3,4,dtype=np.float)
x = torch.tensor(x_r,requires_grad=True,device=device)

y = (x*relu(x)).sum()


print(y)
y.backward()
print(x.grad)

