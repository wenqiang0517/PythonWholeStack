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
#     print('右滑一下')
#     print("找个漂亮的妹子")
#     print("问她,约不约啊!")
#     print("ok 走起")
#
# meet('女', 15, 'python nb')

# 写一个函数，只接受两个int的参数，函数的功能是将较大的数返回

def max_num(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2

print(max_num(3244424, 3424232))

