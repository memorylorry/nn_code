import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt


# load data
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
trainset = torchvision.datasets.CIFAR10('data',train=True,transform=transform,download=True)
trainloader = torch.utils.data.DataLoader(
                                            trainset,
                                            batch_size=512,
                                            shuffle=True,
                                            num_workers=2
                                        )


# load model
resnet50 = torchvision.models.resnet50(pretrained=False,progress=True)
resnet50.to(device)

# load state_dict
sd=torch.load('sd2.pkl')
resnet50.load_state_dict(sd)


# load optimizer
optimizer = torch.optim.SGD(resnet50.parameters(), lr=0.256, momentum=0.9)
criterion = torch.nn.CrossEntropyLoss()


# train step
# for epoch in range(5):
#     running_loss = 0.0
#     for i, data in enumerate(trainloader, 0):
#         inputs, labels = data[0].to(device), data[1].to(device)
#
#         optimizer.zero_grad()
#         output = resnet50(inputs)
#         loss = criterion(output, labels)
#         running_loss += loss.item()
#
#         loss.backward()
#         optimizer.step()
#
#         if i%20==19:
#             print('[%d, %5d] loss: %.3f' %
#                     (epoch + 1, i + 1, running_loss / 20))
#             # print('loss : ', running_loss / 2000)
#             running_loss = 0.0

# torch.save(resnet50.state_dict(),'sd2.pkl')


# preview
dataiter = iter(trainloader)
imgs,labels = dataiter.next()

imgs = imgs[:80].to(device)
labels = labels[:80].to(device)

output = resnet50(imgs)
classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

print('      Raw: ', ' '.join('%5s' % classes[j]
                              for j in labels))

_, predicted = torch.max(output, 1)
print('Predicted: ', ' '.join('%5s' % classes[j]
                              for j in predicted))

res = predicted-labels
print('      DIF: ', ' '.join('%5s' % j.item()
                              for j in res))

npimg = torchvision.utils.make_grid(imgs,nrow=4,padding=0,normalize=True).cpu().numpy()
npimg = np.transpose(npimg,(1,2,0))
plt.imshow(npimg)
plt.show()


# count precision
sum = 0
right = 0
dataiter = iter(trainloader)
for images, labels in dataiter:
    images = images.to(device)
    labels = labels.to(device)

    output = resnet50(images)
    _, predicted = torch.max(output, dim=1)

    res=labels-predicted
    res=res[res==0]

    sum += len(labels)
    right += len(res)

print("AP is : ",right/sum)