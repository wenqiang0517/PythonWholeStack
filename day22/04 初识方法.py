class Person:  # 类名
    def __init__(self, name, sex, job, hp, weapon, ad):
        # 必须叫__init__这个名字,不能改变的,所有的在一个具体的人物出现之后拥有的属性
        self.name = name  # 对象的属性/实例变量
        self.sex = sex
        self.hp = hp
        self.ad = ad

    def hit(self, dog):  # 方法,又有一个必须传的参数-->self对象
        dog.hp -= self.ad
        print('%s给%s搓了澡, %s掉了%s点血, %s当前血量%s' % (self.name, dog.dog_name, dog.dog_name, self.ad, dog.dog_name, dog.hp))


class Dog:
    def __init__(self, name, blood, aggr, kind):
        self.dog_name = name
        self.hp = blood
        self.ad = aggr
        self.kind = kind

    def bite(self, person):
        print(self.__dict__)
        print(person.__dict__)
        person.hp -= self.ad
        print('%s给%s咬了, %s掉了%s点血, %s当前血量%s' % (self.dog_name, person.name, person.name, self.ad, person.name, person.hp))


alex = Person('alex', '不详', '搓澡工', 260, '搓澡巾', 1)  # 对象\实例 = 类名() -->  实例化的过程
print('alex : ', alex)
small_write = Dog('小白', 5000, 249, '柴犬')
alex.hit(small_write)
small_write.bite(alex)
# small_write.bite(alex)




