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
train_set = torchvision.datasets.VOCSegmentation(root, year='2012', image_set='train', download=True,
                                                 transform=transform, target_transform=t_transform)
# test_set = torchvision.datasets.VOCSegmentation(root, year='2012', image_set='val', download=True, transform=transform,target_transform=t_transform)
train_loader = torch.utils.data.DataLoader(train_set, batch_size=1, shuffle=True, num_workers=4)
# test_loader = torch.utils.data.DataLoader(test_set,batch_size=1,shuffle=True,num_workers=4)


# load model
model = torchvision.models.segmentation.fcn_resnet50(pretrained=True, progress=True, num_classes=21)
res = model.to(device)

# hyper parameters
LR = 10e-4
EPOCH = 10

# Load State Dict
model_name = 'fcn'
model_file = model_name + '.pkl'
if os.path.exists(model_file):
    sd = torch.load(model_file)
    model.load_state_dict(sd)

# count accurracy
loss_sum = 0
for step, (img, target) in enumerate(train_loader):
    img = img.to(device)
    target = torch.round(target * 255)  # 小数转整数
    target[target == 255] = 0  # 去除边框
    target = target.to(device, dtype=torch.float)

    # predict
    pred = model(img)
    d = pred['out']  # 预测值
    mask_pred = d.max(1)[1]
    dif = target - mask_pred
    err_num = torch.sum(dif != 0)
    err_rate = err_num.item() / len(torch.flatten(d))
    #    print(err_rate)
    loss_sum += err_rate

print(loss_sum / len(train_loader))