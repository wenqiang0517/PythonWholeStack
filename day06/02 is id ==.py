# id
i = 100
s = 'alex'
print(id(i))  # 745695172048
print(id(s))  # 745696359536

# == 比较的是两边的值是否相等
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)  # True
s1 = 'alex'
s2 = 'alex '
print(s1 == s2)  # False

# is 判断内存地址是否相同
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(id(l1))  # 745696413376
print(id(l2))   # 745695427840
print(l1 is l2)     # False
s1 = 'alex'
s2 = 'alex'
print(id(s1))   # 745696359536
print(id(s2))   # 745696359536
print(s1 is s2)     # True

# id 相同，值一定相同
# 值相同，id不一定相同

