# -*- coding: utf-8 -*-
# 1, 二分查找  [1,2,3,4,5,6,7,8,9,10,27,36,46,58,69] - 有序列表
# in index 从列表中找到一个值的位置
# 实现上面的功能 - 用代码
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 27, 36, 46, 58, 69]
# def func(lis, number):
#     mid_number = (len(lis) - 1) // 2
#     if number > lis[mid_number]:
#         new_lis = lis[mid_number - 1:]
#         func(new_lis, number)
#     elif number < lis[mid_number]:
#         new_lis = lis[:mid_number]
#         func(new_lis, number)
#     else:
#         return mid_number
# print(func(lis, 1))


# 2, 写一个python脚本, 在cmd里执行, sys.argv练习
# python xxx.py 用户名 密码 cp 文件路径 目的地址
# python xxx.py alex sb cp D:\python_22\day22\1.内容回顾.py D:\python_22\day21
# python xxx.py alex sb rm D:\python_22\day22
# python xxx.py alex sb rename D:\python_22\day22  D:\python_22\day23


import sys
import os
import shutil
lis = sys.argv

if len(lis) >= 4:
    if lis[1] == 'alex' and lis[2] == 'sb':
        if lis[3] == 'rm' and len(lis) == 5:
            if os.path.isfile(lis[4]):
                os.remove(lis[4])
            else:
                shutil.rmtree(lis[4])
        elif lis[3] == 'cp' and len(lis) == 6:
            if os.path.isfile(lis[4]):
                shutil.copy2(lis[4], lis[5] + '/' + os.path.basename(lis[4]))
            else:
                shutil.copytree(lis[4], lis[5])
        elif lis[3] == 'rename' and len(lis) == 6:
            os.rename(lis[4], lis[5])
        else:
            print('参数错误或不足')
    else:
        print('用户名或密码错误')
else:
    print('参数不足，请补充')


# 3, 使用walk来计算文件夹的总大小
"""
import os

count = 0
g = os.walk('/Users/luwenqiang/Documents/lwq/PythonProject/PythonWholeStack')
for i in g:
    path, dir_lst, name_lst = i
    for x in name_lst:
        count += os.path.getsize(os.path.join(path, x))
print(count)
"""

# 4, 定义一个圆形类,半径是这个圆形的属性,实例化一个半径为5的圆形,一个半径为10的圆形
# 完成方法
# 计算圆形面积
# 计算圆形周长
"""
class Round:
    def __init__(self, radius):
        self.round_radius = radius

    def round_area(self):
        area = 3.14159 * (self.round_radius ** 2)
        return area

    def round_perimeter(self):
        perimeter = 2 * 3.14159 * self.round_radius
        return perimeter


radius_ = Round(5)
print(radius_.round_radius, f'面积：{radius_.round_area()}，周长：{radius_.round_perimeter()}')
radius_.round_radius = 10
print(radius_.round_radius, f'面积：{radius_.round_area()}，周长：{radius_.round_perimeter()}')
"""


# 5, 定义一个用户类,用户名和密码是这个类的属性,实例化两个用户,分别有不同的用户名和密码
# 登陆成功之后才创建用户对象
# 设计一个方法 修改密码
"""
import os


def login(username, password):
    with open('user', encoding='utf8') as f1:
        for i in f1:
            user, pwd = i.strip().split('|')
            if username == user and password == pwd:
                print('登陆成功')
                return True
    print('登陆失败')
    return False


class User:
    def __init__(self, username, pwd):
        self.username = username
        self.password = pwd

    def change_pwd(self):
        new_pwd = input('请输入新密码')
        with open('user', encoding='utf8') as f1, open('user.bak', mode='w', encoding='utf8') as f2:
            for i in f1:
                user, pwd = i.strip().split('|')
                if self.username == user:
                    f2.write(username + '|' + new_pwd + '\n')
                else:
                    f2.write(i)
        os.remove('user')
        os.renames('user.bak', 'user')


username = input('请输入用户名').strip()
password = input('请输入密码').strip()
ret = login(username, password)
if ret:
    alex = User(username, password)
    alex.change_pwd()
    print('修改成功')
"""


# 6, 继续完成人狗大战
# 你是人
# 狗是一个npc
# 你一个回合  狗一个回合
# 狗掉的血是一个波动值
# 闪避概率
