# 本节内容主要描述文件的读取；
# 这里用到了with(它的优势是，不管在处理文件过程中是否发生异常，都能保证 with 语句执行完毕后已经关闭了打开的文件句柄！！！相比try-catch要更好用！！！)
# 关于它的详细描述，请看第10节的部分！

# P1 文件的读取
with open('./pi_digits.txt') as file_obj:
    content = file_obj.read()
    print(content)


# P2 将文件读入到list对象中
print('# P2')
with open('pi_digits.txt') as file_obj:
    lines = file_obj.readlines() # 使用readlines函数，将文本内容，读如到1个list类型的对象中

for line in lines:
    print(line.strip()) # 利用strip函数，去除两端的空字符


# P3 拼接出pi的值
print('#P3')
pi = ''
with open('pi_digits_detail.txt') as file_obj:
    for line in file_obj.readlines():
        pi += line.strip()
print(pi)
print('精度 ： '+str(len(pi)-2))