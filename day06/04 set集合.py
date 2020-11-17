# 集合的创建
set1 = set({1, 3, "lwq", False})
set1 = {1, 3, "lwq", False, 'alex', 7}
print(set1)

# 空集合
print({}, type({}))  # 空字典
set1 = set()
print(set1)

# 集合的有效性测试
# set1 = {1, [1, 23, 4], 3, "lwq", False, 'alex', 7}
# print(set1)  # 无效的

set1 = {'lwq', 'abc', 'alex', 'zzz', 'ttt', 'ccc'}
# 增 add
set1.add('xxx')
print(set1)  # {'ttt', 'xxx', 'ccc', 'zzz', 'abc', 'lwq', 'alex'}

# update 迭代着增加
set1.update('abcdabcd')
print(set1)

# 删
# remove 按照元素删除
set1.remove('alex')
print(set1)

# pop 随机删除
# set1.pop()
# print(set1)

# 变相改值
set1.remove('lwq')
set1.add('lwqnb')
print(set1)

# 关系测试   ***
# 交集
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 & set2)  # {4, 5}
print(set1.intersection(set2))  # {4, 5}

# 并集
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7,8}
print(set2.union(set1))  # {1, 2, 3, 4, 5, 6, 7,8}

# 差集
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 - set2)  # {1, 2, 3}
print(set1.difference(set2))  # {1, 2, 3}

# 反交集
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 ^ set2)  # {1, 2, 3, 6, 7, 8}
print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}

# 子集与超集
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5, 6}
print(set1 < set2)
print(set1.issubset(set2))  # 这两个相同，都是说明set1是set2子集。

print(set2 > set1)
print(set2.issuperset(set1))  # 这两个相同，都是说明set2是set1超集。

# 列表的去重 ***
l1 = [1, 'lwq', 1, 2, 2, 'lwq', 2, 6, 6, 6, 3, 'lwq', 4, 5]
set1 = set(l1)
l1 = set1
print(l1)

# 用处：数据之间的关系，列表去重。

