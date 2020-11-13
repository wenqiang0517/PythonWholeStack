dic = {'lwq':
           {'name': '卢文强', 'age': 18},
       'alex':
           ['1', '3', 5, 9]
       }

# 创建字典的几种方式：
# 方式1:
dic = dict((('one', 1), ('two', 2), ('three', 3)))
# dic = dict([('one', 1), ('two', 2), ('three', 3)])
print(dic)  # {'one': 1, 'two': 2, 'three': 3}

# 方式2:
dic = dict(one=1, two=2, three=3)
print(dic)  # {'one': 1, 'two': 2, 'three': 3}

# 方式3:
dic = dict({'one': 1, 'two': 2, 'three': 3})
print(dic)  # {'one': 1, 'two': 2, 'three': 3}

# 验证字典的合法性
# 合法
dic = {123: 456, True: 999, "id": 1, "name": 'sylar', "age": 18, "stu": ['帅哥', '美⼥'], (1, 2, 3): '麻花藤'}
print(dic[123])
print(dic[True])
print(dic['id'])
print(dic['stu'])
print(dic[(1, 2, 3)])

# 不合法
# dic = {[1, 2, 3]: '周杰伦'} # list是可变的. 不能作为key
# dic = {{1: 2}: "哈哈哈"} # dict是可变的. 不能作为key
# dic = {{1, 2, 3}: '呵呵呵'}  # set是可变的, 不能作为key

# 键要唯一
dic = {1: 'lwq', 1: 'alex', 2: 'abc'}
print(dic)  # {1: 'alex', 2: 'abc'}

# 字典的增删改查
# 增
# 通过键值对直接增加,有则改之,无则增加
dic = {'name': '太白', 'age': 18}
dic["weight"] = 75
print(dic)  # {'name': '太白', 'age': 18, 'weight': 75}
dic['name'] = 'barry'
print(dic)  # {'name': 'barry', 'age': 18, 'weight': 75}

# setdefault 有则不变,无则增加
dic = {'name': '太白', 'age': 18}
dic.setdefault('sex')
print(dic)  # {'name': '太白', 'age': 18, 'sex': None}
dic.setdefault('height', 175)
print(dic)  # {'name': '太白', 'age': 18, 'height': 175}
dic.setdefault('name', 'barry')
print(dic)  # {'name': '太白', 'age': 18, 'height': 175}
# 有返回值
dic = {'name': '太白', 'age': 18}
ret = dic.setdefault('name')
print(ret)  # 太白

# 删
# pop 通过key删除字典的键值对，有返回值，可设置返回值。
dic = {'name': '太白', 'age': 18}
ret = dic.pop('name')
print(ret, dic)  # 太白 {'age': 18}
ret1 = dic.pop('n', None)
print(ret1, dic)  # None {'name': '太白', 'age': 18}

# clear 清空字典
dic = {'name': '太白', 'age': 18}
dic.clear()
print(dic)  # {}

# del
# 通过键删除键值对
dic = {'name': '太白', 'age': 18}
del dic['name']
print(dic)  # {'age': 18}
# 删除整个字典
del dic

# 改
# 通过键值对直接改
dic = {'name': '太白', 'age': 18}
dic['name'] = 'barry'
print(dic)  # {'name': 'barry', 'age': 18}

# update
dic = {'name': '太白', 'age': 18}
dic.update(sex='男', height=175)
print(dic)  # {'name': '太白', 'age': 18, 'sex': '男', 'height': 175}

dic = {'name': '太白', 'age': 18}
dic.update([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])
print(dic)  # {'name': '太白', 'age': 18, 1: 'a', 2: 'b', 3: 'c', 4: 'd'}

dic1 = {"name": "jin", "age": 18, "sex": "male"}
dic2 = {"name": "alex", "weight": 75}
dic1.update(dic2)
print(dic1)  # {'name': 'alex', 'age': 18, 'sex': 'male', 'weight': 75}
print(dic2)  # {'name': 'alex', 'weight': 75}

# 查
# 通过键查询
# 直接dic[key](没有此键会报错)
dic = {'name': '太白', 'age': 18}
print(dic['name'])  # 太白

# get ***
dic = {'name': '太白', 'age': 18}
v = dic.get('name')
print(v)  # '太白'
v = dic.get('name1')
print(v)  # None
v = dic.get('name2', '没有此键')
print(v)  # 没有此键

# keys()
dic = {'name': '太白', 'age': 18}
print(dic.keys())  # dict_keys(['name', 'age'])
# 可以转化成列表
print(list(dic.keys()))
for key in dic.keys():
    print(key)

for key in dic:
    print(key)

# values()
dic = {'name': '太白', 'age': 18}
print(dic.values())  # dict_values(['太白', 18])

# items()
dic = {'name': '太白', 'age': 18}
print(dic.items())  # dict_items([('name', '太白'), ('age', 18)])
for key, value in dic.items():
    print(key, value)

# 面试题
a = 11
b = 22
a, b = b, a
print(a, b)

dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
dic["k4"] = "v4"
print(dic)
# 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
dic["k1"] = "alex"
print(dic)
# 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic["k3"].append(44)
dic.get("k3").append(44)
print(dic)
# 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
dic["k3"].insert(0, 18)
print(dic)

