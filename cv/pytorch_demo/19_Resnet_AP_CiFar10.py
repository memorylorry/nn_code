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
testset = torchvision.datasets.CIFAR10('data',train=False,transform=transform,download=True)
testloader = torch.utils.data.DataLoader(
    testset,
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


# count train precision
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

print("Train AP is : ",right/sum)


# count test precision
sum = 0
right = 0
dataiter = iter(testloader)
for images, labels in dataiter:
    images = images.to(device)
    labels = labels.to(device)

    output = resnet50(images)
    _, predicted = torch.max(output, dim=1)

    res=labels-predicted
    res=res[res==0]

    sum += len(labels)
    right += len(res)

print("Test AP is : ",right/sum)