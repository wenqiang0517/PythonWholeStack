# 组合
    # 一个类的对象是另外一个类对象的属性

# 学生类
    # 姓名 性别 年龄 学号 班级 手机号
# 班级信息
    # 班级名字
    # 开班时间
    # 当前讲师
# class Student:
#     def __init__(self,name,sex,age,number,clas,phone):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.number = number
#         self.clas = clas
#         self.phone = phone
# class Clas:
#     def __init__(self,cname,begint,teacher):
#         self.cname = cname
#         self.begint = begint
#         self.teacher = teacher

# 查看的是大壮的班级的开班日期是多少
# 查看的是雪飞的班级的开班日期是多少
# py22 = Clas('python全栈22期','2019-4-26','小白')
# py23 = Clas('python全栈23期','2019-5-28','宝元')
# 大壮 = Student('大壮','male',18,27,py23,13812012012)
# 雪飞 = Student('雪飞','male',18,17,py22,13812012013)
# print(大壮.clas,py23)
# print(py23.begint)
# print(大壮.clas.begint)



# 练习 :
# 对象变成了一个属性
# 班级类
    # 包含一个属性 - 课程
# 课程
    # 课程名称
    # 周期
    # 价格
# 创建两个班级 linux57
# 创建两个班级 python22
# 查看linux57期的班级所学课程的价格
# 查看python22期的班级所学课程的周期

class Clas:
    def __init__(self, teacher):
        self.teacher = teacher


class Course:
    def __init__(self, course_name, period, price):
        self.course_name = course_name
        self.period = period
        self.price = price


linux57 = Clas('lwq')
python22 = Clas('alex')
linux = Course('linux', 10, 10000)
python = Course('python', 20, 20000)
linux57.course = linux
python22.course = python

linux.price = 30000
print(linux57.course.price, linux57.course.period)
print(python22.course.price, python22.course.period)


