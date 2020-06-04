'''
# 本文主要讲述 类的基本 内容
  1. 所有定义的对象默认继承了object对象
  2. 子类可以重写父类的方法
  3. Python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头(__)，该属性就无法被外部访问！
  4. Python中的‘多态的实现’，主要通过带默认值参数的方式实现！！！
  5. 验证是否有‘向上转型’和‘向下转型’的特点(无)！！！
'''

# 基本用法
class Dog():
    # 定义属性的默认值(也可以不写，因为构造方法会增加属性)
    name = 'default'
    age = 1

    # 定义方法
    def __init__(self,name,age): # __init__方法，为object的方法，所有子类均继承了object对象！！！还有更多方法，都可以被继承，目前暂时不再此深入！
        self.name = name
        self.age = age

    def whoAreYou(self):
        print('Hello, I am %s!' % self.name)

    def whatYouCanDo(self):
        print('I, %s, can run and eat!' % self.name)

    def howOldAreYou(self):
        print('I am %d years old!' % self.age)

dog1 = Dog('Mozx',3)
dog1.whoAreYou()


# 子类间的多态性
class Husky(Dog): # 定义哈士奇的这个类，并继承了Dog
    def whatYouCanDo(self): # 重写父类的方法
        print('I, %s, can destroy your room!' % self.name)

class Collie(Dog): # 定义牧羊犬的这个类，并继承了Dog
    # def __init__(self,name='',age=0,dog=None):
    #     if dog is not None:
    #         self = dog
    #     else:
    #         self.name = name
    #         self.age = age
    def whatYouCanDo(self): # 重写父类的方法
        print('I, %s, can help you protect your sheep!' % self.name)

dog_h = Husky('husky',6)
dog_c = Collie('collie',5)
dog_h.whatYouCanDo() # 由这2个方法的调用可知，不同子类的相同函数，所调用的结果不同，于是具有多态性！
dog_c.whatYouCanDo()


# ‘向上转型’和‘向下转型’的特点: python貌似没有这2个概念，所以在此暂时不加以描述。若读者发现有这2个概念，麻烦请github告知我，我将及时更新！
# dog_h_2 = Dog(dog_h) 会报错
# dog_c_2 = Collie(dog=dog1)  # 通过关键字参数传递对象地址,然后self = dog,也无法保存还是已有对象,故认为不存在该概念
# dog_c_2.whoAreYou()