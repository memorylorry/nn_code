import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F

import warnings
import os


# conf
root ='data'


# load data
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
trainset = torchvision.datasets.CIFAR10(root,train=True,transform=transform,download=True)
trainloader = torch.utils.data.DataLoader(
                                            trainset,
                                            batch_size=512,
                                            shuffle=True,
                                            num_workers=2
                                        )

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
testset = torchvision.datasets.CIFAR10(root,train=False,transform=transform,download=True)
testloader = torch.utils.data.DataLoader(
                                            testset,
                                            batch_size=512,
                                            shuffle=True,
                                            num_workers=2
                                        )


# prepare model
model = torchvision.models.densenet121(pretrained=True, progress=True)
model.to(device)

# prepare optimizer and loss
optimizer = torch.optim.SGD(model.parameters(),lr=0.02,momentum=0.02)
criterion = torch.nn.CrossEntropyLoss()


# train
model_name = 'densenet.pkl'
if os.path.exists(model_name):
    sd = torch.load(model_name)
    model.load_state_dict(sd)
for epoch in range(50):
    running_loss = 0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data[0].to(device), data[1].to(device)

        optimizer.zero_grad()
        output = model(inputs)
        loss = criterion(output, labels)
        print(loss.item())
        print(type(loss))
        running_loss += loss.item()

        loss.backward()
        optimizer.step()

        if i % 20 == 19:
            print('epoch %d, round %3d loss: %.3f' %
                (epoch + 1, i + 1, running_loss / 20))
            running_loss = 0.0

# save model
torch.save(model.state_dict(),model_name)


# count loss
def count_loss(loader):
    # loader cannot be None
    if loader is None:
        warnings.warn('loader cannot be None!')
        return -1

    full = 0
    err = 0

    for i, data in enumerate(loader, 0):
        inputs, labels = data[0].to(device), data[1].to(device)
        output = model(inputs)
        prob, index = torch.max(F.softmax(output), dim=1)
        dif = index - labels

        full += index.size()[0]
        err += dif[dif != 0].size()[0]

    rate = round(err / full * 100, 3)
    return rate


# count train loss
print("Train loss is : ",count_loss(trainloader),"%")
# count test loss
print("Test loss is : ",count_loss(testloader),"%")