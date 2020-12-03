# 1，写出代码的执行结果
# def func1():
#     print(**'in func1'**)
#
# def func2():
#     print(**'in func2'**)
#
# ret = func1
# ret()
# ret1 = func2
# ret1()
# ret2 = ret
# ret3 = ret2
# ret2()
# ret3()
# 结果：
#
# def func1():
#     print(**'in func1'**)
#
# def func2():
#     print(**'in func2'**)
#
# def func3(x, y):
#     x()
#     print(**'in func3'**)
#     y()
#
# print(111)
# func3(func2, func1)
# print(222)
# 结果：
#
# def func1():
#     print(**'in func1'**)
#
# def func2(x):
#     print(**'in func2'**)
#     return x
#
# def func3(y):
#     print(**'in func3'**)
#     return y
#
# ret = func2(func1)
# ret()
# ret2 = func3(func2)
# ret3 = ret2(func1)
# ret3()
# 结果：
#
# 2,写出代码的执行结果
# def func(arg):
#     return arg.replace('苍老师', '***')
#
# def run():
#     msg = 'Alex的女朋友苍老师和大家都是好朋友'
#     result = func(msg)
#     print(result)
#
# data = run()
# print(data)
#
# 3,
# DATA_LIST = []
# def func(arg):
#     return DATA_LIST.insert(0, arg)
#
# data = func('绕不死你')
# print(data)
# print(DATA_LIST)
#
# 4,
# def func():
#     print('你好呀')
#     return '好你妹呀'
#
# func_list = [func, func, func]
# for item in func_list:
#     val = item()
#     print(val)
#
# 5,
# def func():
#     print('你好呀')
#     return '好你妹呀'
#
# func_list = [func, func, func]
# for i in range(len(func_list)):
#     val = func_list[i]()
#     print(val)
#
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
#
# 7,
# for item in range(10):
#     print(item)
# print(item)
#
# 8,
# def func():
#     for item in range(10):
#         pass
#     print(item)
# func()
#
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
#
# 10,
# l1 = []
# def func(args):
#     l1.append(args)
#     return l1
#
# print(func(1))
# print(func(2))
# print(func(3))
#
# 11,
# name = '太白'
# def func():
#     global name
#     name = '男神'
# print(name)
# func()
# print(name)
#
# 12,
# name = '太白'
# def func():
#     print(name)
# func()
#
# 13,
# name = '太白'
# def func():
#     print(name)
#     name = 'alex'
# func()
#
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
#
# 15,
# def extendlist(val, list=[]):
#     list.append(val)
#     return list
# list1 = extendlist(10)
# list2 = extendlist(123, [])
# list3 = extendlist('a')
# print('list1=%s' % list1)
# print('list2=%s' % list2)
# print('list3=%s' % list3)
#
#
# 16,
# def extendlist(val, list=[]):
#     list.append(val)
#     return list
# print('list1=%s' % extendlist(10))
# print('list2=%s' % extendlist(123, []))
# print('list3=%s' % extendlist('a'))
#
#
# 17,用你的理解解释一下什么是可迭代对象，什么是迭代器
#
# 18,如何判断该对象是否是可迭代对象或者迭代器
#
# 19，写代码，用while循环模拟for内部的循环机制
#
# 20，写函数，传入n个数，返回字典 {'max': 最大值, 'min': '最小值'}
# 例如 min_max(2,5,7,8,4) 返回 {'max': 8, 'min': 2}  用到max() min() 内置函数
#
# 21,写函数，传入n个数，返回n的阶乘，例如cal(7) 计算7654321
#
# 22，写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组，例如 [('红心', 2),('草花', 2),....('黑桃', A)]
#
# 23, 写代码完成99乘法表
# 1 * 1 = 1
# 2 * 1 = 2 2 * 2 = 4
# 3 * 1 = 3 3 * 2 = 6 3 * 3 = 9
# 。。。
# 。。。。。
#
#
#
#
