# 列表 由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字 0~9 或所有家庭成员姓名的列表;也可以将任何东西加入列表中,其中的元素之间可以没有任何关系。
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())


# P1 - 增
bicycles.append('add1') # 在列表后追加元素
bicycles.insert(1,'add2') # 在索引为1的位置，插入元素
print(bicycles)


# P2 - 删
res1 = bicycles.pop() # m1. 使用pop函数，从列表尾部弹出1个元素，并通过返回值返回
del bicycles[1] # m2. 直接根据索引位删除元素
bicycles.remove('cannondale') # m3. 根据值，来删除
print(bicycles)


# P3 - 改
bicycles[0] = 'motor' # 根据索引位，更改元素的值
print(bicycles)


# P4 - 查
# 目前python提供的基础list，暂时未提供查询操作，需要自己实现！
for idx,val in enumerate(bicycles):
    if val == 'redline':
        print(idx) # 打印匹配项的索引值
        break


# Other - 组织列表
bicycles.sort() # 使用方法 sort() 对列表进行永久性排序(字典排序、值的升序)
print(bicycles)
bicycles.sort(reverse=True) # 可以用reverse参数设置，是否为将序排列
print(bicycles)

bicycles = sorted(bicycles) # 使用函数 sorted() 对列表进行临时排序(需要赋值回来)
print(bicycles)

bicycles.reverse() # 到序
print(bicycles)

print(len(bicycles)) # 数组长度

# 遍历列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)