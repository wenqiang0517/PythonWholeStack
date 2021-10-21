class Authentic:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def register(self):
        print('注册')

    def login(self):
        print('登录')


l = [('登录', 'login'), ('注册', 'register'), ('名字', 'name')]
# 循环这个列表
# 显示 序号 用户要做的操作
# 用户输入序号
# 你通过序号找到对应的login或者register方法
# 先实例化
# 调用对应的方法,完成登录或者注册功能

for i, y in enumerate(l, 1):
    print(i, y[0])

while True:
    serial = input('请选择>>: ').strip()
    if 0 < int(serial) <= len(l):
        serial = int(serial)
        auth = Authentic('lwq', 18)
        if hasattr(auth, l[int(serial) - 1][1]):
            if callable(getattr(auth, l[int(serial) - 1][1])):
                operation = getattr(auth, l[int(serial) - 1][1])()
            else:
                print(getattr(auth, l[int(serial) - 1][1]))
        else:
            print("方法不存在")
    else:
        print('输入有误，请重新输入')


