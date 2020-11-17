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

# 交集
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 & set2)  # {4, 5}
print(set1.intersection(set2))  # {4, 5}

# 并集







