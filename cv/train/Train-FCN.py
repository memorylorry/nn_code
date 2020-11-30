import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

from utils.ProgressBar import ProgressBar
from utils.ArrayPainter import convertArr2IMG
import torch.nn.functional as F

import PIL

from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter()


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# Load Data
transform = transforms.Compose([
#     transforms.Resize((500,500)),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])
t_transform = transforms.Compose([
#     transforms.Resize((500,500)),
    transforms.ToTensor()
])

root = '/home/huqian/data/datasets'
train_set = torchvision.datasets.VOCSegmentation(root, year='2012', image_set='train', download=True, transform=transform,target_transform=t_transform)
# test_set = torchvision.datasets.VOCSegmentation(root, year='2012', image_set='val', download=True, transform=transform,target_transform=t_transform)
train_loader = torch.utils.data.DataLoader(train_set,batch_size=1,shuffle=True,num_workers=4)
# test_loader = torch.utils.data.DataLoader(test_set,batch_size=1,shuffle=True,num_workers=4)


# Define the helper function
def decode_segmap(image, nc=21):
    label_colors = np.array([(0, 0, 0),  # 0=background
                             # 1=aeroplane, 2=bicycle, 3=bird, 4=boat, 5=bottle
                             (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128),
                             # 6=bus, 7=car, 8=cat, 9=chair, 10=cow
                             (0, 128, 128), (128, 128, 128), (64, 0, 0), (192, 0, 0), (64, 128, 0),
                             # 11=dining table, 12=dog, 13=horse, 14=motorbike, 15=person
                             (192, 128, 0), (64, 0, 128), (192, 0, 128), (64, 128, 128), (192, 128, 128),
                             # 16=potted plant, 17=sheep, 18=sofa, 19=train, 20=tv/monitor
                             (0, 64, 0), (128, 64, 0), (0, 192, 0), (128, 192, 0), (0, 64, 128)])

    r = np.zeros_like(image).astype(np.uint8)
    g = np.zeros_like(image).astype(np.uint8)
    b = np.zeros_like(image).astype(np.uint8)

    for l in range(0, nc):
        idx = image == l
        r[idx] = label_colors[l, 0]
        g[idx] = label_colors[l, 1]
        b[idx] = label_colors[l, 2]

    rgb = np.stack([r, g, b], axis=2)
    return rgb


# load model
model = torchvision.models.segmentation.fcn_resnet50(pretrained=True, progress=True, num_classes=21)
res = model.to(device)


# hyper parameters
LR= 10e-4
EPOCH = 10


# lambda2 = lambda epoch: LR* (0.9 ** epoch)
optim = torch.optim.SGD(model.parameters(),lr = LR,momentum=0.1)
# scheduler = torch.optim.lr_scheduler.LambdaLR(optim, lr_lambda=lambda2)



model_name = 'fcn'
model_file = model_name + '.pkl'
if os.path.exists(model_file):
    sd = torch.load(model_file)
    model.load_state_dict(sd)

running_loss = 0
for epoch in range(100):
    progress = ProgressBar(len(train_loader))
    for step, (img, target) in enumerate(train_loader):
        img = img.to(device)
        #         img = torch.ceil(img*255)
        target = torch.round(target*255)
        target[target==255] = 0
        # print('t:',target[target>0])
        target = target.to(device, dtype=torch.long)

        optim.zero_grad()
        d = model(img)['out']
        #         print('target:',d.size())
        #         print('target:',target.size())
        log_p = F.log_softmax(d, dim=1)
        loss = F.nll_loss(log_p, target[0], reduction='mean')
        loss.backward()
        optim.step()

        running_loss += loss.item()
        progress.step(step+1)
        # break
    #     scheduler.step()
    avg_loss = running_loss / len(train_loader)
    running_loss = 0
    print(' epoch-',epoch+1,'loss',avg_loss)
    writer.add_scalar("Loss/train", avg_loss, epoch + 1)
    writer.flush()

torch.save(model.state_dict(), model_file)
