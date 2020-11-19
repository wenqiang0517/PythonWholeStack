# str
# captalize,swapcase,title
name = 'taiBAi'
print(name.capitalize())  # 首字母大写
print(name.swapcase())  # 大小写翻转
msg = 'taibai say hi'
print(msg.title())  # 每个单词的首字母大写

# 内同居中，总长度，空白处填充
a1 = 'abc'
ret2 = a1.center(20, "*")
print(ret2)

# 寻找字符串中的元素是否存在
# ret6 = a4.find("fjdk",1,6)
# print(ret6)  # 返回的找到的元素的索引，如果找不到返回-1

# ret61 = a4.index("fjdk",4,6)
# print(ret61) # 返回的找到的元素的索引，找不到报错。

# tuple
# 元组中如果只含有一个元素且没有逗号，则该元组不是元组，与改元素数据类型一致，如果有逗号，那么它是元组
tu = (1)
print(tu, type(tu))  # 1 <class 'int'>
tu1 = ('alex')
print(tu1, type(tu1))  # 'alex' <class 'str'>
tu2 = ([1, 2, 3])
print(tu2, type(tu2))  # [1, 2, 3] <class 'list'>

tu = (1,)
print(tu, type(tu))  # (1,) <class 'tuple'>
tu1 = ('alex',)
print(tu1, type(tu1))  # ('alex',) <class 'tuple'>
tu2 = ([1, 2, 3],)
print(tu2, type(tu2))  # ([1, 2, 3],) <class 'tuple'>

# index：通过元素找索引（可切片），找到第一个元素就返回，找不到该元素即报错
tu = ('太白', [1, 2, 3, ], 'WuSir', '女神')
print(tu.index('太白'))  # 0

# count: 获取某元素在列表中出现的次数
tu = ('太白', '太白', 'WuSir', '吴超')
print(tu.count('太白'))  # 2

# list
# count（数）（方法统计某个元素在列表中出现的次数）
a = ["q", "w", "q", "r", "t", "y"]
print(a.count("q"))

# index（方法用于从列表中找出某个值第一个匹配项的索引位置）
a = ["q", "w", "r", "t", "y"]
print(a.index("r"))

# sort （方法用于在原位置对列表进行排序） **
# reverse （方法将列表中的元素反向存放）
l1 = [5, 4, 3, 7, 8, 9, 1]
l1.sort()  # 默认从小到大排序
l1.sort(reverse=True)  # 从大到小排序
l1.reverse()  # 反转
print(l1)

# 列表可以相加
l1 = [1, 2, 3]
l2 = [1, 2, 3, '太白', '123', '女神']
print(l1 + l2)

# 列表与数字相乘
l1 = [1, 'daf', 3]
l2 = l1 * 3
print(l2)

# 在循环一个列表时的过程中，如果你要改变列表的大小（增加值，或者删除值），那么结果很可能会出错或者报错。

l1 = [11, 22, 33, 44, 55]
# 请把索引为奇数对应的元素删除（不能一个一个删除，此l1只是举个例子，里面的元素不定）
# 第一种方法 直接删除
# del l1[1::2]
# print(l1)
# 第二种方法 倒序删除
# for i in range(len(l1) - 1, -1, -1):
#     if i % 2 == 1:
#         l1.pop(i)
# print(l1)
# 第三种方法 思维置换
# l2 = l1[::2]
# l1 = l2
# print(l1)

# dict
# update
dic = {'name': '太白', 'age': 18}
dic.update(hobby='运动', hight='175')
dic.update(name='太白金星')
dic.update([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])  # ***重点
print(dic)
dic1 = {'name': 'jin', 'age': 18, 'sex': 'male'}
dic2 = {'name': 'alex', 'weight': 75}
dic1.update(dic2)  # 更新，有则覆盖，无则添加
print(dic1)  # {'name': 'alex', 'age': 18, 'sex': 'male', 'weight': 75}
print(dic2)

# fromkeys
dic = dic.fromkeys('abc', 100)
print(dic)  # {'a': 100, 'b': 100, 'c': 100}
dic = dic.fromkeys([1, 2, 3], 'alex')
print(dic)  # {1: 'alex', 2: 'alex', 3: 'alex'}
# 值共有一个
dic = dic.fromkeys([1, 2, 3], [])
dic[1].append(666)
print(dic)  # {1: [666], 2: [666], 3: [666]}

# 将字典中所有键带k元素的键值对删除
dic = {'k1': '太白', 'k2': 'barry', 'k3': '白白', 'age': 18}
for i in list(dic.keys()):
    if 'k' in i:
        dic.pop(i)
print(dic)

# 字典在循环时，不能改变字典的大小，只要改变大小，就会报错
