import torch
import torch.nn as nn
import numpy as np
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F

import os
import sys
import warnings
import json

from utils.LossTracer import LossTracer


class ModelRunner():

    def __init__(self,model,optimizer,criterion,model_name,device='cpu',epoch_steps = 10):
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.model_name = model_name
        self.device = device

        self.conf_path = model_name + '.json'
        self.model_path = model_name + '.pkl'

        # 如果存在配置文件，则先用配置文件初始化epoch_base变量
        self.tracer = LossTracer()
        self.tracer.load(self.conf_path)
        self.epoch_base = self.tracer.epoch_base

        self.epoch_steps = epoch_steps

    '''
    初始化模型；若本地存在模型的参数，则用已有参数初始化模型
    '''
    def init_model(self):
        flag = os.path.exists(self.model_path)
        if flag:
            sd = torch.load(self.model_path)
            self.model.load_state_dict(sd)

    def train(self,loader,batches_to_print=20):
        # check if it exist, if True then load it
        self.init_model()

        # Train
        for epoch in range(self.epoch_steps):
            running_loss = 0
            for i, data in enumerate(loader, 0):
                inputs, labels = data[0].to(self.device), data[1].to(self.device)

                self.optimizer.zero_grad()
                output = self.model(inputs)
                loss = self.criterion(output, labels)
                running_loss += loss.item()

                loss.backward()
                self.optimizer.step()

                if i % batches_to_print == (batches_to_print-1):
                    avg_loss = running_loss / batches_to_print
                    print('epoch %3d, round %3d loss:  %.7f' %
                        (epoch + self.epoch_base + 1, i + 1, avg_loss))
                    # trace it
                    self.tracer.value.append(avg_loss)
                    running_loss = 0.0

        # modify params
        self.epoch_base += self.epoch_steps
        self.tracer.epoch_base = self.epoch_base

        # Save Model 、params and precision
        torch.save(self.model.state_dict(), self.model_path)
        self.tracer.store(self.conf_path)
        
        return self.epoch_base

    def eval(self, loader,topk=1):
        # loader cannot be None
        if loader is None:
            warnings.warn('loader cannot be None!')
            return -1

        full = 0
        err = 0

        for i, data in enumerate(loader, 0):
            inputs, labels = data[0].to(self.device), data[1].to(self.device)
            output = self.model(inputs)
            prob, index = torch.max(F.softmax(output), dim=1)
            dif = index - labels

            full += index.size()[0]
            err += dif[dif != 0].size()[0]

        rate = round(err / full * 100, 4)
        return rate
    
    # 计算所有指定的top
    def eval_all(self,trainloader,testloader,epoch, train_top=[1],test_top=[1],history={}):
        if trainloader:
            for k in train_top:
                rate = self.eval(trainloader,topk=k)
                name = 'train_top_'+str(k)
                isExist = (name in history.keys())
                if isExist:
                    history[name].append(rate)
                else:
                    history[name] = [rate]
                
        if testloader:
            for k in test_top:
                rate = self.eval(testloader,topk=k)
                name = 'test_top_'+str(k)
                isExist = (name in history.keys())
                if isExist:
                    history[name].append(rate)
                else:
                    history[name] = [rate]
        
        # 新增epoch
        if 'epoch' in history.keys():
            history['epoch'].append(epoch)
        else:
            history['epoch'] = [epoch]
        
        return history