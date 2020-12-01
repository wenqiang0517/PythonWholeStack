# 万能参数： *args，约定俗称：args
# 函数定义时，*代表聚合。他将所有的位置参数聚合成一个元组，赋值给了 args。

"""
def eat(*args):
    print(args)
    print('我请你吃：%s %s %s %s' % (args))
eat('蒸羊羔','蒸熊掌','蒸鹿尾儿','烧花鸭')
"""

# 写一个函数，计算你传入函数的所有的数字的和
# def func(*args):
#     count = 0
#     for i in args:
#         count += i
#     print(count)
# func(1,2,3,4,5)

# **kwargs
# 函数的定义时：** 将所有的关键字参数聚合到一个字典中，将这个字典赋值给了kwargs
# def func(**kwargs):
#     print(kwargs)
# func(name='lwq', age=18, sex='男')

# 万能参数： *args **kwargs
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# func()

"""
# * **在函数的调用时，*代表打散。
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(*[1, 2, 3], *[22, 33])    # func(1, 2, 3, 22, 33)
func(*'abc', *'123')    # func(1, 2, 3, 22, 33)
func(**{'name': 'lwq'}, **{'age': 18})   # func(name='lwq', age=18)
"""


# 形参角度的参数的顺序
# *args 的位置
# def func(*args, a, b, sex='男'):
#     print(a, b)
# func(1, 2, 3, 4)

# args得到实参的前提，sex必须被覆盖了
# def func(a, b, sex='男', *args):
#     print(a, b)
#     print(sex)
#     print(args)
# func(1, 2, 3, 4, 5, 6, 7)

"""
def func(a, b, *args, sex='男'):
    print(a, b)
    print(sex)
    print(args)
func(1, 2, 3, 4, 5, 6, 7, sex='女')
"""

# **kwargs 位置
# def func(a, b, *args, sex='男', **kwargs):
#     print(a, b)
#     print(sex)
#     print(args)
#     print(kwargs)
# func(1, 2, 3, 4, 5, 6, 7, sex='女', name='lwq', age=19)

# 形参角度第四个参数：仅限关键字参数
def func(a, b, *args, sex='男', c, **kwargs):
    print(a, b)
    print(sex)
    print(args)
    print(kwargs)
    print(c)
func(1, 2, 3, 4, 5, 6, 7, sex='女', name='lwq', age=19, c=99)

# 形参角度最终的顺序：位置参数，*args，默认参数，仅限关键字参数，**kwargs
