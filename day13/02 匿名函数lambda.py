# def func(a, b):
#     return a + b
# 构建匿名函数
# func1 = lambda a, b : a + b
# print(func1(1, 2))

# 接收一个可切片的数据，返回索引为0与2的对应的元素（元组形式）
func = lambda a: (a[0], a[2])
print(func('abcde'))

# 接收两个int参数，将较大的数据返回
# func = lambda a, b: max(a, b)
func = lambda a, b: a if a > b else b
print(func(5, 12))

