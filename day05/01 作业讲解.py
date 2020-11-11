# 面试题：
l1 = range(5)
print(l1[1:3])  # range(1,3),       [1,2]  1, 2  (1, 2)
print(l1[-1])

# for i in range(1, 5, -1):
#     print(i)

# 4.请用代码实现：
# li = ["alex", "wusir", "taibai", 2]
# 利用下划线将列表的每一个元素拼接成字符串"alex_wusir_taibai"
# s = '_'.join(li)
# print(s)
# s = ''
# for i in li:
#     s = s + '_' + i
# print(s[1:])

# 5.利用for循环和range打印出下面列表的索引。
"""
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
for i in range(len(li)):
    print(i)
"""
# 6.利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
"""
l1 = []
for i in range(2, 101, 2):
    print(i)
    l1.append(i)
print(l1)
"""
# 7.利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
"""
l1 = []
for i in range(3, 51):
    if i % 3 == 0:
        l1.append(i)
print(l1)
"""
# 8.利用for循环和range从100~1，倒序打印。
"""
for i in range(100, 0, -1):
    print(i)
"""
# 9.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
"""
l1 = []
for i in range(100, 9, -2):
    l1.append(i)
print(l1)
for i in l1:
    if i % 4 != 0:
        l1.remove(i)
print(l1)
"""
# 10.利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成*。
"""
l1 = []
for i in range(1, 31):
    l1.append(i)
print(l1)
for i in l1:
    if i % 3 == 0:
        l1[l1.index(i)] = '*'
print(l1)
"""
# 11.查找列表li中的元素，移除每个(for)元素的空格 strip，
# 并找出以"A"或者"a"开头startswith，并以"c"结尾的所有元素 endswith，并添加到一个新列表new_  l = []中,最后循环for 打印这个新列表。
"""
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc", 'a c', 'adfdfdgdc']
new_list = []
for i in li:
    new_i = i.strip()  # "TaiBai"
    # if (new_i.startswith('A') or new_i.startswith('a')) and new_i.endswith('c'):
    # if new_i.upper().startswith('A') and new_i.endswith('c'):
    if new_i[0].upper() == 'A' and new_i[-1] == 'c':
        new_list.append(new_i)
for i in new_list:
    print(i)
"""

# 12.开发敏感词语过滤程序，提示用户输入input评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# # 则将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），并添加到一个列表中；
# # 如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
# '武藤兰hd苍老师skafh苍老师sdf苍老师fdslkafjl东京热波多野结衣。'
"""
li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
comment_list = []
comment = input('请输入您的评论：')
for word in li:
    if word in comment:
        comment = comment.replace(word, '*' * len(word))
        print(comment)
        # 第一次循环： c = '武藤兰hd***skafh***sdf***fdslkafjl东京热波多野结衣。'
        # 第二次循环:  c = '武藤兰hd苍老师skafh苍老师sdf苍老师fdslkafjl***波多野结衣。'
        # ......
        # 最后一次循环：c = '武藤兰hd苍老师skafh苍老师sdf苍老师fdslkafjl东京热*****。'
comment_list.append(comment)
print(comment_list)
"""

# 13.有如下列表（选做题）
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# 循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
# 我想要的结果是：
# 1
# 3
# 4
# "alex"
# 3
# 7
# 8
# "taibai"
# 5
# ritian
"""
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
for i in li:
    if type(i) == list:
        for j in i:
            print(j)
    else:
        print(i)
"""

# 明日默写内容
# 将列表的增删改查不同的方法全部写出来，
# 例如：增：有三种，append：在后面添加。Insert按照索引添加，
# expend：迭代着添加。

# sort排序，对原列表排序，默认升序，返回值为None，reverse=True降序，只能对元素都是同一类型的list进行排序
# l2 = [5, 8, 2, 4, '3', '76', [8, 2, 4, 1, 0]]
# l2 = [5, 8, 2, 4]
l2 = ['3', '76', '56', '0', '11', 'wqeqe', 'q', 'adsdsdsd', 'saaaa']
# l2 = [[5, 8, 2, 4], [1, 7, 0, 4],[56, 22, 8, 3]]
print(id(l2))
l2.sort()
print(id(l2))
# l2.sort(reverse=True)
print(l2)

