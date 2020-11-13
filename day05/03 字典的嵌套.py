dic = {
    'name': '汪峰',
    'age': 48,
    'wife': [{'name': '国际章', 'age': 38}],
    'children': {'girl_first': '小苹果', 'girl_second': '小怡', 'girl_three': '顶顶'}
}
# 1. 获取汪峰的名字。
print(dic.get('name'))
# 2.获取这个字典：{'name':'国际章','age':38}。
print(dic.get('wife')[0])
# 3. 获取汪峰妻子的名字。
print(dic.get('wife')[0].get('name'))
# 4. 获取汪峰的第三个孩子名字。
print(dic.get('children').get('girl_three'))

dic1 = {
    'name': ['alex', 2, 3, 5],
    'job': 'teacher',
    'oldboy': {'alex': ['python1', 'python2', 100]}
}
# 1，将name对应的列表追加⼀个元素’wusir’。
dic1.get('name').append('wusir')
print(dic1)
# 2，将name对应的列表中的alex⾸字⺟⼤写。
dic1.get('name')[0] = dic1.get('name')[0].upper()
print(dic1)
# 3，oldboy对应的字典加⼀个键值对’⽼男孩’,’linux’。
dic1.get('oldboy').setdefault('老男孩', 'linux')
print(dic1)
# 4，将oldboy对应的字典中的alex对应的列表中的python2删除
dic1.get('oldboy').get('alex').remove('python2')
print(dic1)
