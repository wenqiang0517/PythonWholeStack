import sys

# sys.setrecursionlimit(100000000)
count = 0


# def func():
#     global count
#     count += 1
#     print(count)
#     func()
#     print(456)
#
#
# func()


# RecursionError
# 递归的最大深度1000层 : 为了节省内存空间,不要让用户无限使用内存空间
# 1.递归要尽量控制次数,如果需要很多层递归才能解决问题,不适合用递归解决
# 2.循环和递归的关系
    # 递归不是万能的
    # 递归比起循环来说更占用内存
# 修改递归的最大深度
    # import sys
    # sys.setrecursionlimit(1000000000)


# 你的递归函数 必须要停下来
# 递归函数是怎么停下来的?递归3次结束整个函数
# count = 0
# def func():        # func1
#     global count
#     count += 1     # 1
#     print(count)
#     if count == 3: return
#     func()
#     print(456)
# func()
#
# def func():        # func2
#     global count
#     count += 1     # 2
#     print(count)
#     if count == 3: return
#     func()
#     print(456)
#
#
# def func():        # func3
#     global count
#     count += 1     # 3
#     print(count)
#     if count == 3:return
#     func()
#     print(456)


# 一个递归函数要想结束,必须在函数内写一个return,并且return的条件必须是一个可达到的条件
# 并不是函数中有return,return的结果就一定能够在调用函数的外层接收到
# def func(count):
#     count += 1
#     print(count)
#     if count == 5 : return 5
#     ret = func(count)
#     print(count ,':',ret)
#     return ret
# print('-->',func(1))

# def func(1):
#     1 += 1
#     print(2)
#     if 2 == 5 : return 5
#     ret = func(2)
#     print(ret)
#     return ret
#
# def func(2):
#     2 += 1
#     print(3)
#     if 3 == 5 : return 5
#     ret = func(3)
#     print(ret)
#     return ret
#
# def func(3):
#     3 += 1
#     print(4)
#     if 4 == 5 : return 5
#     ret = func(4)
#     print(ret)
#     return ret
#
# def func(4):
#     4 += 1
#     print(5)
#     if 5 == 5 : return 5
#     func(count)
#

# def func(count):
#     count += 1
#     print(count)
#     if count == 5 : return 5
#     return func(count)
# print('-->',func(1))

