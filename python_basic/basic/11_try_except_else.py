# try_except_else 用于捕获程序异常，然后决定是否向外通知、或中断程序
# try-except 本身就满足异常捕获的条件了；同时还可以搭配else使用(也就是说else不是必要的部分，可有可无！！！)：
#     1. 若try的内部'发生'异常，则'不会'进入else部分
#     2. 若try的内部'未发生'异常，则'会'进入else部分！

filename = 'no_this_file.txt'
# filename = 'pi_digits.txt'
try:
    with open(filename) as file_obj:
        pass
except FileNotFoundError:
    print(FileNotFoundError.__str__())
else:
    print('try中未发生任何异常，走这里！！！')
