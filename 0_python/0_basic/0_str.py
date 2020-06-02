# 定义字符串的方式
msg1 = ' hello world '
msg2 = "我可以为'你'做什么"
msg3 = '我可以为"你"做什么'
msg4 = 'hello world'
print(msg1)
print(msg2)
print(msg3)

# 修改字符串的大小写
print(msg1.title())
print(msg1.upper())
print(msg1.lower())

# 拼接字符串
print(msg1+msg2)

# 使用字表位和换行符
print(msg1+'\t'+msg2)
print(msg1+'\n'+msg2)

# 删除字符串的空白
print(msg1.rstrip()) # 去除右边的空格
print(msg1.lstrip()) # 去除左边的空格
print(msg1.strip()) # 去除左右两边的空格
print(msg4.strip('h')) # 去除两边的指定字符串

# 其它常用函数
print(msg1.replace(' ',''))

print(len(msg1)) # 返回串长
print(msg4.startswith('hello'))
print(msg4.endswith('world'))
print(msg4.index('ll'))
print(msg4.find('llx'))

# 字符串的类型判断
# 总结：
# isdigit()
# True: Unicode数字，byte数字（单字节），全角数字（双字节）
# False: 汉字数字，罗马数字,小数
# Error: 无
#
# isdecimal()
# True: Unicode数字，全角数字（双字节）
# False: 罗马数字，汉字数字,小数
# Error: byte数字（单字节）
#
# isnumeric()
# True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
# False: 小数
# Error: byte数字（单字节）
msg4.isalpha()
print(msg4.isspace()) # Return True if the string is a whitespace string (Length is not 0!), False otherwise.
print(msg4.isascii()) # return True if all characters in the string are ASCII, False otherwise.
print('34'.isdecimal()) # Return True if the string is a decimal string (Length is not 0!), False otherwise.
msg4.isdigit()
msg4.isnumeric()
msg4.isprintable()
