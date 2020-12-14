# 3，看代码写结果
# def wrapper(f):
#     def inner(*args, **kwargs):
#         print(111)
#         ret = f(*args, **kwargs)
#         print(222)
#         return ret
#     return inner
#
# @wrapper    # func = wrapper(func)
# def func():
#     print(333)
# print(444)
# func()
# print(555)
# 444 111 333 222 555

# 4，编写装饰器,在每次执行被装饰函数之前打印一句'每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码'。
# def wrapper(f):
#     def inner(*args, **kwargs):
#         print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
#         ret = f()
#         return ret
#     return inner
#
# @wrapper    # func = wrapper(func)
# def func(*args, **kwargs):
#     print('被装饰函数')
#     return True
# ret = func()
# print(ret)

# 5，为函数写一个装饰器，把函数的返回值 +100 然后再返回。
# def wrapper(f):
#     def inner():
#         ret = f()
#         return ret+100
#     return inner
#
# @wrapper
# def func():
#     return 7
# result = func()
# print(result)

# 6，请实现一个装饰器，通过一次调用是函数重复执行5次。
# def wrapper(f):
#     def inner():
#         for i in range(5):
#             f()
#     return inner
#
# @wrapper
# def func():
#     print('1')
#
# func()

# 7，请实现一个装饰器，每次调用函数时，将函数名以及调用此函数的时间节点写入文件中。
# 可用代码：     # 函数名通过： 函数名.__name__获取。
import time


def wrapper(f):
    def inner(*args, **kwargs):
        struct_time = time.localtime()
        ret = f(*args, **kwargs)
        with open('test', encoding='utf-8', mode='a') as f1:
            f1.write(f'{time.strftime("%Y-%m-%d %H:%M:%S", struct_time)} {f.__name__} \n')
        return ret
    return inner


@wrapper    # func1 = wrapper(func1)
def func1(*args, **kwargs):
    print('abc')
    time.sleep(2)
    return True


ret = func1()
print(ret)

