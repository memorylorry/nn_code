import json
import os

class APTracer():
    def __init__(self):
        self.epoch_base = 0
        self.train_index = []
        self.train_err_rate = []
        self.test_index = []
        self.test_err_rate = []

    # 追加数据
    def append(self, idx, val, train=True):
        if train:
            self.train_index.append(idx)
            self.train_err_rate.append(val)
        else:
            self.test_index.append(idx)
            self.test_err_rate.append(val)

    # 获取结果
    def fetch(self):
        return self.train_index, self.train_err_rate, self.test_index, self.test_err_rate

    # 存结果
    def store(self,file_path):
        data = {
            "epoch_base":self.epoch_base,
            "train_index":self.train_index,
            "train_err_rate": self.train_err_rate,
            "test_index": self.test_index,
            "test_err_rate": self.test_err_rate
        }
        # 写入文件
        with open(file_path,'w+') as writer:
            json.dump(data,writer)

    # 取配置
    def load(self,file_path):
        if os.path.exists(file_path):
            with open(file_path) as reader:
                data = json.load(reader)
                self.epoch_base = data['epoch_base']
                self.train_index = data['train_index']
                self.train_err_rate = data['train_err_rate']
                self.test_index = data['test_index']
                self.test_err_rate = data['test_err_rate']
