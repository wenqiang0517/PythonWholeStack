r = range(10)  # [0,1,2,3,4,5,6,7,8,9]
# 顾头不顾腚
# print(r)
# for i in r:
#     print(i)
# 索引（了解）
# print(r[1])

# for i in range(1,101): print(i)

# for i in range(2,101,2):
#     print(i)

# for i in range(100,0,-1):
#     print

# l1 = [1, 2, 3, 'alex', '太白', 2, 3, 4, 66,]
# # 利用for循环，利用range将l1列表的所有索引依次打印出来
# '''
# 0
# 1
# 2
# 3
# 4
# '''
# for i in range(len(l1)):
#     print(i)

# for i in range(3):
#     pass
# print(i)


# enumerate：枚举，对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值。
li = ['alex', '银角', '女神', 'egon', '太白']
for i in enumerate(li):
    print(i)
# (0, 'alex')
# (1, '银角')
# (2, '女神')
# (3, 'egon')
# (4, '太白')

for index, name in enumerate(li, 1):
    print(index, name)
# 1 alex
# 2 银角
# 3 女神
# 4 egon
# 5 太白

for index, name in enumerate(li, 100):  # 起始位置默认是0，可更改
    print(index, name)
# 100 alex
# 101 银角
# 102 女神
# 103 egon
# 104 太白

