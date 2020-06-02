# 本模块主要解释模块的调用
# 总结：
# 1. 为了让工程中，代码与代码直接能够调用，请一调要设置Source Root;其中Source Root相当于一个包
# 2. 使用PyCharm开发时，记得确认勾选了'Add source roots to PYTHONPATH';这将方便包的调用
# 3. 使用方法如往常一样，import python_basic.basic
#
# 本文相关的详细解释，请看
#   https://vimiix.com/post/2017/12/29/import-error-relative-no-parent/
#   https://blog.csdn.net/qq_30622831/article/details/80978118

from python_basic.basic import module_test as mt

mt.sayHello()
print(mt.count)