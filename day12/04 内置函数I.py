# eval：剥去字符串的外衣运算里面的代码
s1 = '1 + 3'
print(s1)
print(eval(s1))
s = '{"name": "alex"}'
print(s, type(s))
print(eval(s), type(eval(s)))
# 网络传输的str input输入的时候，sql注入等绝对不能使用evel

# exec 与evel几乎一样，代码流
s = '''
for i in [1,2,3]:
    print(i)
'''
exec(s)

# hash 哈希值
print(hash('adsdsa'))

# help 帮助
print(help(list))
print(help(str.split))

# callable 判断一个对象是否可被调用
name = 'alex'
def func():
    pass
print(callable(name))  # False
print(callable(func))  # True

# bin：将十进制转换成二进制并返回。
# oct：将十进制转化成八进制字符串并返回。
# hex：将十进制转化成十六进制字符串并返回
print(bin(10), type(bin(10)))  # 0b1010 <class 'str'>
print(oct(10), type(oct(10)))  # 0o12 <class 'str'>
print(hex(10), type(hex(10)))  # 0xa <class 'str'>

# ord:输入字符找该字符编码的位置
# chr:输入位置数字找出其对应的字符
print(ord('a'))
print(ord('中'))
print(chr(97))
print(chr(20013))

