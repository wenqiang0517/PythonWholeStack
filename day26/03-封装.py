# 封装 :就是把属性或者方法装起来

# 广义 :把属性和方法装起来,外面不能直接调用了,要通过类的名字来调用
# 狭义 :把属性和方法藏起来,外面不能调用,只能在内部偷偷调用
# class User:
#     def __init__(self,name,passwd):
#         self.usr = name
#         self.__pwd = passwd  # 私有的实例变量/私有的对象属性
# alex = User('alex','sbsbsb')
# print(alex.__pwd)  # 报错
# print(alex.pwd)    # 报错

# 给一个名字前面加上了双下划线的时候,这个名字就变成了一个私有的
# 所有的私有的内容或者名字都不能在类的外部调用,只能在类的内部使用了

# class User:
#     def __init__(self,name,passwd):
#         self.usr = name
#         self.__pwd = passwd  # 私有的实例变量/私有的对象属性
#     def get_pwd(self):       # 表示的是用户不能改只能看 私有 + 某个get方法实现的
#         return self.__pwd
#     def change_pwd(self):    # 表示用户必须调用我们自定义的修改方式来进行变量的修改 私用 + change方法实现
#         pass

# class User:
#     __Country = 'China'   # 私有的静态变量
#     def func(self):
#         print(User.__Country)  # 在类的内部可以调用
# print(User.Country)  # 报错 在类的外部不能调用
# print(User.__Country)# 报错 在类的外部不能调用
# User().func()
# import  hashlib
# class User:
#     def __init__(self,name,passwd):
#         self.usr = name
#         self.__pwd = passwd  # 私有的实例变量
#     def __get_md5(self):     # 私有的绑定方法
#         md5 = hashlib.md5(self.usr.encode('utf-8'))
#         md5.update(self.__pwd.encode('utf-8'))
#         return md5.hexdigest()
#     def getpwd(self):
#         return self.__get_md5()
# alex = User('alex','sbsbsb')
# print(alex.getpwd())

# 所有的私有化都是为了让用户不在外部调用类中的某个名字
# 如果完成私有化 那么这个类的封装度就更高了 封装度越高各种属性和方法的安全性也越高 但是代码越复杂

