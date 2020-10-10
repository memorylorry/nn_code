import torch
import torch.nn as nn
import numpy as np
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F

import os
import sys

class ModelRunner():
    
    def __init__(self,epoch_base = 0,epoch_steps = 10):
        self.epoch_base = epoch_base
        self.epoch_steps = epoch_steps
    
    def setTrainLoader(self,trainloader):
        self.trainloader = trainloader
        return self
    
    def setTestLoader(self,testloader):
        self.testloader = testloader
        return self
    
    def setModel(self,model):
        self.model = model
        return self
    
    def count_loss(self,train=True):
        # set loader
        loader = self.trainloader if train else self.testloader
        
        # loader cannot be None
        if loader is None:
            warnings.warn('loader cannot be None!')
            return -13

        full = 0
        err = 0

        for i, data in enumerate(loader, 0):
            inputs, labels = data[0].to(device), data[1].to(device)
            output = model(inputs)
            prob, index = torch.max(F.softmax(output), dim=1)
            dif = index - labels

            full += index.size()[0]
            err += dif[dif != 0].size()[0]

        rate = round(err / full * 100, 4)
        return rate

    def train(self,model_name,optimizer,criterion,device='cpu'):
        # check if it exist, if True then load it
        flag = os.path.exists(model_name)
        if flag:
            sd = torch.load(model_name)
            self.model.load_state_dict(sd)

        # Train
        for epoch in range(self.epoch_steps):
            running_loss = 0
            for i, data in enumerate(self.trainloader, 0):
                inputs, labels = data[0].to(device), data[1].to(device)

                optimizer.zero_grad()
                output = self.model(inputs)
                loss = criterion(output, labels)
                running_loss += loss.item()

                loss.backward()
                optimizer.step()

                if i % 20 == 19:
                    print('epoch %3d, round %3d loss:  %.7f' %
                        (epoch + self.epoch_base + 1, i + 1, running_loss / 20)) 
                    running_loss = 0.0

        # Save Model
        torch.save(self.model.state_dict(),model_name)

        # store train loss and test loss
    #     epoch_idx = epoch + epoch_base + 1
    #     train_loss = count_loss(trainloader)
    #     test_loss = count_loss(testloader)
    #     train_trace.append(epoch_idx,train_loss)
    #     test_trace.append(epoch_idx,test_loss)

        # modify params
        self.epoch_base += self.epoch_steps