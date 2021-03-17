import time


def logger(path):
    def log(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            with open(path, mode='a', encoding='utf-8') as f:
                msg = '%s 执行了 %s' % (time.strftime('%Y-%m-%d %X'), func.__name__)
                f.write(msg)
            return ret
        return inner
    return log


@logger('auth.log')
def login():
    print("登陆的逻辑")


@logger('auth.log')
def register():
    print("注册的逻辑")


@logger('auth.log')
def show_goods():
    print("查看所有商品信息")


@logger('operate.log')
def add_goods():
    print("商品加入购物车")


login()
add_goods()

# 带参数的装饰器
# 有100个函数，分别添加一个计算函数执行时间的装饰器
# 有的时候需要计算时间，有的时候不需要
# 希望能通过修改一个变量，能控制这100个函数的装饰器是否执行

# import time
#
#
# def run_time(flag):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             start_time = time.time()
#             ret = func(*args, **kwargs)
#             end_time = time.time()
#             if flag:
#                 print(end_time - start_time)
#             return ret
#
#         return inner
#
#     return wrapper
#
#
# @run_time(True)
# def a():
#     time.sleep(1)
#
#
# @run_time(True)
# def b():
#     time.sleep(2)
#
#
# @run_time(False)
# def c():
#     time.sleep(3)
#
#
# a()
# b()
# c()
