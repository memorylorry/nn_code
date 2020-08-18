import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
trainset = torchvision.datasets.CIFAR10('data',train=True,transform=transform,download=True)
trainloader = torch.utils.data.DataLoader(
                                            trainset,
                                            batch_size=4,
                                            shuffle=True,
                                            num_workers=2
                                        )

dataiter = iter(trainloader)


class MyNet(torch.nn.Module):
    def __init__(self):
        super(MyNet,self).__init__()
        self.conv1 = torch.nn.Conv2d(3, 6, 5)
        self.conv2 = torch.nn.Conv2d(6, 16, 5)
        self.line1 = torch.nn.Linear(16*5*5,120)
        self.line2 = torch.nn.Linear(120, 84)
        self.line3 = torch.nn.Linear(84, 10)

    def forward(self,x):
        x = F.max_pool2d(F.relu(self.conv1(x)),kernel_size=2,stride=2)
        x = F.max_pool2d(F.relu(self.conv2(x)),kernel_size=2,stride=2)
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.line1(x))
        x = F.relu(self.line2(x))
        x = self.line3(x)
        return x

# 定义模型
net = MyNet()
# net.to(device)

sd = torch.load('sd.pkl')
net.load_state_dict(sd)
optimizer = torch.optim.SGD(net.parameters(),lr=1e-3, momentum=0.9)
criterion = torch.nn.CrossEntropyLoss()
running_loss=0
# for epoch in range(10):  # loop over the dataset multiple times
#
#     running_loss = 0.0
#     for i, data in enumerate(trainloader, 0):
#         # get the inputs; data is a list of [inputs, labels]
#         inputs, labels = data[0].to(device), data[1].to(device)
#
#         # zero the parameter gradients
#         optimizer.zero_grad()
#
#         # forward + backward + optimize
#         outputs = net(inputs)
#         loss = criterion(outputs, labels)
#         loss.backward()
#         optimizer.step()
#
#         # print statistics
#         running_loss += loss.item()
#         if i % 2000 == 1999:    # print every 2000 mini-batches
#             print('[%d, %5d] loss: %.3f' %
#                   (epoch + 1, i + 1, running_loss / 2000))
#             running_loss = 0.0
# torch.save(net.state_dict(),'sd.pkl')


imgs,labels = dataiter.next()

output = net(imgs)
output = torch.max(F.softmax(output,dim=1),dim=1)[1]
classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

print('Real: ', ' '.join('%5s' % classes[labels[j]]
                              for j in range(4)))
print('Predicted: ', ' '.join('%5s' % classes[output[j]]
                              for j in range(4)))

npimg = torchvision.utils.make_grid(imgs,nrow=4,padding=0,normalize=True).numpy()
npimg = np.transpose(npimg,(1,2,0))
plt.imshow(npimg)
plt.show()