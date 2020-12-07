# 2,用列表推导式做下列题目
# 3，过滤掉长度小于3的字符串列表，病将剩下的转换成大写字母 ------
# 4，求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元组列表
# l1 = []
# for i in range(6):
#     for x in range(6):
#         l1.append((i, x))
# print(l1)
# print([(i, x) for i in range(6) for x in range(6)])

# 5，求M中3,6,9组成的列表
# M = [[1,2,3],[4,5,6],[7,8,9]]
# for i in M:
#     for x in i:
#         if x in [3,6,9]:
#             print(i)

# 6,求出50以内能被3整除的数的平方，并放入到一个列表中
# print([i for i in range(1, 51) if i % 3 == 0])

# 7，构建一个列表：['python1期','python2期'....'python10期']
# print([f'python{i}期' for i in range(1, 11)])

# 8，构建一个列表：[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6)]    ********************
print([(i, i+1) for i in range(6)])

# 9，构建一个列表：[0,2,4,6,8,10,12,14,16,18]
# print([i for i in range(0, 19, 2)])

# 10，有一个列表l1 = ['alex','WuSir','老男孩','太白']将其构造成这种列表['alex0','WuSir1','老男孩2','太白3']
# l1 = ['alex','WuSir','老男孩','太白']
# for index in range(len(l1)):
#     l1[index] += str(index)
# print(l1)

# 11，有一下数据类型
x = {'name': 'alex',
     'Values': [{'timestamp': 1517991992.94, 'values': 100,},
                {'timestamp': 1517992000.94, 'values': 200,},
                {'timestamp': 1517992014.94, 'values': 300,},
                {'timestamp': 1517992744.94, 'values': 350,},
                {'timestamp': 1517992800.94, 'values': 280,}],}
# 将上面的数据通过列表推导式转换成下面的类型：
# [[1517991992.94, 100], [1517992000.94, 200], [1517992014.94, 300], [1517992744.94, 350], [1517992800.94, 280]]
# l1 = []
# for i in x['Values']:
#     l1.append(list(i.values()))
# print(l1)
print([list(i.values()) for i in x['Values']])

# 12，用列表完成笛卡尔积
# 笛卡尔积就是一个列表，列表里面的元素是由输入的可迭代类型的元素对构成的元组，因此笛卡尔积列表的长度等于输入变量的长度的乘积
# a，构建一个列表，列表里面是三种不同尺寸的T恤衫，每个尺寸都有两个颜色(列表里面的元素为元组类型)
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
print([(i, x) for i in colors for x in sizes])

# b，构建一个列表，列表里面的元素是扑克牌出去大小王以后，所有的牌类(列表里面的元素为元组类型)
# l1 = [('A', 'spades'), ('A', 'diamonds'), ('A', 'clubs'), ('A', 'hearts')...('K', 'spades')]
# l1 = []
# for i in (list('A') + [i for i in range(2, 11)] + list('JQK')):
#     for x in ['spades', 'diamonds', 'clubs', 'hearts']:
#         l1.append((i, x))
# print(l1)
print([(i, x) for i in (list('A') + [i for i in range(2, 11)] + list('JQK')) for x in ['spades', 'diamonds', 'clubs', 'hearts']])
# 13，简述一下yield与yield from 的区别

# 14，看下面代码，能否对其简化以及简化后的优点
# def chain(*iterables):
#     for it in iterables:
#         yield from it
#         # for i in it:
#         #     yield i
# g = chain('abc', (0,1,2))
# print(list(g))      # 将迭代器转化成列表
# 只要循环就耗费时间，时间复杂度，优化了内层循环，提高效率

# 15，看代码写结果
"""
v = [i % 2 for i in range(10)]
print(v)
# [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

v = (i % 2 for i in range(10))
print(v)
# <generator object <genexpr> at 0x000000B9ACE1A740>

# for i in range(5):
#     print(i)
# print(i)
# 0 1 2 3 4 5 5
"""

# 16，看代码写结果 ******************
"""
def demo():
    for i in range(4):
        yield i
g = demo()
g1 = (i for i in g)
g2 = (i for i in g1)
print(g)
# <generator object demo at 0x000000DEC820A970>
print(g1)
# <generator object <genexpr> at 0x0000006F99F6A7B0>
print(g2)
# <generator object <genexpr> at 0x0000006F99F6A7B0>
print(list(g1))
# [0, 1, 2, 3]
print(list(g2))
# []
"""

# 17，看代码写结果
def add(n, i):
    return n+i
def test():
    for i in range(4):
        yield i
g = test()
for n in [1, 10]:
    g = (add(n, i) for i in g)
print(list(g))

# [20, 21, 22, 23]




