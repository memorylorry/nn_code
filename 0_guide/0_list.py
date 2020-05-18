# 列表 由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字 0~9 或所有家庭成员姓名的列表;也可以将任何东西加入列表中,其中的元素之间可以没有任何关系。
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

# 追加元素
bicycles.append('add1')

# 插入元素
bicycles.insert(1,'add2')
print(bicycles)

# 删除元素
# 根据标记删除
del bicycles[1]
# 利用pop()删除
res1 = bicycles.pop()
# 利用值来删除
bicycles.remove('cannondale')
print(bicycles)


# 组织列表
## 使用方法 sort() 对列表进行永久性排序
bicycles.sort()
print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)

## 使用函数 sorted() 对列表进行临时排序(需要赋值回来)
bicycles = sorted(bicycles)
print(bicycles)

## 倒着
bicycles.reverse()
print(bicycles)

## 数组长度
print(len(bicycles))