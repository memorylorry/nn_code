# enumerate方法
# 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
# Grammer : enumerate(sequence, [start=0])

# 对list
list = ['orange','apple','melon']

for step,val in enumerate(list):
    print('step : ',step,' val : ',val)

# 对tuple
tup = (6,2,3)
for i,v in enumerate(tup):
    print(i,'-',v)

# 对字符串
str='hello world'
for i,v in enumerate(str):
    print(i,'-',v)