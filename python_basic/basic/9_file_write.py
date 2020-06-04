# 本文之讲述文件的写入
'''
# 文件的操作模式(关键概念)
1. 读取模式(r) : 需要读取文件内容的时候，用该模式，该参数可缺省。
2. 写模式(w) : 在写文件时，用该模式。注意：对于已存在的文件，该模式会从重写调以前的内容！！！
3. 附加模式(a) ： 该模式，相当于向文件后追加内容。a - append！！！
'''

with open('write_content.txt','a') as file_obj:
    for i in range(0,10):
        file_obj.write('line - %d\n' % i)