# 赋值运算
l1 = [1, 2, 3, [22, 33]]
l2 = l1
l1.append(666)
print(l1)
print(l2)

# 浅copy
l1 = [1, 2, 3, [22, 33]]
l2 = l1.copy()
l1.append(666)
print(id(l1))
print(id(l2))

