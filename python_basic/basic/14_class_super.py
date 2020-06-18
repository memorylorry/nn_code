class Base:
    def __init__(self):
        self.name = 'base'
        print('Base - Init : ' + self.name)


class Next(Base):
    def __init__(self):
        super(Next, self).__init__() # 不调用该方法，子类不会自动调用父类的构造方法初始化参数；对应的也就是如下使用self.name报错
        self.name += ' - modified'
        print('Base - Init : ' + self.name)

class Final(Next):
    def __init__(self):
        super(Final, self).__init__()
        self.name = 'Final'
        print('Base - Init : ' + self.name)

obj = Final()