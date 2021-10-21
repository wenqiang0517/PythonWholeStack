class User:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('eat')

    def sleep(self):
        print('sleep')

# 用户输入用户名密码性别
# 实例化对象
# 用户任意输入内容 : 不能用异常处理
# 如果输入的是属性名 打印属性值
# 如果输入的是方法名 调用fangfa
# 如果输入的什么都不是 不做操作


user_name = input('请输入用户名: ')
user_age = input('请输入年龄: ')
user_sex = input('请输入性别: ')

user = User(user_name, user_age, user_sex)

while True:
    content = input('请任意输入内容: ')
    if hasattr(user, content):
        if callable(getattr(user, content)):
            result = getattr(user, content)()
        else:
            print(getattr(user, content))




