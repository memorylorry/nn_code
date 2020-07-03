# 利用核函数将图片锐化
import torch
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

# 读入图片
img_r=plt.imread('sample2.jpg')
img=np.stack([img_r])
img=np.transpose(img,(0,3,1,2))
f=torch.tensor(img,dtype=torch.float)

# 生成模糊图片的核函数
k = np.ones([10,10])*(1/100)
k = torch.FloatTensor(k).expand(3,1,10,10)
print(f.size())
print(k.size())

# 利用卷积将图片模糊
'''
torch.nn.functional.conv2d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1) → Tensor
input.size()  - (minibatch,in_channels,iH,iW)
weight.size() - (out_channels,in_channels/groups,kH,kW)
注：由此可知，groups可以将输入的通道分组，避免多通道运算后进行叠加
'''
h=F.conv2d(f,k,groups=3)
print(h.size())

# 将运算后的数据转为可绘制的图像
new_img=h.clone().detach().numpy()
new_img=np.transpose(new_img,(0,2,3,1))[0]/255

# 绘图
plt.figure(figsize=(7,10))
plt.subplot(2,1,1)
plt.title('raw pic')
plt.imshow(img_r)
plt.subplot(2,1,2)
plt.title('blur pic with (10,10)')
plt.imshow(new_img)
plt.show()