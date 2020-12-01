# 1，整理函数相关知识点，写博客
# 2，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者
# def func(l):
#     new_l = []
#     for i in range(len(l)):
#         if i % 2 != 0:
#             new_l.append(l[i])
#     return new_l
# print(func([1, 2, 3, 4, 5, 8]))

# 3，判断用户传入的对象（字符串，列表，元组）长度是否大于5
def func(l):
    return True if len(l) > 5 else False


print(func('weqewdwew'))

# 4，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
# 5，计算传入函数的字符串中，数字，字母 以及 其他 的个数，并返回结果
# s1 = '123qwe456asd@#$'
# def func(s1):
#     num_count = 0
#     al_count = 0
#     other_count = 0
#     for i in s1:
#         if i.isdecimal():
#             num_count += 1
#         elif i.isalpha():
#             al_count += 1
#         else:
#             other_count += 1
#     return '数字：%s，字母：%s，其他：%s' % (num_count, al_count, other_count)
# print(func(s1))

# 6，接收两个数字参数，返回比较大的那个数字
# 7，检查传入字典的每一个value 的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者,ps:字典中的value只能是字符串或列表
dic = {'k1': 'v1v1', 'k2': [11, 22, 33, 44]}


# def func(dic):
#     for key in dic.keys():
#         dic[key] = dic[key][:2]
#     return dic
# print(func(dic))

# 8，此函数只接受一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，此字典的键值对为此列表的索引及对应的元素
# 例如传入的列表为： [11, 22, 33]   返回的字典为 {0:11, 1:22, 2:33}
# def func(l):
#     dic = {}
#     for index in range(len(l)):
#         dic[index] = l[index]
#     return dic
# print(func([11, 22, 33]))

# 9，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这四个内容传入到函数中，此函数接收到这四个内容
# 将内容追加到一个student_msg文件中
# 10，对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女
"""
def func(name, age, education, sex='男'):
    with open('student_msg', mode='a', encoding='utf-8') as f:
        f.write('%s %s %s %s\n' % (name, sex, age, education))

while 1:
    name = input('请输入姓名(Q或者q退出)：')
    if name.upper() == 'Q':
        break
    sex = input('请输入性别：')
    age = input('请输入年龄：')
    education = input('请输入学历：')
    if sex == '':
        func(name, age, education)
    else:
        func(name, age, education, sex)
"""

# 11，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
"""
import os
def func(file_name, old_content, new_content):
    with open(file_name, encoding='utf-8') as f, open(file_name+'.bak', encoding='utf-8', mode='w') as f1:
        for line in f:
            new_line = line.replace(old_content, new_content)
            f1.write(new_line)
    os.remove('student_msg')
    os.rename('student_msg.bak', 'student_msg')
func('student_msg', '卢文强', 'alex')
"""

