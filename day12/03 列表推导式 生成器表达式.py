# 用一行代码构建一个比较复杂有规律的列表
# l1 = []
# for i in range(1, 11):
#     l1.append(i)
# print(l1)

# 列表推导式
# l1 = [i for i in range(1, 11)]
# print(l1)

# 列表推导式分两类
# 循环模式：[变量(加工的变量) for 变量 in iterable]
"""
# 将10以内所有整数的平方写入列表。
l1 = [i**2 for i in range(1, 11)]
print(l1)

# 100以内所有的偶数写入列表.
l1 = [i for i in range(0, 101, 2)]
print(l1)

# 从python1期到python100期写入列表lst
l1 = [f'python{i}期' for i in range(1, 101)]
print(l1)
"""

# 筛选模式: [变量(加工的变量) for 变量 in iterable if 条件]
"""
# 三十以内可以被三整除的数
l1 = [i for i in range(1, 31) if i % 3 == 0]
print(l1)

# 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
l1 = ['wusir', 'laonanhai', 'aa', 'b', 'taibai']
l2 = [i.upper() for i in l1 if len(i) >= 3]
print(l2)

# 含有两个‘e’的所有名字留下来
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
l1 = [name for i in names for name in i if name.count('e') == 2]
print(l1)
"""
# 列表推导式
#     缺点：
#         1，有毒，列表推导式只能构建比较复杂并且有规律的列表。
#         2，超过三层循环才能构建成功的，不建议用列表推导式
#         3，查找错误(debug模式)不行
#     优点：
#         1，一行构建，简单
#         2，装逼


# 生成器表达式
# 生成器表达式和列表推导式的语法上几乎一模一样,也有筛选模式、循环模式
# [] 换成 ()
# l1 = (i for i in range(1, 11))
# print(l1)
# print(next(l1))
# print(next(l1))
# for i in l1:
#     print(i)

# 构建一个列表：[2,3,4,5,5,6,7,8,9,10,'J','Q','K','A']
l1 = [i for i in range(2, 11)] + list('JQKA')
print(l1)

# 生成器表达式和列表推导式的区别:
#     1, 列表推导式比较耗内存,所有数据一次性加载到内存。而.生成器表达式遵循迭代器协议，逐个产生元素
#     2, 得到的值不一样,列表推导式得到的是一个列表.生成器表达式获取的是一个生成器
#     3, 列表推导式一目了然，生成器表达式只是一个内存地址
# 写法上： [] ()
# iterable    iterator

# 字典推导式（了解）
lst1 = ['jay', 'jj', 'meet']
lst2 = ['周杰伦', '林俊杰', '郭宝元']
dic = {lst1[i]: lst2[i] for i in range(len(lst1))}
print(dic)

# 集合推导式（了解）
print({i for i in range(1, 11)})

