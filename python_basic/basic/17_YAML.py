import os
import yaml

'''
一、yaml文件介绍
YAML是一种简洁的非标记语言。其以数据为中心，使用空白，缩进，分行组织数据，从而使得表示更加简洁。
1. yaml文件规则
基本规则：
    大小写敏感
    使用缩进表示层级关系
    缩进时不允许使用Tab键，只允许使用空格。
    缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
    使用#表示注释
    字符串可以不用引号标注

2. yaml文件数据结构

    对象：键值对的集合（简称 "映射或字典"）
    键值对用冒号 “:” 结构表示，冒号与值之间需用空格分隔
    数组：一组按序排列的值（简称 "序列或列表"）
    数组前加有 “-” 符号，符号与值之间需用空格分隔
    纯量(scalars)：单个的、不可再分的值（如：字符串、bool值、整数、浮点数、时间、日期、null等）
    None值可用null可 ~ 表示

二、安装yaml

pip命令： pip install PyYaml
引入：import yaml
用python读取yaml文件如下:

代码:
import yaml
from Common.dir_config import *

# 打开yaml文件
fs = open(os.path.join(caps_dir, "data.yaml"),encoding="UTF-8")
datas = yaml.load(fs)
print(datas)
备注：yaml版本5.1之后弃用，YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated
代码改后：
import yaml
from Common.dir_config import *

# 打开yaml文件
fs = open(os.path.join(caps_dir, "data.yaml"),encoding="UTF-8")
datas = yaml.load(fs,Loader=yaml.FullLoader)  #添加后就不警告了
print(datas)
'''


file_name = 'conf/test.yaml'


# Sample 1
# if os.path.exists(file_name):
#     fs = open(file_name,encoding='UTF-8')
#     conf = yaml.load(fs)
#     # 输出dict类型的数据
#     print(conf)
#     # 备注：yaml版本5.1之后弃用，YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated

# Sample 2
if os.path.exists(file_name):
    fs = open(file_name,encoding='UTF-8')
    conf = yaml.load(fs,Loader=yaml.FullLoader)
    # 输出dict类型的数据
    print(conf)