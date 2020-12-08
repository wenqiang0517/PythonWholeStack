# eval：剥去字符串的外衣运算里面的代码
s1 = '1 + 3'
print(s1)
print(eval(s1))
s = '{"name": "alex"}'
print(s, type(s))
print(eval(s), type(eval(s)))
# 网络传输的str input输入的时候，sql注入等绝对不能使用evel

# exec 与evel几乎一样，代码流
s = '''
for i in [1,2,3]:
    print(i)
'''
exec(s)

# hash 哈希值
print(hash('adsdsa'))

# help 帮助
# print(help(list))
# print(help(str.split))

# callable 判断一个对象是否可被调用
name = 'alex'


def func():
    pass


print(callable(name))  # False
print(callable(func))  # True

# int：函数用于将一个字符串或数字转换为整型
print(int())  # 0
print(int('12'))  # 12
print(int(3.6))  # 3
print(int('0100', base=2))  # 将2进制的 0100 转化成十进制。结果为 4

# float：函数用于将整数和字符串转换成浮点数。
# complex：函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
print(float(3))  # 3.0
print(complex(1, 2))  # (1+2j)

# bin：将十进制转换成二进制并返回。
# oct：将十进制转化成八进制字符串并返回。
# hex：将十进制转化成十六进制字符串并返回
print(bin(10), type(bin(10)))  # 0b1010 <class 'str'>
print(oct(10), type(oct(10)))  # 0o12 <class 'str'>
print(hex(10), type(hex(10)))  # 0xa <class 'str'>

# divmod：计算除数与被除数的结果，返回一个包含商和余数的元组(a // b, a % b)。
# round：保留浮点数的小数位数，默认保留整数。
# pow：求x**y次幂。（三个参数为x**y的结果对z取余）
print(divmod(7, 2))  # (3, 1)
print(round(7 / 3, 2))  # 2.33
print(round(7 / 3))  # 2
print(round(3.32567, 3))  # 3.326
print(pow(2, 3))  # 两个参数为2**3次幂
print(pow(2, 3, 3))  # 三个参数为2**3次幂，对3取余。

# bytes：用于不同编码之间的转化
# s = '你好'
# bs = s.encode('utf-8')
# print(bs)
# s1 = bs.decode('utf-8')
# print(s1)
# bs = bytes(s,encoding='utf-8')
# print(bs)
# b = '你好'.encode('gbk')
# b1 = b.decode('gbk')
# print(b1.encode('utf-8'))

# ord:输入字符找该字符编码的位置
# chr:输入位置数字找出其对应的字符
print(ord('a'))
print(ord('中'))
print(chr(97))
print(chr(20013))

# repr:返回一个对象的string形式（原形毕露）
# %r  原封不动的写出来
# name = 'taibai'
# print('我叫%r'%name)

# repr 原形毕露
print(repr('{"name":"alex"}'))
print('{"name":"alex"}')

# all：可迭代对象中，全都是True才是True
# any：可迭代对象中，有一个True 就是True
print(all([1, 2, True, 0]))
print(any([1, '', 0]))

# print() 屏幕输出
''' 源码分析
def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    file:  默认是输出到屏幕，如果设置为文件句柄，输出到文件
    sep:   打印多个值之间的分隔符，默认为空格
    end:   每一次打印的结尾，默认为换行符
    flush: 立即把内容输出到流文件，不作缓存
    """
'''
print(111, 222, 333, sep='*')  # 111*222*333
print(111, end='')
print(222)  # 两行的结果 111222
# f = open('log', 'w', encoding='utf-8')
# print('写入文件', fle=f, flush=True)

# int():pass
# str():pass
# bool():pass
# set(): pass
# list() 将一个可迭代对象转换成列表
# tuple() 将一个可迭代对象转换成元组
# dict() 通过相应的方式创建字典
# 创建字典的几种方式
# 直接创建
# dic = dict([(1, 'one'), (2, 'two'), (3, 'three')])
# dic = dict(one=1, two=2)
# print(dic)
# fromkeys
# update
# 字典推导式

l1 = list('abcd')
print(l1)  # ['a', 'b', 'c', 'd']
tu1 = tuple('abcd')
print(tu1)  # ('a', 'b', 'c', 'd')

# abs() 返回绝对值   ***
i = -5
print(abs(i))  # 5

# sum() 求和 ***
l1 = [i for i in range(10)]
print(sum(l1))
print(sum([1, 2, 3]))
print(sum((1, 2, 3), 100))

# reversed() 将一个序列翻转, 返回翻转序列的迭代器  ***
l = reversed('你好')  # l 获取到的是一个生成器
print(list(l))
ret = reversed([1, 4, 3, 7, 9])
print(ret, list(ret))  # <list_reverseiterator object at 0x7fd8cf7d1a30> [9, 7, 3, 4, 1]

# zip() *** 拉链方法。函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组,
# 然后返回由这些元祖组成的内容,如果各个迭代器的元素个数不一致,则按照长度最短的返回
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c', 'd']
lst3 = (11, 12, 13, 14, 15)
for i in zip(lst1, lst2, lst3):
    print(i)
# (1, 'a', 11)
# (2, 'b', 12)
# (3, 'c', 13)

# ********************************
# min() 求最小值
print(min([1, 2, 3]))  # 返回此序列最小值
ret = min([1, 2, -5, ], key=abs)  # 按照绝对值的大小，返回此序列最小值
print(ret)
# 加key是可以加函数名，min自动会获取传入函数中的参数的每个元素，然后通过你设定的返回值比较大小，返回最小的传入的那个参数。
print(min(1, 2, -5, 6, -3, key=lambda x: abs(x)))  # 可以设置很多参数比较大小

# x为dic的key，lambda的返回值（即dic的值进行比较）返回最小的值对应的键
dic = {'a': 3, 'b': 2, 'c': 1}
print(min(dic, key=lambda x: dic[x]))

l2 = [('太白', 18), ('alex', 73), ('wusir', 35), ('口天吴', 41)]
print(min(l2, key=lambda x: x[1]))
print(min(l2, key=lambda x: x[1])[0])
# print(min(l2, key=lambda x: dict(l2).keys()))

# max() 最大值与最小值用法相同

# sorted 排序函数
l1 = [22, 33, 1, 2, 8, 7, 6, 5]
l2 = sorted(l1)
print(l1)
print(l2)

lst = [{'id': 1, 'name': 'alex', 'age': 18},
       {'id': 2, 'name': 'wusir', 'age': 17},
       {'id': 3, 'name': 'taibai', 'age': 16}, ]
print(sorted(lst, key=lambda e: e['age']))  # 返回一个列表，默认从低到高
print(sorted(lst, key=lambda e: e['age'], reverse=True))  # 返回一个列表，默认从高到低

# filter 列表推导式的筛选模式
l1 = [2, 3, 4, 5, 6, 7, 8]
print([i for i in l1 if i > 3])
ret = filter(lambda x: x > 3, l1)
print(ret)
print(list(ret))

# map 列表推导式的循环模式
l1 = [1, 4, 9, 16, 25]
print([i ** 2 for i in range(1, 6)])
ret = map(lambda x: x ** 2, range(1, 6))
print(ret)
print(list(ret))

# reduce
# reduce 的使用方式:
# reduce(函数名,可迭代对象)  # 这两个参数必须都要有,缺一个不行
# reduce的作用是先把列表中的前俩个元素取出计算出一个值然后临时保存着,
# 接下来用这个临时保存的值和列表中第三个元素进行计算,求出一个新的值将最开始
# 临时保存的值覆盖掉,然后在用这个新的临时值和列表中第四个元素计算.依次类推
from functools import reduce
def func(x, y):
    return x + y


ret = reduce(func, [3, 4, 5, 6, 7])
print(ret)  # 结果 25

