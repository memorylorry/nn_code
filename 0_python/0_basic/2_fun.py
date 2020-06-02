# 本文主要介绍函数的使用及参数问题

# A. 基本用法
# 在形参中，定义参数，可以带有默认值，也可以不带默认值（但带默认值的参数，在使用时，有代码提示！）
def greet(username, age=18):
    print('Hello,'+username+'. Are you '+ str(age) +' years old?')

greet('darling')


# B. 形参详解
# 1. 使用变量，如何让PyCharm能够提示？
# ANS : 在形参上指定类型，或给其赋值
def greet2(username:str,job='programmer'):
    print('My name is '+ username +', and my job is a '+job+'.')

# 2. 参数传递方式
greet2('xi')
greet2('mo','investor') # (调用方式：位置实参) 此处可以覆盖形参的初始值
greet2(username='mo',job='runner') # (调用方式：关键字实参)
greet2(username='mo') # (调用方式：关键字实参+默认实参)


# C. 返回值
def formatName(firstName, lastName, midName=''):  # 带初始值的参数，必须全部放后面
    if midName == '':
        return firstName + ' ' + lastName
    return firstName + ' ' + midName + ' ' + lastName

name = formatName('Monkey','Li')
print(name)


# D. 传值(数、字符串)、传址(dict、list)
# Q1
x=1
y=2
info='test'
def add(x,y,info:str): # n1. 传普通的变量(数字、字符串)，是传值；若字典
    x = x**2
    str = 'add'
    return x+y

print(add(x,y,info))
print(x)
print(info)

# Q2
mDict = {'a':2}
def test_dict(my_dict:dict): # n2. 传字典是传引用
    my_dict['b'] = 3

test_dict(mDict)
print(mDict)

# Q3
mList = [1,2]
def test_list(m_list:list): # n2. 传列表是传引用，若想禁止函数内部更改，可用def test_list(m_list[:])去拷贝一份给内部函数使用
    m_list.append(3)

test_list(mList)
print(mList)


# E. 传递任意数量的实参
def report(*toppings): # 给变量名前加*号，就可以接受任意个数的参数，相当于用了一个该名称元组装了参数
    print(toppings)

report('melon','suger','ice')

# 1. 结合使用位置实参和任意数量实参
# 如果要让函数接受不同类型的实参,必须在函数定义中将接纳任意数量实参的形参放在最后。
def report2(name:str,*toppings):
    pass

# 2. 使用任意数量的关键字实参
def build_profile(name, **user_info):
    print(user_info)

build_profile('xia',age=20,job='sporter')

# 3. 上面2种综合(一个星星的参数必须在两个星星的参数前！！！)
def check1(name:str,*mTupple,**mDict):
    pass
