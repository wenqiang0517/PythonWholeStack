# 可迭代对象
# 获取一个对象的所有方法：dir()
s1 = 'swewqe'
l1 = [1, 2, 3]
print(dir(s1))
print(dir(l1))
print('__iter__' in dir(s1))
print('__iter__' in dir(l1))
print('__iter__' in dir(range(10)))

# 从字面意思来说：可迭代对象就是可以进行循环更新的一个实实在在的值。
# 从专业角度来说：内部含有 '__iter__' 方法的对象，就是可迭代对象。
# 可迭代对象可以通过判断该对象是否有 '__iter__' 方法来判断：  '__iter__' in dir(对象)
# str list tuple dict set range
# 可迭代对象的优点：
#   1，存储的数据直接能显示，比较直观
#   2，拥有的方法比较多，操作方便
# 可迭代对象的缺点：
#   1，占用内存。
#   2，不能直接通过for循环，不能直接取值（除去索引，key以外）
#   for循环在底层做了一个小小的转化，就是先将可迭代对象转化成迭代器，然后在进行取值的


# 迭代器
# 迭代器的定义
#     字面意思: 更新迭代，器：工具：可更新迭代的工具
#     专业角度：内部含有 '__iter__' 方法并且含有 '__next__' 方法的对象就是迭代器
#     可以判断是是迭代器：'__iter__' and '__next__' 在不在 dir(对象)
# 优点：
# 1，节省内存
# 2，惰性机制，next一次，取一个值
# 缺点：
# 1，速度慢
# 2，不走回头路
# 可迭代对象与迭代器的对比
# 1，可迭代对象：是一个私有的方法比较多，操作灵活, 比较直观，存储数据相对较少（几百万个对象，8G内存是可以承受的）的一个数据集。
# 2，应用：当你侧重于对于数据可以灵活处理，并且内存空间足够，将数据集设置为可迭代对象是明确的选择。
# 3，迭代器：是一个非常节省内存，可以记录取值位置，可以直接通过循环 + next方法取值，但是不直观，操作方法比较单一的数据集。
# 4，应用：当你的数据量过大，大到足以撑爆你的内存或者你以节省内存为首选因素时，将数据集设置为迭代器是一个不错的选择

# 判断是否是迭代器
with open('test', encoding='utf-8') as f:
    print(('__iter__' in dir(f)) and ('__next__' in dir(f)))

# 可迭代对象可以转化成迭代器
s1 = 'qwetyui'
obj = iter(s1)      # obj = s1.__iter__()
print(obj)
print(next(obj))        # print(obj.__next__())
print(next(obj))
print(next(obj))
print(next(obj))

l1 = [11, 22, 33, 44, 55, 66]
obj = iter(l1)
print(obj)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

# 利用while循环模拟for循环对可迭代对象进行取值的机制
l1 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
# 将可迭代对象转化成迭代器
obj = iter(l1)
while 1:
    try:
        print(next(obj))
    except StopIteration:
        break
