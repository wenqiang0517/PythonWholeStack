# 封闭的东西：保证数据的安全


def make_averager():
    l1 = []
    def averager(new_value):
        l1.append(new_value)
        total = sum(l1)
        return total / len(l1)
    return averager


avg = make_averager()   # averager
print(avg(100000))
print(avg(110000))
print(avg(120000))


# 闭包：   什么是闭包？ 闭包有什么作用？
#     1，闭包只能存在嵌套函数中。
#     2，内层函数对外层函数非全局变量的引用(使用)，就会形成闭包
# 被引用的非全局变量也称作自由变量，这个自由变量会与内层函数产生一个绑定关系
# 自由变量不会再内存中消失
# 闭包的作用：保证数据的安全

"""
# 判断是不是闭包
# 例一：是
def wrapper():
    a = 1
    def inner():
        print(a)
    return inner
ret = wrapper()

# 例二： 不是
a = 2
def wrapper():
    def inner():
        print(a)
    return inner
ret = wrapper()

# 例三： 也是闭包
def wrapper(a, b):
    # a = 2
    # b = 3
    def inner():
        print(a)
        print(b)
    return inner
a = 2
b = 3
ret = wrapper(a, b)
"""

# 如何代码判断闭包
# 函数名.__code__.co_freevars 查看函数的自由变量
print(avg.__code__.co_freevars)  # ('series',)

