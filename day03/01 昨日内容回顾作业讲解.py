# # while True:
# #     print(1)
#
#
# '''
# 如何终止循环？
#     1，标志位
# '''
# # n = True
# # while n:
# #     print(111)
# #     print(222)
# #     n = False
# #     print(333)
#
# # break: 直接终止循环
# # continue：终止本次循环，继续下一次循环
# '''
# while  else:
# '''
#
#
# Day2作业及默写
#
# 1. 判断下列逻辑语句的True,False.
#    1）1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
print(True, 1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
#    2）not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
print(False, not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# 2. 求出下列逻辑语句的值。
#    1),8 or 3 and 4 or 2 and 0 or 9 and 7
print(8, 8 or 3 and 4 or 2 and 0 or 9 and 7)
#    2),0 or 2 and 3 and 4 or 6 and 0 or 3
print(4, 0 or 2 and 3 and 4 or 6 and 0 or 3)
# 3. 下列结果是什么？
#    1)、6 or 2 > 1
print(6, 6 or 2 > 1)
#    2)、3 or 2 > 1
print(3, 3 or 2 > 1)
#    3)、0 or 5 < 4
print(False, 0 or 5 < 4)
#    4)、5 < 4 or 3
print(3, 5 < 4 or 3)
#    5)、2 > 1 or 6
print(True, 2 > 1 or 6)
#    6)、3 and 2 > 1
print(True, 3 and 2 > 1)
#    7)、0 and 3 > 1 *****************
print(0, 0 and True)
#    8)、2 > 1 and 3
print(3, 2 > 1 and 3)
#    9)、3 > 1 and 0
print(0, 3 > 1 and 0)
#    10)、3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
print(2, 3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)
# 4. while循环语句基本结构？
# while True:
#     循环体
# else：
#     语句
# 5. 利用while语句写出猜大小的游戏：
#    设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确，然后退出循环。
"""
while True:
    num_1 = int(input('请输入一个数字：'))
    if num_1 == 66:
        print('yes')
        break
    elif num_1 > 66:
        print('big')
    else:
        print('small')
"""
# 6. 在5题的基础上进行升级：
#    给用户三次猜测机会，如果三次之内猜测对了，
# 则显示猜测正确，退出循环，
# 如果三次之内没有猜测正确，
# 则自动退出循环，并显示‘太笨了你....’。
# while
# 3 次
# input
# if elif else

# count = 1
# while count < 4:
#     num = int(input('请输入数字：'))
#     if num > 66:
#         print('猜大了')
#     elif num < 66:
#         print('猜小了')
#     else:
#         print('恭喜你猜对了')
#         break
#     count += 1
# else:
#     print('太笨了')

# 7. 使用while循环输出 1 2 3 4 5 6 8 9 10
# count = 1
# while count < 11:
#     if count == 7:
#         print('')
#     else:
#         print(count)
#     count += 1

# count = 1
# while count < 11:
#     if count == 7:
#         pass
#     else:
#         print(count)
#     count += 1

# count = 1
# # while count < 11:
# #     if count == 7:
# #         count += 1
# #     print(count)
# #     count += 1

# count = 0
# while count < 10:
#     count += 1
#     if count == 7:
#         continue
#     print(count)

# 8. 求1-100的所有数的和
# 9. 输出 1-100 内的所有奇数
# 10. 输出 1-100 内的所有偶数
# 11. 求1-2+3-4+5 ... 99的所有数的和
"""
count = 2
sum_1 = 1
while count < 100:
    if (count % 2) == 0:
        sum_1 = sum_1 - count
    else:
        sum_1 = sum_1 + count
    count = count + 1
print(sum_1)
"""
# count = 1
# s = 0
# while count < 100:
#     if count % 2 == 0:
#         s = s - count
#     else:
#         s = s + count
#     count += 1
# print(s)


# 12. 用户登录（三次输错机会）且每次输错误时显示剩余错误次数（提示：使用字符串格式化）
"""
count = 3
while count > 0:
    count -= 1
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == 'lwq' and password == '123456':
        print('success')
        break
    else:
        print('登陆失败，你还剩 %s 次机会' % count)
"""
# count = 1
# while count <= 3:
#     username = input('用户名')
#     password = input('密码')
#     if username == 'alex' and password == '123':
#         print('登录成功')
#     else:
#         print('用户名或者密码错误,还剩%s机会' % (3-count))
#     count = count + 1
# 13. 简述ASCII、Unicode、utf-8编码
# 14. 简述位和字节的关系？
#
#



