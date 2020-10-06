##
# 记录损失度的记录器
##

class LossTrace:
    def __init__(self):
        self.index  = []
        self.value = []
        pass

    # 追加数据
    def append(self,idx,val):
        self.index.append(idx)
        self.value.append(val)

    # 获取结果
    def fetch(self):
        return self.index, self.value

import matplotlib.pyplot as plt
plt.figure((20,10))