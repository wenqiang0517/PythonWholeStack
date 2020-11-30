s1 = 'wdlsfkfjewf'
# count = 0
# for i in s1:
#     count += 1
# print(count)

l1 = [1, 2, 3, 4, 5, 6, 7]
# count = 0
# for i in l1:
#     count += 1
# print(count)


def my_len(s):
    count = 0
    for i in s:
        count += 1
    print(count)
my_len(s1)
my_len(l1)

# 函数：以功能（完成一件事）为导向，登陆，注册，len，一个函数就是一个功能，随调随用
# 减少代码的重复性
# 增强了代码的可读性


def meet():
    print("拿出手机")
    print("打开陌陌")
    print('左滑一下')
    print('右滑一下')
    print("找个漂亮的妹子")
    print("问她,约不约啊!")
    print("ok 走起")
# meet()
'''
结构：def 关键字，定义函数
    meet 函数名：与变量设置相同，具有可描述性
    函数体：缩进。函数中尽量不要出现print
'''

# 函数什么时候执行？
# 当函数遇到   函数名() 函数才会执行！！！


# 函数的返回值
def meet():
    print("拿出手机")
    print("打开陌陌")
    print('左滑一下')
    # return
    print('右滑一下')
    print("找个漂亮的妹子")
    print("问她,约不约啊!")
    print("ok 走起")
    # return '妹子一个'
    return '妹子一个', 123, [22, 33]

ret = meet()
# ret, ret1, ret2 = meet()
print(ret, type(ret))
# return: 在函数中遇到return直接结束函数
# return 将数据返回给函数的执行者，调用者 meet()
# return 返回多个元素，是以元组的形式返回给函数的执行者。

'''
return 总结：
    1，在函数中，终止函数。
    2，return 可以给函数的执行者返回值
        1，return 单个值        单个值
        2，return 多个值        (多个值,)
'''

