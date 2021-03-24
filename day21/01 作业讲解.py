# 1、匹配一篇英文文章的标题 类似 The Voice Of China
# ([A-Z]{1}[a-z]+\s)+([A-Z]{1}[a-z]+)

# 2、匹配一个网址
# ([a-z]+).([a-z]+).([a-z]+)


# 4、匹配15位或者18位身份证号


# 5、从lianjia.html（html文件在群文件中）中匹配出标题，户型和面积，结果如下：
# [('金台路交通部部委楼南北大三居带客厅   单位自持物业', '3室1厅', '91.22平米'), ('西山枫林 高楼层南向两居 户型方正 采光好', '2室1厅', '94.14平米')]
# import re
# par = '<div class="title">.*?<a class=.*?>(?P<name>.*?)</a>.*?<span class="divide">/</span>(?P<room>.*?)<span class="divide">.*?>(?P<size>.*?)<span class="divide">'
# with open('lianjia.html', encoding='utf-8') as f:
#     content = f.read()
# ret = re.findall(par, content, flags=re.S)
# print(ret)


# 递归相关
# 1.计算阶乘 100! = 100*99*98*97*96....*1
# def fin(n):
#     if n == 1:
#         return n
#     else:
#         return n * fin(n-1)
# print(fin(10))

# 1.os模块:查看一个文件夹下的所有文件,这个文件夹下面还有文件夹,不能用walk
import os
# def func(path):
#     ret = os.listdir(path)
#     for i in ret:
#         abs_path = os.path.join(path, i)
#         if os.path.isdir(abs_path):
#             func(abs_path)
#         else:
#             print(i)
# func('/Users/luwenqiang/Documents/lwq/PythonProject/PythonWholeStack')


# 2.os模块:计算一个文件夹下所有文件的大小.这个文件夹下面还有文件夹,不能用walk
def func(path):
    size = 0
    ret = os.listdir(path)
    for i in ret:
        abs_path = os.path.join(path, i)
        if os.path.isdir(abs_path):
            ret = func(abs_path)
            size += ret
        else:
            size += os.path.getsize(abs_path)
    return size

# func('/Users/luwenqiang/Documents/lwq/PythonProject/PythonWholeStack')
# print(func('C://Program Files (x86)//Python//PythonWholeStack'))

# 3.计算斐波那契数列
    # 找第100个数
    # 1 1 2 3 5

# 递归
# def func(n, a=1, b=1):
#     if n == 1 or n == 2:
#         return b
#     else:
#         return func(n-1, b, a + b)
# print(func(10))


# 循环
# def func(n):
#     a, b = 1, 1
#     while n > 2:
#         a, b = b, a + b
#         n -= 1
#     return b
# print(func(10))


# 4.三级菜单 可能是n级
    # 递归 循环
    # https://www.cnblogs.com/Eva-J/articles/7205734.html#_label4
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}


def func(menu):
    for i in menu:
        print(i)
    city = input('>>>')
    func(menu[city])
func(menu)



