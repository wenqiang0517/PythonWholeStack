# 1，函数可以支持接受任意数字（位置传参）并将所有数据相加返回
# def func(*args):
#     count = 0
#     for i in args:
#         count += i
#     print(count)
# func(1,2,3,4,5)

# 2，看代码写结果
def func():
    return 1, 2, 3
val = func()
print(type(val) == tuple)
# True
print(type(val) == list)
# False

# 3，看代码写结果
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# a,请将执行函数，并实现让args的值为（1，2，3，4）
# func(1,2,3,4)
# b,请将执行函数，并实现让args的值为 ([1，2，3，4], [11,22,33])
# func([1,2,3,4], [11,22,33])
# c,请将执行函数，并实现让args的值为 ([11,22],33),且kwargs的值为{'k1':'v1', 'k2': 'v2'},
# func([11,22],33,k1='v1',k2='v2')
# d,如执行func(*{'武佩奇','金鑫','女神'})，请问args和kwargs的值分别是？
# func(*{'武佩奇','金鑫','女神'})
# args = ('武佩奇','金鑫','女神')
# kwargs = {}
# e,如执行func({'武佩奇','金鑫','女神'}, [11,22,33])，请问args和kwargs的值分别是？
# func({'武佩奇','金鑫','女神'}, [11,22,33])
# args = ({'武佩奇','金鑫','女神'}, [11,22,33])
# kwargs = {}
# f,如执行func('武佩奇','金鑫','女神', [11,22,33], **{'k1': '栈'})，请问args和kwargs的值分别是？
# func('武佩奇','金鑫','女神', [11,22,33], **{'k1': '栈'})
# args = ({'武佩奇','金鑫','女神'}, [11,22,33])
# kwargs = {'k1': '栈'}

# 4，看代码写结果
def func(name, age=19, email='123@qq.com'):
    print(name)
    print(age)
    print(email)
# a,执行func('alex'),判断是否可执行，如可以请问name,age,email的值分别是？
func('alex')
# name = 'alex'
# age = 19
# email = '123@qq.com'
# b,执行func('alex', 20),判断是否可执行，如可以请问name,age,email的值分别是？
func('alex', 20)
# name = 'alex'
# age = 20
# email = '123@qq.com'
# c,执行func('alex',20,30),判断是否可执行，如可以请问name,age,email的值分别是？
func('alex',20,30)
# name = 'alex'
# age = 20
# email = 30
# d,执行func('alex', email='x@qq.com'),判断是否可执行，如可以请问name,age,email的值分别是？
func('alex', email='x@qq.com')
# name = 'alex'
# age = 19
# email = 'x@qq.com'

# e,执行func('alex', email='x@qq.com', age=99),判断是否可执行，如可以请问name,age,email的值分别是？
func('alex', email='x@qq.com', age=99)
# name = 'alex'
# age = 99
# email = 'x@qq.com'

# f,执行func(name='alex', 99),判断是否可执行，如可以请问name,age,email的值分别是？
# func(name='alex', 99)
# 不可执行

# g,执行func(name='alex', 99, '111@qq.com'),判断是否可执行，如可以请问name,age,email的值分别是？
# func(name='alex', 99, '111@qq.com')
# 不可执行

# 5,看代码写结果
def func(user, name):
    user.append(name)
    return user
result = func(['武佩奇', '李杰'], 'alex')
print(result)
# ['武佩奇', '李杰', 'alex']

# 6,看代码写结果
def func(v1):
    return v1 * 2
def bar(arg):
    return "%s 是什么玩意" % (arg,)
val = func('你')
data = bar(val)
print(data)
# 你你 是什么玩意

# 7,看代码写结果
def func(v1):
    return v1 * 2
def bar(arg):
    msg = "%s 是什么玩意" % (arg,)
    print(msg)
val = func('你')
data = bar(val)
print(data)
# None

# 8,看代码写结果
v1 = '武佩奇'
def func():
    print(v1)
func()
v1 = '老男人'
func()
# '武佩奇' '老男人'

# 9,看代码写结果
v1 = '武佩奇'
def func():
    v1 = '景女神'
    def inner():
        print(v1)
    v1 = '肖大侠'
    inner()
func()
v1 = '老男人'
func()
# '肖大侠' '肖大侠'

# 10,看代码写结果
def func():
    data = 2 * 2
    return data
new_name = func
val = new_name()
print(val)
# 4

# 11,看代码写结果
def func():
    data = 2 * 2
    return data
data_list = [func, func, func]
for item in data_list:
    v = item()
    print(v)
# 4 4 4

# # 12,看代码写结果
def func(arg):
    arg()
def show():
    print('show函数')
func(show)
# 'show函数'

# 13,写函数，接收n个数字，求这些参数数字的和。(动态传参)
# def func(*args):
#     count = 0
#     for i in args:
#         count += i
#     print(count)
# func(1,2,3,4,5)

# 14，读代码，回答：代码中，打印出来的值a,b,c分别是什么，为什么
a = 10
b = 20
def test5(a,b):
    print(a,b)
c = test5(b, a)
print(c)
# a=20 b=10 None

# 15，读代码，回答：代码中，打印出来的值a,b,c分别是什么，为什么
a = 10
b = 20
def test5(a,b):
    a = 3
    b = 5
    print(a,b)
c = test5(b, a)
print(c)
# a=3 b=5 None

# 16,传入函数中多个列表和字典，如何将每个列表的每个元素一次添加到函数的动态参数args里面，如何将每个字典的所有键值对依次添加到kwargs里面
# func(*[1,2,3,4], **{'k1': 'v1'})

# 17,写函数，接收两个数字参数，将较小的数字返回

# 18，接收一个参数（此参数类型必须为可迭代对象），将可迭代对象的每个元素以'_'相连接，形成新的字符串，并返回
# 例如 传入的可迭代对象为[1, '老男孩', '武sir'] 返回的结果为'1_老男孩_武sir'
def func(l):
    content = ''
    for i in range(len(l)):
        if i == 0:
            content += str(l[i])
        else:
            content = content + '_' + str(l[i])
    return content
print(func([1, '老男孩', '武sir']))

# 19,有如下函数
def wrapper():
    def inner():
        print(666)
    inner()
wrapper()
# 你可以任意代码，执行inner函数

# 20,写出下列代码结果：
def foo(a, b, *args, c, sex=None, **kwargs):
    print(a, b)
    print(c)
    print(sex)
    print(args)
    print(kwargs)
foo(1,2,3,4,c=6)
# 1 2 6 None (3,4) {}

# foo(1,2,sex='男',name='alex',hobby='old_woman')
# foo() missing 1 required keyword-only argument: 'c'

# foo(1,2,3,4,name='alex',sex='男')
# foo() missing 1 required keyword-only argument: 'c'

foo(1,2,c=18)
# 1 2 18 None () {}

foo(2,3,[1,2,3],c=13,hobby='喝茶')
# 2 3 13 None ([1,2,3],) {'hobby': '喝茶'}

foo(*[1,2,3,4],**{'name':'太白','c':12,'sex':'女'})
# 1 2 12 '女' (3,4) {'name': '太白'}


