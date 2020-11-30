# 1，有如下文件，a1.txt ， 里面的内容为：
# 老男孩是最好的学校，
#
# 全心全意为学生服务，
#
# 只为学生未来，不为牟利。
#
# 我说的都是真的。哈哈
# 分别完成以下的功能：
# a，将原文件全部读出来并打印。
# with open('a1.txt', encoding='utf-8') as f1:
#     print(f1.read())
# b，在原文件后面追加一行内容：信不信由你，反正我信了。
# with open('a1.txt', encoding='utf-8', mode='a') as f1:
#     f1.write('信不信由你，反正我信了。')
# c，将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。
# with open('a1.txt', encoding='utf-8', mode='r+') as f1:
#     print(f1.read())
#     f1.write('信不信由你，反正我信了。')
# d，将原文件全部清空，换成下面的内容：
# 每天坚持一点，
#
# 每天努力一点，
#
# 每天多思考一点，
#
# 慢慢你会发现，
#
# 你的进步越来越大。
# with open('a1.txt', encoding='utf-8', mode='w') as f1:
#     f1.write("""每天坚持一点，
#
# 每天努力一点，
#
# 每天多思考一点，
#
# 慢慢你会发现，
#
# 你的进步越来越大。""")

# 2，有如下文件，t1.txt ，里面的内容为：
# 葫芦娃，葫芦娃，
# 一个藤上七个瓜
# 风吹雨打，都不怕，
# 啦啦啦啦。
# 我可以算命，而且算的特别准：
# 上面的内容你肯定是心里默唱出来的，对不对？哈哈
# 分别完成以下的功能：
# a，以r模式打开原文件，利用for循环遍历文件句柄
# with open('a1.txt', encoding='utf-8') as f1:
#     for i in f1:
#         print(i)
# b，以r模式打开原文件，以readline()方法读取出来，并循环遍历readlines()，并分析a与b有什么区别？深入理解文件句柄与readlines()结果的区别
# with open('a1.txt', encoding='utf-8') as f1:
#     print(f1.readline())
#     for i in f1.readlines():
#         print(i)
# c，以r模式读取'葫芦娃，'前四个字符
# with open('a1.txt', encoding='utf-8') as f1:
#     print(f1.read(4))
# d，以r模式读取第一行内容，并去除此行前后的空行，制表符，换行符。
# with open('a1.txt', encoding='utf-8') as f1:
#     print(f1.readline().strip())
# e，以a+模式打开文件，先追加一行：'老男孩教育'然后在从最开始将原文件全部读取出来。
# with open('a1.txt', encoding='utf-8', mode='a+') as f1:
#     f1.write('老男孩教育')
#     f1.seek(0)
#     print(f1.read())

# 3，文件 a.txt 内容，每一行内容分别为商品名字，价钱，个数。
# apple 10 3
# tesla 100000 1
# mac 3000 2
# lenovo 30000 3
# chicken 10 3
# 通过代码，将其构建成这种数据类型：
# [{'name': 'apple', 'price': 10,'amount': 3},{'name': 'tesla', 'price': 100000,'amount': 1}...] 并计算出总价钱

"""
l1 = []
with open('a1.txt', encoding='utf-8') as f1:
    for line in f1:
        dic = {}
        l2 = line.strip().split()
        dic = {'name': l2[0], 'price': int(l2[1]), 'amount': int(l2[2])}
        l1.append(dic)
print(l1)
"""

"""
l1 = []
l2 = ['name', 'price', 'amount', 'year']
with open('a1.txt', encoding='utf-8') as f1:
    for line in f1:
        dic = {}
        l3 = line.strip().split()
        for index in range(len(l3)):
            dic[l2[index]] = l3[index]
        l1.append(dic)
print(l1)
"""

# 4，有如下文件，t1.txt ，里面的内容为： 将文件中所有的alex替换成SB     已做---
# alex是老男孩python发起人，创建人。
#
# alex其实是人妖。
#
# 谁说alex是sb？
#
# 你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。

# 5，文件a1.txt 内容
# name:apple price:10 amount:3 year:2012
# name:tesla price:100000 amount:1 year:2013
# 将其构建成这种数据类型
# [{'name': 'apple', 'price': 10,'amount': 3, 'year': 2012},{'name': 'tesla', 'price': 100000,'amount': 1}...] 并计算出总价钱
"""
l1 = []
with open('a1.txt', encoding='utf-8') as f1:
    for line in f1:
        dic = {}
        for i in line.strip().split():
            i = i.split(':')
            dic[i[0]] = i[1]
        l1.append(dic)
print(l1)
"""

"""
l1 = []
count = 0
with open('a1.txt', encoding='utf-8') as f1:
    for line in f1:
        dic = {}
        l2 = line.strip().split()
        dic[l2[0].split(':')[0]] = l2[0].split(':')[1]
        dic[l2[1].split(':')[0]] = int(l2[1].split(':')[1])
        dic[l2[2].split(':')[0]] = int(l2[2].split(':')[1])
        dic[l2[3].split(':')[0]] = int(l2[3].split(':')[1])
        count += int(l2[1].split(':')[1])
        l1.append(dic)
print(l1)
print(count)
"""

# 6，文件a1.txt内容
# 序号 部门 人数 平均年龄 备注
# 1 python 30 26 单身狗
# 2 linux 26 30 没对象
# 3 运营部 20 24 女生多
# 。。。
# 将其构建成这种数据类型
# [{'序号': 1, '部门': 'python','人数': 30, '平均年龄': 26, '备注': '单身狗'},
#  {'序号': 2, '部门': 'linux','人数': 26, '平均年龄': 30, '备注': '没对象'}...]

"""
l1 = []
with open('a1.txt', encoding='utf-8') as f1:
    l2 = f1.readlines()
    l_name = l2[0].split()
    for line in l2[1:]:
        dic = {}
        l3 = line.strip().split()
        for i in range(len(l3)):
            dic[l_name[i]] = l3[i]
        l1.append(dic)
print(l1)
"""

"""
l1 = []
count = 0
with open('a1.txt', encoding='utf-8') as f1:
    for line in f1:
        dic = {}
        l2 = line.strip().split()
        dic[l2[0].split(':')[0]] = l2[0].split(':')[1]
        dic[l2[1].split(':')[0]] = int(l2[1].split(':')[1])
        dic[l2[2].split(':')[0]] = int(l2[2].split(':')[1])
        dic[l2[3].split(':')[0]] = int(l2[3].split(':')[1])
        count += int(l2[1].split(':')[1])
        l1.append(dic)
print(l1)
print(count)
"""

