# 1，面向对象为什么要有继承
# 当两个类中有相同或相似的静态变量或绑定方法时，使用继承可以减少代码的重用，提高代码可读性，规范编程模式

# 2，python继承时，查找成员的顺序遵循什么规则
# 经典类 -- 深度优先
# 新式类 -- 广度优先

# 3，看代码，写结果
"""
class Base1:
    def f1(self):
        print('base1.f1')

    def f2(self):
        print('base1.f2')

    def f3(self):
        print('base1.f3')
        self.f1()


class Base2:
    def f1(self):
        print('base2.f1')


class Foo(Base1, Base2):
    def f0(self):
        print('foo.f0')
        self.f3()


obj = Foo()
obj.f0()

# 执行结果
# foo.fo
# base1.f3
# base1.f1
"""

# 4，看代码，写结果
"""
class Base:
    def f1(self):
        print('base.f1')

    def f3(self):
        self.f1()
        print('base.f3')


class Foo(Base):
    def f1(self):
        print('foo.f1')

    def f2(self):
        print('foo.f2')
        self.f3()


obj = Foo()
obj.f2()

# 执行结果
# foo.f2
# foo.f1
# base.f3
"""

# 5，补充代码实现下列需求
    # 5.1 while循环提示用户输入: 用户名、密码、邮箱(正则满足邮箱格式)
    # 5.2 为每个用户创建1个对象，并添加到列表中。
    # 5.3 当列表中的添加 3个对象后，跳出循环并以此循环打印所有用户的姓名和邮箱

"""
import re
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


user_list = []
while True:
    if len(user_list) < 3:
        user = input("请输入用户名:")
        pwd = input("请输入密码:")
        while True:
            email = input("请输入邮箱:").strip()
            result = re.search('\w+@\w+\.com(\.cn)?', email)
            if result:
                email = result.group()
                break
            else:
                print('重新输入')
                continue
        people = User(user, pwd, email)
        user_list.append(people)
    else:
        for i in user_list:
            print(i.username, i.email)
        break
"""

# 6，补充代码，实现用户登录和注册
class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = []
        self.dic = {}
        self.lis = []

    def login(self):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        username = input('请输入用户名').strip()
        pwd = input('请输入密码').strip()
        for i in self.user_list:
            self.dic = dict()
            self.dic[i.name] = i.pwd
        # print(self.dic)
        if username in self.dic.keys():
            if pwd == self.dic[username]:
                print('登录成功')
                return True
            else:
                print('密码错误，重新输入')
        else:
            print('用户不存在，请先注册')
            self.register()

    def register(self):
        """
        用户注册，每注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        while True:
            username = input('请输入用户名').strip()
            pwd = input('请输入密码').strip()
            for i in self.user_list:
                self.lis = []
                self.lis.append(i.name)
            print(self.lis)
            if username in self.lis:
                print('用户已存在,请重新输入')
            else:
                people = User(username, pwd)
                self.user_list.append(people)
                break

    def run(self):
        """
        主程序
        :return:
        """
        opt_lst = ['登录', '注册']
        while True:
            for a, b in enumerate(opt_lst, 1):
                print(a, b)
            num = input('请选择：').strip()
            if num == '1':
                self.login()
            elif num == '2':
                self.register()
            elif num.upper() == 'Q':
                print('退出')
                break
            else:
                print('请重新输入')


if __name__ == '__main__':
    obj = Account()
    obj.run()


# 6.5 将第6题的需求进行修改，不用列表了，改成读取本地文件


# 7，读代码写结果
"""
class Base:
    x = 1

obj = Base()
print(obj.x)
obj.y = 123
print(obj.y)
obj.x = 123
print(obj.x)
print(Base.x)

# 执行结果
# 1
# 123
# 123
# 1
"""

# 8，读代码写结果
"""
class Parent:
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child2.x = 2
print(Parent.x, Child1.x, Child2.x)
Child1.x = 3
print(Parent.x, Child1.x, Child2.x)

# 执行结果
# 1 1 1
# 1 1 2
# 1 3 2
"""

# 9，读代码写结果
"""
class Foo(object):
    n1 = '武沛齐'
    n2 = '金老板'

    def __init__(self):
        self.n1 = 'eva'


obj = Foo()
print(obj.n1)
print(obj.n2)

# 执行结果
# eva
# 金老板
"""

# 10，看代码写结果，如果有错误，则标注错误即可，并且假设程序报错可以继续执行
"""
class Foo(object):
    n1 = '武沛齐'

    def __init__(self, name):
        self.n2 = name


obj = Foo('太白')
print(obj.n1)
print(obj.n2)
print(Foo.n1)
print(Foo.n2)

# 执行结果
# 武沛齐
# 太白
# 武沛齐
# 报错------
"""


