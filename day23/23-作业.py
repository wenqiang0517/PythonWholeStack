# 第一大题 : 读程序,标出程序的执行过程,画出内存图解,说明答案和为什么
# 请不要想当然,执行之后检查结果然后再确认和自己的猜想是不是一致
# (1)
"""
class A:
    Country = '中国'  # 静态变量/静态属性 存储在类的命名空间里的

    def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age

    def func1(self):
        print(self)


a = A('alex', 83, '印度')
b = A('wusir', 74, '泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country)    # 日本
print(b.Country)    # 英国
print(A.Country)    # 英国
"""


# (2)
"""
class A:
    Country = ['中国']  # 静态变量/静态属性 存储在类的命名空间里的

    def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age

    def func1(self):
        print(self)


a = A('alex', 83, '印度')
b = A('wusir', 74, '泰国')
a.Country[0] = '日本'
print(a.Country)    # ['日本']
print(b.Country)    # ['日本']
print(A.Country)    # ['日本']
"""


# (3)
"""
class A:
    Country = '中国'  # 静态变量/静态属性 存储在类的命名空间里的

    def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
        self.Country = country

    def func1(self):
        print(self)


a = A('alex', 83, '印度')
b = A('wusir', 74, '泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country)    # 日本
print(b.Country)    # 泰国
print(A.Country)    # 英国
"""


# (4)
class A:
    Country = '中国'  # 静态变量/静态属性 存储在类的命名空间里的

    def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age

    def Country(self):
        return self.Country


a = A('alex', 83, '印度')
b = A('wusir', 74, '泰国')
print(a.Country)    # Country 内存地址
print(a.Country())  # Country 内存地址


# 第二大题:基于圆形类实现一个圆环类,要求接收参数 外圆半径和内圆半径
# 完成方法 :计算环形面积和环形周长(公式自己上网查)
# 要求,借助组合,要求组合圆形类的对象完成需求
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def round_area(self):
        area = pi * (self.radius ** 2)
        return area

    def round_perimeter(self):
        perimeter = 2 * pi * self.radius
        return perimeter


class Annulus:
    def __init__(self, big_radius, small_radius):
        big_radius, small_radius = (big_radius, small_radius) if big_radius > small_radius else (small_radius, big_radius)
        self.big_radius = Circle(big_radius)
        self.small_radius = Circle(small_radius)

    def annulus_area(self):
        return self.big_radius.round_area() - self.small_radius.round_area()

    def annulus_perimeter(self):
        return self.big_radius.round_perimeter() + self.small_radius.round_perimeter()


c = Annulus(10, 5)
print(c.annulus_area(), c.annulus_perimeter())

# 第三大题:继续完成计算器和优化工作

