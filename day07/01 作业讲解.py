# 1.请用代码验证"name" 是否在字典的键中
info = {'name': '盖伦', 'hobby': '锤子', 'age': '18', }  # 100个键值对
if 'name' in info.keys():
    print('yes')
else:
    print('no')

# 2.验证'alex'是否在字典的值中
# info = {'name':'盖伦','hobby':'锤子','age':'18',...100个键值对}
if 'alex' in info.values():
    print('yes')
else:
    print('no')

# 3.写代码
v1 = {'盖伦', '皇子', '赵信', '德玛'}
v2 = {'皇子', '德玛', '女枪', '女警'}
# 3.1 请输出v1和v2的交集
print(v1 & v2)
# 3.2 请输出v1和v2的并集
print(v1 | v2)
# 3.3 请输出v1和v2的差集
print(v1 - v2)
# 3.4 请输出v2和v1的差集
print(v2 - v1)

# 4.循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环）
"""
l1 = []
while 1:
    content = input("请输入：").strip()
    if content.upper() == 'N':
        break
    l1.append(content)
print(l1)
"""
# 5.循环提示用户输入，并将输入内容追加到集合中（如果输入N或n则停止循环）
"""
s1 = set()
while 1:
    content = input("请输入：").strip()
    if content.upper() == 'N':
        break
    s1.add(content)
print(s1)
"""
# 6.循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中（如果输入N或n则停止循环）
"""
v1 = {'lwq', '皇子', '赵信'}
v2 = []
while 1:
    content = input("请输入：").strip()
    if content.upper() == 'N':
        break
    elif content in v1:
        v2.append(content)
    else:
        v1.add(content)
print(v1)
print(v2)
"""
# 7.判断以下值哪个能做字典的key？  哪个能做集合的元素？  1  -1  ""  None  [1,2]  (1,)  {11,22,33,4}  {'name':'lwq','age':18}
# 字典的key  1 -1 (1,)
# 集合的元素  1  -1  (1,) ""

# 8.is 和 == 的区别
# is 判断id内存地址是否相等
# == 判断值是否相等

# 9.type使用方式及作用
# type(变量)  查看变量的数据类型

# 10.id的使用方式及作用
# id(变量)  查看内存地址

# 11.看代码写结果并解释原因
v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
v2 = {'k1': 'v1', 'k2': [1, 2, 3]}
result1 = v1 == v2
result2 = v1 is v2
print(result1)  # True
print(result2)  # False

# 12.看代码写结果并解释原因
v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
v2 = v1
result1 = v1 == v2
result2 = v1 is v2
print(result1)  # True
print(result2)  # True

# 13.看代码写结果并解释原因
v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
v2 = v1
v1['k1'] = 'lwq'
print(v2)  # {'k1': 'lwq', 'k2': [1, 2, 3]}

# 14.看代码写结果并解释原因
v1 = '人生苦短，我用python'
v2 = [1, 2, 3, 4, v1]
v1 = '人生苦短，用毛线python'
print(v2)  # [1, 2, 3, 4, '人生苦短，我用python']

# 15.看代码写结果并解释原因
info = [1, 2, 3]
userinfo = {'account': info, 'num': info, 'money': info}

info.append(9)
print(userinfo)  # {'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]}

info = "题怎么这么多"
print(userinfo)  # {'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]}

# 16.看代码写结果并解释原因 ****
info = [1, 2, 3]
userinfo = [info, info, info, info, info]

info[0] = "不仅多，还特么难呢"
print(info, userinfo)
# ["不仅多，还特么难呢", 2, 3]
# ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3]]

# 17.看代码写结果并解释原因 ****
info = [1, 2, 3]
userinfo = [info, info, info, info, info]

userinfo[2][0] = "闭嘴"
print(info, userinfo)
# ['闭嘴', 2, 3]
# [['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3]]

# 18.看代码写结果并解释原因
info = [1, 2, 3]
user_list = []
for item in range(10):
    user_list.append(info)
info[1] = "是谁说python好学的"
print(user_list)
# [[1, '是谁说python好学的', 3], [1, '是谁说python好学的', 3], [1, '是谁说python好学的', 3], [1, '是谁说python好学的', 3]....]

# 19.看代码写结果并解释原因
data = {}
for i in range(10):
    data['user'] = i
print(data)  # {'user': 9}

# 20.看代码写结果并解释原因
data_list = []
data = {}
for i in range(10):
    data['user'] = i
    data_list.append(data)
print(data)  # {'user': 9}

# 21.看代码写结果并解释原因
data_list = []
for i in range(10):
    data = {}
    data['user'] = i
    data_list.append(data)
print(data_list)  # [{'user': 0}, {'user': 1},{'user': 2},{'user': 3},....{'user': 9}]

# 22.使用循环打印出以下效果
# 22.1
# *
# **
# ***
# ****
# *****
"""
count = 0
while count < 5:
    count += 1
    print('*' * count)
"""
# 22.2
# ****
# ***
# **
# *
"""
count = 5
while count > 1:
    count -= 1
    print('*' * count)
"""
# 22.3
# *
# ***
# *****
# *******
# *********
count = -1
while count < 9:
    count += 2
    print('*' * count)

# 23.敲七游戏，从1开始数数，遇到7或者7的倍数（不包含17,27，这种数）要在桌上敲一下，编程来完成敲七，给出一个任意的数字n
# 从1开始数，数到n结束，把每个数字都放在列表中，在数的过程中出现7或者7的倍数，则想列表中添加一个'咣'
# 例如，输入10， lst = [1,2,3,4,5,6,'咣',8,9,10]
num_1 = input("请输入：").strip()
lst = []
for i in range(1, int(num_1)):
    if (i % 7) == 0:
        lst.append('咣')
    else:
        lst.append(i)
print(lst)
