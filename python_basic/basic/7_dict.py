user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}


# P1 - 增
user_0['new'] = 'test' # 通过key增加
print(user_0)


# P2 - 删
del user_0['new']
print(user_0)


# P3 - 改
user_0['username'] = 'malong' # 通过key更改
print(user_0)


# P4 - 查
print(user_0['username'])  # 通过key访问;若查找不存在的key的值,会抛异常
print(user_0)


# method 1. 遍历dict
for key,value in user_0.items():
    print('method 1 : ',key + ' : '+value)

# method 2. 遍历dict
for key in user_0.keys():
    print('method 2 : ',key + ' : '+user_0[key])

# method 3. 遍历dict
for idx,key in enumerate(user_0.keys()):
    print('method 3 : ',key + ' : '+user_0[key],'pos:',idx)


# 其他操作
user_1 = user_0 # 传地址!!!
user_1['username'] = 'xigua'
print(user_0)

user_2 = user_0.copy() # 拷贝出来,再赋值给新的变量!!!
user_2['username'] = 'xigua2' # 此处不影响user_0中的值
print(user_0)

user_0.clear() # 清空字典
print(user_0)