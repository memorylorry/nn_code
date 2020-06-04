# 我们或许很熟悉了用with去读文件，但with究竟是什么？
# 我想我们需要多加留意with，因为他在🕸后面的使用会很多！！！
# IBM论坛参考 ： https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/
# 官方解读 : https://docs.python.org/release/2.6/whatsnew/2.6.html#pep-343-the-with-statement

'''
# 关键术语

   要使用 with 语句，首先要明白上下文管理器这一概念。有了上下文管理器，with 语句才能工作。

   上下文管理协议（Context Management Protocol）：包含方法 __enter__() 和 __exit__()，支持该协议的对象要实现这两个方法。

   上下文管理器（Context Manager）：支持上下文管理协议的对象，这种对象实现了__enter__() 和 __exit__() 方法。
                                 上下文管理器定义执行 with 语句时要建立的运行时上下文，负责执行 with 语句块
                                 上下文中的进入与退出操作。
                                 通常使用 with 语句调用上下文管理器，也可以通过直接调用其方法来使用。

   运行时上下文（runtime context）：由上下文管理器创建，通过上下文管理器的 __enter__() 和__exit__() 方法实现，__enter__() 方法
                                在语句体执行之前进入运行时上下文，__exit__() 在语句体执行完后从运行时上下文退出。with 语句支持运
                                行时上下文这一概念。

   上下文表达式（Context Expression）：with 语句中跟在关键字 with 之后的表达式，该表达式要返回一个上下文管理器对象。

   语句体（with-body）：with 语句包裹起来的代码块，在执行语句体之前会调用上下文管理器的 __enter__() 方法，执行完语句体之后会执行 __exit__() 方法。
'''

'''
# 基本语法和工作原理

Part 1. 基本语法格式
with context_expression [as target(s)]: 
    with-body
    
                                          !!! 这里 context_expression 要返回一个上下文管理器对象，该对象并不'赋值'给 as 子句中的 target(s) 。
                                          如果指定了 as 子句的话，会将上下文管理器的 __enter__() 方法的返回值赋值给 target(s)。
                                          target(s) 可以是单个变量，或者由“()”括起来的元组（不能是仅仅由“,”分隔的变量列表，必须加“()”）。

                                          Python 对一些内建对象进行改进，加入了对上下文管理器的支持，可以用于 with 语句中，比如可以自动关闭文件、线程锁的自动获取和释放等。

    
Part 2. 使用with操作文件对象的例子
with open('pi_digits_detail.txt') as file_obj:
    for line in file_obj:
        print(line)
        # more code ...
                                 
                              !!! 这里使用了 with 语句，不管在处理文件过程中是否发生异常，都能保证 with 语句执行完毕后已经关闭了打开的文件句柄。
                                  如果使用传统的 try/finally 范式，则要使用类似如下代码：


Part 3. try/finally 方式操作文件对象
somefile = open(r'somefileName')
try:
    for line in somefile:
        print line
        # ...more code
finally:
    somefile.close()
                              !!! 比较起来，使用 with 语句可以减少编码量。已经加入对上下文管理协议支持的还有模块 threading、decimal 等。
                              
                              
Part 4. with的详细过程如下（官方协议文档：https://www.python.org/dev/peps/pep-0343/）
context_manager = context_expression
exit = type(context_manager).__exit__  
value = type(context_manager).__enter__(context_manager)
exc = True   # True 表示正常执行，即便有异常也忽略；False 表示重新抛出异常，需要对异常进行处理
try:
    try:
        target = value  # 如果使用了 as 子句
        with-body     # 执行 with-body
    except:
        # 执行过程中有异常发生
        exc = False
        # 如果 __exit__ 返回 True，则异常被忽略；如果返回 False，则重新抛出异常
        # 由外层代码对异常进行处理
        if not exit(context_manager, *sys.exc_info()):
            raise
finally:
    # 正常退出，或者通过 statement-body 中的 break/continue/return 语句退出
    # 或者忽略异常退出
    if exc:
        exit(context_manager, None, None, None) 
    # 缺省返回 None，None 在布尔上下文中看做是 False
'''


# 自定义 上下文管理器
'''
开发人员可以自定义支持上下文管理协议的类。自定义的上下文管理器要同时实现上下文管理协议所需要的 __enter__() 和 __exit__() 两个方法：
1. context_manager.__enter__() ：进入上下文管理器的运行时上下文，在语句体执行前调用。如果with后面指定了 as 子句的话,with 语句将该方法的返回值赋值给 as 子句中的 target；
2. context_manager.__exit__(exc_type, exc_value, exc_traceback) ：退出与上下文管理器相关的运行时上下文，返回一个布尔值表示是否对发生的异常进行处理。
                                                                  参数表示引起退出操作的异常，如果退出时没有发生异常，则3个参数都为None。
                                                                  如果发生异常，返回True 表示不处理异常，否则会在退出该方法后重新抛出异常以由 with 语句之外的代码
                                                                  逻辑进行处理。
                                                                  如果该方法内部产生异常，则会取代由 statement-body 中语句产生的异常。
                                                                  要处理异常时，不要显示重新抛出异常，即不能重新抛出通过参数传递进来的异常，只需要将返回值设置为 False 
                                                                  就可以了。之后，上下文管理代码会检测是否 __exit__() 失败来处理异常
'''

class DumpContext:
    def sayHello(self):
        print('Hello, I am %s!' % self.tag)
    def __init__(self,tag = 'default'):
        self.tag = tag
    def __enter__(self):
        print('[Enter %s]' % self.tag)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('[Exit %s]' % self.tag)
        if exc_tb is None:
            print('[Exit %s Without Exception]' % self.tag)
        else:
            print('[Exit %s With Exception]' % self.tag)

with DumpContext() as dc:
    dc.sayHello()



# contextlib 模块(可用于简化上述的实现的代码)



# nested函数
# nested 可以将多个上下文管理器组织在一起，避免使用嵌套 with 语句。
'''
with nested(A(), B(), C()) as (X, Y, Z):
     # with-body code here

# 类似于如下功能

with A() as X:
    with B() as Y:
        with C() as Z:
             # with-body code here
'''