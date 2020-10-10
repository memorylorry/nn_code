##
# 记录损失度的记录器
##

import json
import os


class LossTracer:
    def __init__(self):
        self.epoch_base = 0
        self.index = []
        self.value = []
        pass

    # 追加数据
    def append(self, idx, val):
        self.index.append(idx)
        self.value.append(val)

    # 获取结果
    def fetch(self):
        return self.index, self.value

    # 存结果
    def store(self, file_path):
        data = {
            "epoch_base": self.epoch_base,
            "index": self.index,
            "value": self.value
        }
        # 写入文件
        with open(file_path, 'w') as writer:
            json.dump(data, writer)

    # 取配置
    def load(self, file_path):
        if os.path.exists(file_path):
            with open(file_path) as reader:
                data = json.load(reader)
                self.epoch_base = data['epoch_base']
                self.index = data['index']
                self.value = data['value']
