# 生成器函数
# def func():
#     print(111)
#     print(222)
#     yield 3
#     print(444)
#     yield 4
# ret = func()
# print(next(ret))
# print(next(ret))
# print(next(ret))

# return yield
# return：函数中只存在一个return结束函数，并且给函数的执行者返回值
# yield：只要函数中有yield那么他就是生成器函数而不是函数了
# 生成器函数中可以存在多个yield，yield不会结束生成器函数，一个yield对应一个next

# 吃包子
"""
def func():
    l1 = []
    for i in range(1, 5001):
        l1.append(f'{i}号包子')
    return l1
ret = func()
print(ret)
"""

# def gen_func():
#     for i in range(1, 5001):
#         yield f'{i}号包子'
# ret = gen_func()
# for i in range(200):
#     print(next(ret))
# for i in range(200):
#     print(next(ret))


# yield from
"""
def func():
    l1 = [1, 2, 3, 4, 5]
    yield l1
ret = func()
print(next(ret))

def func():
    l1 = [1, 2, 3, 4, 5]
    # 将l1这个列表变成迭代器返回
    yield from l1
ret = func()
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))
"""


def func():
    lst1 = ['卫龙', '老冰棍', '北冰洋', '牛羊配']
    lst2 = ['馒头', '花卷', '豆包', '大饼']
    yield from lst1
    yield from lst2
g = func()
for i in g:
    print(i)
'''
yield from ['卫龙','老冰棍','北冰洋','牛羊配'] 
等同于：
    yield '卫龙'
    yield '老冰棍'
    yield '北冰洋'
    yield '牛羊配'
'''

