# 面向对象的思想
# 类 对象实例 实例化
# 方法 实例变量

# class语法 __init__方法
# self __dict__

# 算法
# 二分查找  [1,2,3,4,5,6,7,8,9,10,27,36,46,58,69] - 有序列表
# in index 从列表中找到一个值的位置
# 实现上面的功能 - 用代码
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 27, 36, 46, 58, 69]


def func(lis, number):
    mid_number = (len(lis) - 1) // 2
    if number > lis[mid_number]:
        new_lis = lis[mid_number - 1:]
        func(new_lis, number)
    elif number < lis[mid_number]:
        new_lis = lis[:mid_number]
        func(new_lis, number)
    else:
        return mid_number


print(func(lis, 1))
# sys.argv练习
# 写一个python脚本,在cmd里执行
# python xxx.py 用户名 密码 cp 文件路径 目的地址
# python xxx.py alex sb cp D:\python_22\day22\1.内容回顾.py D:\python_22\day21
# python xxx.py alex sb rm D:\python_22\day22
# python xxx.py alex sb rename D:\python_22\day22  D:\python_22\day23

# -*- coding: utf-8 -*-
# sys.argv练习
# 写一个python脚本,在cmd里执行
# python xxx.py 用户名 密码 cp 文件路径 目的地址
# python xxx.py alex sb cp D:\python_22\day22\1.内容回顾.py D:\python_22\day21
# python xxx.py alex sb rm D:\python_22\day22
# python xxx.py alex sb rename D:\python_22\day22  D:\python_22\day23

import sys
import shutil
lis = sys.argv
# print(lis)

dic = {'cp': shutil.copytree, 'rm': shutil.rmtree, 'rename': shutil.move}


def auth(lis):
    if lis[1] == 'alex' and lis[2] == 'sb':
        print('ok')
    else:
        print('用户名或密码错误')


def operation(lis):
    if lis[3] in dic:
        dic[lis[3]](lis[4])
    else:
        print('没有这个操作权限')


auth(lis)
operation(lis)







# 使用walk来计算文件夹的总大小
# import os
#
# count = 0
# g = os.walk('/Users/luwenqiang/Documents/lwq/PythonProject/PythonWholeStack')
# for i in g:
#     path, dir_lst, name_lst = i
#     for x in name_lst:
#         count += os.path.getsize(os.path.join(path, x))
# print(count)

# 定义一个圆形类,半径是这个圆形的属性,实例化一个半径为5的圆形,一个半径为10的圆形
#     完成方法
# 计算圆形面积
# 计算圆形周长
class Round:
    def __init__(self, radius):
        self.round_radius = radius

    def round_area(self):
        area = 3.14159 * (self.round_radius ** 2)
        return area

    def round_perimeter(self):
        perimeter = 2 * 3.14159 * self.round_radius
        return perimeter


radius5 = Round(5)
print(radius5.round_radius, f'面积：{radius5.round_area()}，周长：{radius5.round_perimeter()}')

radius_10 = Round(10)
print(radius_10.round_radius, f'面积：{radius_10.round_area()}，周长：{radius_10.round_perimeter()}')

# 定义一个用户类,用户名和密码是这个类的属性,实例化两个用户,分别有不同的用户名和密码
# 登陆成功之后才创建用户对象
# 设计一个方法 修改密码


# 继续完成人狗大战
# 你是人
# 狗是一个npc
# 你一个回合  狗一个回合
# 狗掉的血是一个波动值
# 闪避概率

# 继续完成计算器
