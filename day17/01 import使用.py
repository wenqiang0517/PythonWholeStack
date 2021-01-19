import tbjx

name = 'alex'
print(name)
print(tbjx.name)
'''
from the tbjx.py
alex
太白金星
'''


def read1():
    print(666)


tbjx.read1()
'''
from the tbjx.py
tbjx模块： 太白金星
'''

name = '日天'
tbjx.change()
print(name)
print(tbjx.name)
'''
from the tbjx.py
日天
barry
'''

# import tbjx as sm
# print(sm.name)
#
# 了解

# 原始写法
# result = input('请输入')
# if result == 'mysql':
#     import mysql1
#     mysql1.mysql()
# elif result == 'oracle':
#     import oracle1
#     oracle1.oracle()
# list.index()
# str.index()
# tuple.index()
# 起别名
# result = input('请输入')
# if result == 'mysql':
#     import mysql1 as sm
# elif result == 'oracle':
#     import oracle1 as sm
# ''' 后面还有很多'''
# sm.db()  # 统一接口,归一化思想
import time, os, sys  # 这样写不好
import time
import os
import sys

