# 1，写出代码的执行结果
# def func1():
#     print('in func1')
# def func2():
#     print('in func2')
# ret = func1
# ret()
# ret1 = func2
# ret1()
# ret2 = ret
# ret3 = ret2
# ret2()
# ret3()
# 'in func1'
# 'in func2'
# 'in func1'
# 'in func1'

# def func1():
#     print('in func1')
# def func2():
#     print('in func2')
# def func3(x, y):
#     x()
#     print('in func3')
#     y()
# print(111)
# func3(func2, func1)
# print(222)
# 111
# 'in func2'
# 'in func3'
# 'in func1'
# 222

# def func1():
#     print('in func1')
# def func2(x):
#     print('in func2')
#     return x
# def func3(y):
#     print('in func3')
#     return y
# ret = func2(func1)
# ret()
# ret2 = func3(func2)
# ret3 = ret2(func1)
# ret3()
# 'in func2'
# 'in func1'
# 'in func3'
# 'in func2'
# 'in func1'

# 2,写出代码的执行结果
# def func(arg):
#     return arg.replace('苍老师', '***')
# def run():
#     msg = 'Alex的女朋友苍老师和大家都是好朋友'
#     result = func(msg)
#     print(result)
# data = run()
# print(data)
# 'Alex的女朋友***和大家都是好朋友'
# None

# 3,
"""
DATA_LIST = []
def func(arg):
    return DATA_LIST.insert(0, arg)
data = func('绕不死你')
print(data)
print(DATA_LIST)
# None      DATA_LIST.insert(0, arg) 是个插入的动作，没有返回值，所以是None
# ['绕不死你']
"""

# 4,
# def func():
#     print('你好呀')
#     return '好你妹呀'
# func_list = [func, func, func]
# for item in func_list:
#     val = item()
#     print(val)
# '你好呀'
# '好你妹呀'
# '你好呀'
# '好你妹呀'
# '你好呀'
# '好你妹呀'

# 5,
# def func():
#     print('你好呀')
#     return '好你妹呀'
# func_list = [func, func, func]
# for i in range(len(func_list)):
#     val = func_list[i]()
#     print(val)
# '你好呀'
# '好你妹呀'
# '你好呀'
# '好你妹呀'
# '你好呀'
# '好你妹呀'

# 6,
# def func():
#     return '烧饼'
#
# def bar():
#     return '豆饼'
#
# def base(a1, a2):
#     return a1() + a2()
#
# result = base(func, bar)
# print(result)
# '烧饼豆饼'

# 7,
"""
for item in range(10):
    print(item)
print(item)
# 0 1 2 3 4 5 6 7 8 9
# 9
"""

# 8,
# def func():
#     for item in range(10):
#         pass
#     print(item)
# func()
# 9

# 9,
# item = '老男孩'
# def func():
#     item = 'alex'
#     def inner():
#         print(item)
#     for item in range(10):
#         pass
#     inner()
# func()
# 9

# 10,
# l1 = []
# def func(args):
#     l1.append(args)
#     return l1
#
# print(func(1))
# print(func(2))
# print(func(3))
# [1]
# [1, 2]
# [1, 2, 3]

# 11,
# name = '太白'
# def func():
#     global name
#     name = '男神'
# print(name)
# func()
# print(name)
# '太白'
# '男神'

# 12,
# name = '太白'
# def func():
#     print(name)
# func()
# '太白'

# 13,
# name = '太白'
# def func():
#     print(name)
#     name = 'alex'
# func()
# error
# UnboundLocalError: local variable 'name' referenced before assignment

# 14,
# def func():
#     count = 1
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#     print(count)
#     inner()
#     print(count)
# func()
# 1
# 2
# 2

# 15,
"""
def extendlist(val, list=[]):
    list.append(val)
    return list
list1 = extendlist(10)
list2 = extendlist(123, [])
list3 = extendlist('a')
print('list1=%s' % list1)
print('list2=%s' % list2)
print('list3=%s' % list3)
# 'list1=[10, 'a']'
# 'list2=[123]'
# 'list3=[10, 'a']'
"""

# 16,
# def extendlist(val, list=[]):
#     list.append(val)
#     return list
# print('list1=%s' % extendlist(10))
# print('list2=%s' % extendlist(123, []))
# print('list3=%s' % extendlist('a'))
# 'list1=[10]'
# 'list2=[123]'
# 'list3=[10, 'a']'

# 17,用你的理解解释一下什么是可迭代对象，什么是迭代器
#
#
# 18,如何判断该对象是否是可迭代对象或者迭代器
# __iter__
# __iter__ and __next__
# 19，写代码，用while循环模拟for内部的循环机制

# 20，写函数，传入n个数，返回字典 {'max': 最大值, 'min': '最小值'}
# 例如 min_max(2,5,7,8,4) 返回 {'max': 8, 'min': 2}  用到max() min() 内置函数
# def min_max(*args):
#     print({'max': max(args), 'min': min(args)})
# min_max(2,5,7,8,4)
# 21,写函数，传入n个数，返回n的阶乘，例如cal(7) 计算7654321
# def func(n):
#     obj = iter(range(n, 0, -1))
#     num_1 = next(obj)
#     for i in range(n-1):
#         num_1 *= next(obj)
#     print(num_1)
# func(7)

# 22，写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组，例如 [('红心', 2),('草花', 2),....('黑桃', A)]
# def func():
#     l = []
#     for i in ['红心', '梅花', '方块', '黑桃']:
#         for x in [2,3,4,5,5,6,7,8,9,10,'J','Q','K','A']:
#             # t = (i, x)
#             l.append((i, x))
#     print(l)
# func()

# 23, 写代码完成99乘法表
# 1 * 1 = 1
# 2 * 1 = 2 2 * 2 = 4
# 3 * 1 = 3 3 * 2 = 6 3 * 3 = 9
def func():
    for i in range(1, 10):
        for x in range(1, i+1):
            print(f'{x} * {i} = {i * x} \t', end='')
        print()
func()
