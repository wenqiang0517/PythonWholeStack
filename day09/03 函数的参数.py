# 函数的传参：让函数封装的这个功能，盘活
# 实参，形参
# def meet(sex):
#     print("拿出手机")
#     print("打开陌陌，性别：%s" % sex)
#     print('左滑一下')
#     print('右滑一下')
#     print("找个漂亮的妹子")
#     print("问她,约不约啊!")
#     print("ok 走起")
#
#
# meet('女')   # 函数的执行传的参数：实际参数


# 函数的传参：实参，形参
# 实参角度
# 1，位置参数: 从左至右，一一对应
# def meet(sex, age, skill):
#     print("拿出手机")
#     print("打开陌陌，性别：%s 年龄：%s %s" % (sex, age, skill))
#     print('左滑一下')
#     print("问她,约不约啊!")
#     print("ok 走起")
#
# meet('女', 15, 'python nb')

# 写一个函数，只接受两个int的参数，函数的功能是将较大的数返回
# def compile(a, b):
#     return a if a > b else b
# print(compile(3244424, 3424232))

# 三元运算符：简单的if else
# a = 10
# b = 20
# if a > b:
#     c = a
# else:
#     c = b
# print(c)
#
# a = 100
# b = 20
# c = a if a > b else b
# print(c)


# 2，关键字参数
# 一一对应
# def meet(sex, age, skill, hight, weight):
#     print("拿出手机")
#     print("打开陌陌，性别：%s 年龄：%s 技术：%s 身高：%s 体重：%s" % (sex, age, skill, hight, weight))
#     print('左滑一下')
#     print("问她,约不约啊!")
#     print("ok 走起")
# meet(sex='女', age=15, skill='python nb', weight=100, hight=170)

# 函数：传入两个字符串参数，将两个参数拼接完成后形成的结果返回。
# def content(a, b):
#     return a + b
# print(content(b = '123', a = '456'))


# 混合参数
# 位置参数一定要在关键字参数的前面
# def meet(sex, age, skill, hight, weight):
#     print("拿出手机")
#     print("打开陌陌，性别：%s 年龄：%s 技术：%s 身高：%s 体重：%s" % (sex, age, skill, hight, weight))
#     print('左滑一下')
#     print("ok 走起")
#     return '性别：%s 年龄：%s' % (sex, age)
# print(meet('女', 15, skill='python nb', weight=100, hight=170))


"""
实参角度:
    1, 位置参数 按照顺序，一一对应
    2, 关键字参数，一一对应
    3, 混合参数：位置参数一定要在关键字参数的前面
"""

# 形参角度
# 1，位置参数 与实参角度的位置参数是一种
# 检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

# def func(l):
#     return l[:2]
#     return l[:2] if len(l) > 2 else l
#     if len(l) > 2:
#         return l[:2]
#     else:
#         return l
# print(func([1,2,3,4,5]))

# 2, 默认参数
# 默认参数设置的意义：普遍经常使用的
# def meet(age, skill, hight, weight, sex = '女'):
#     print("拿出手机")
#     print("打开陌陌，性别：%s 年龄：%s 技术：%s 身高：%s 体重：%s" % (sex, age, skill, hight, weight))
#     print('左滑一下')
#     print("ok 走起")
#     return '性别：%s 年龄：%s' % (sex, age)
# print(meet(15, skill='python nb', weight=100, hight=170))

# 形参角度：
#   1. 位置参数
#   2. 默认参数 （经常使用的）
