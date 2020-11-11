# # for i in 'afdsf':
# #     print(i)
#
# # break continue
# # s1 = 'fsdafsda'
# # for i in s1:
# #     continue
# #     print(i)
#
# Day03作业及默写
# 1, 有变量name = "aleX leNb" 完成如下操作：
name = "aleX leNb"
# 移除 name 变量对应的值两边的空格,并输出处理结果
print(name.strip())
# 判断 name 变量是否以 "al" 开头,并输出结果
print(name.startswith('al'))
# 判断name变量是否以"Nb"结尾,并输出结果
print(name.endswith('Nb'))
# 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
print(name.replace('l', 'p'))
# 将name变量对应的值中的第一个"l"替换成"p",并输出结果
print(name.replace('l', 'p', 1))
# 将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
print(name.split('l'))
# 将name变量对应的值根据第一个"l"分割,并输出结果。
print(name.split('l', 1))
# 将 name 变量对应的值变大写,并输出结果
print(name.upper())
# 将 name 变量对应的值变小写,并输出结果
print(name.lower())
# 判断name变量对应的值字母"l"出现几次，并输出结果
print(name.count('l'))
# 如果判断name变量对应的值前四位"l"出现几次,并输出结果
print(name.count('l', 0, 6))
# 请输出 name 变量对应的值的第 2 个字符?
print(name[1])
# 请输出 name 变量对应的值的前 3 个字符?
print(name[:3])
# 请输出 name 变量对应的值的后 2 个字符?
print(name[-1:-3:-1])
# 2.有字符串s = "123a4b5c"
s = "123a4b5c"
# 通过对s切片形成新的字符串s1,s1 = "123"
print(s[:3])
# 通过对s切片形成新的字符串s2,s2 = "a4b"
print(s[3:-2])
# 通过对s切片形成新的字符串s3,s3 = "1345"
print(s[::2])
# 通过对s切片形成字符串s4,s4 = "2ab"
print(s[1:-1:2])
# 通过对s切片形成字符串s5,s5 = "c"
print(s[-1])
# 通过对s切片形成字符串s6,s6 = "ba2"
print(s[-3::-2])
# 使用while和for循环分别打印字符串s="asdfer"中每个元素。
"""
s = "asdfer"
count = 0
while count < len(s):
    print(s[count])
    count += 1
for i in s:
    print(i)
"""
# 使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"。
# s = "asdfer"
# for i in s:
#    print(s)

# 使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb,...gsb。
# s="abcdefg"
# for i in s:
#     print(i + 'sb')

# 使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
# s = '321'
# for i in s:
#     print('倒计时{}秒'.format(i))
# print(i)
# print('出发！')

# 实现一个整数加法计算器(两个数相加)：
"""
num_1 = int(input('第一个数：'))
num_2 = int(input('第二个数：'))
print('sum: {}'.format(num_1 + num_2))
"""
# 如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。
"""
content = input("请输入内容: ")
print(int(content.split('+')[0]) + int(content.split('+')[1]))
"""
# 选做题：实现一个整数加法计算器（多个数相加）：
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+ 13，然后进行分割再进行计算。
"""
content = input("请输入内容:").split('+')
count = 0
for i in content:
    count += int(i)
print(count)
"""
# 计算用户输入的内容中有几个整数（以个位数为单位）。
# ​如：content = input("请输入内容：") # 如 fhdal234slfh98769fjdla
"""
content = input("请输入内容：")
count = 0
for i in content:
    if i.isdecimal():
        count += 1
print(count)
"""
# 选做题：写代码，完成下列需求：
# 用户可持续输入（用while循环），用户使用的情况：
# 输入A，则显示走大路回家，然后在让用户进一步选择：
# 是选择公交车，还是步行？
# 选择公交车，显示10分钟到家，并退出整个程序。
# 选择步行，显示20分钟到家，并退出整个程序。
# 输入B，则显示走小路回家，并退出整个程序。
# 输入C，则显示绕道回家，然后在让用户进一步选择：
# 是选择游戏厅玩会，还是网吧？
# 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
# 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
"""
while True:
    content = input("请选择 A B C: ").strip()
    if content == 'A':
        print('走大路回家')
        while True:
            content = input("请选择 公交车 步行: ").strip()
            if content == '公交车':
                print('10分钟到家')
                break
            elif content == '步行':
                print('20分钟到家')
                break
            else:
                print('输入错误')
        break
    elif content == 'B':
        print('走小路回家')
        break
    elif content == 'C':
        print('绕道回家')
        while True:
            content = input("请选择 游戏厅 网吧: ").strip()
            if content == '游戏厅':
                print('一个半小时到家，爸爸在家，拿棍等你。')
                break
            elif content == '网吧':
                print('两个小时到家，妈妈已做好了战斗准备。')
                break
            else:
                print('输入错误')
    else:
        print('输入错误')
"""

# 写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？
count = 1
sum_1 = 1
while count < 99:
    count += 1
    if count == 88:
        continue
    elif count % 2 == 0:
        sum_1 -= count
    else:
        sum_1 += count
print(sum_1)

# **选做题：**判断⼀句话是否是回⽂. 回⽂: 正着念和反着念是⼀样的. 例如, 上海 ⾃来⽔来⾃海上
content = input('输⼊：').replace(' ', '').strip()
if content == content[::-1]:
    print('回⽂')
else:
    print('no')

# 制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进行任意现实 如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
# name = input('输⼊名字：')
# place = input('输⼊地点：')
# hobby = input('输⼊爱好：')
# print('敬爱可亲的{0}，最喜欢在{1}⼲{2}'.format(name, place, hobby))
