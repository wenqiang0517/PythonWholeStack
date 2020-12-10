# 开放封闭原则
# 开放：对代码的拓展开放的
# 封闭：对源码的修改是封闭的

# 装饰器：完全遵循开放封闭原则
# 装饰器：在不改变原函数的代码以及调用方式的前提下，为其增加新的功能
# 装饰器其实就是一个闭包函数

import time
# 原始版本
"""
def index():
    time.sleep(2)
    print('欢迎登陆博客园首页')

def timmer(f):
    def inner():
        start_time = time.time()
        f()
        end_time = time.time()
        print(f'执行效率{end_time-start_time}')
    return inner

index = timmer(index)
index()
"""

# 装饰器
"""
def timmer(f):
    def inner():
        start_time = time.time()
        f()
        end_time = time.time()
        print(f'执行效率{end_time-start_time}')
    return inner


@timmer     # index = timmer(index)
def index():
    time.sleep(2)
    print('欢迎登陆博客园首页')

index()
"""

# 被装饰函数带返回值
"""
def timmer(f):
    def inner():
        start_time = time.time()
        r = f()
        end_time = time.time()
        print(f'执行效率{end_time-start_time}')
        return r
    return inner


@timmer     # index = timmer(index)
def index():
    time.sleep(1)
    print('欢迎登陆博客园首页')
    return 666
# 加上装饰器不应该改变原函数的返回值，所以666应该返回给我下面的ret
# 但是下面的这个ret实际接收的是inner函数的返回值，而666返回给的是装饰器里面的
# f() 也就是r，我们现在要解决的问题就是将r给inner的返回值
r = index()
print(r)
"""

# 被装饰函数带参数
def timmer(f):
    def inner(*args, **kwargs):
        start_time = time.time()
        r = f(*args, **kwargs)
        end_time = time.time()
        print(f'执行效率{end_time-start_time}')
        return r
    return inner

@timmer
def index(name, age):
    time.sleep(1)
    print(f'欢迎{name}登陆博客园首页{age}')
    return 666
r = index('lwq', 11111)
print(r)


# 标准版装饰器
def wrapper(func):
    def inner(*args, **kwargs):
        """添加额外的功能，执行被装饰函数之前的操作"""
        ret = func(*args, **kwargs)
        '''添加额外的功能，执行被装饰函数之后的操作'''
        return ret
    return inner

