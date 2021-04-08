# 先匹配小括号里的内容, 然后先计算乘除法, 再计算加减法, 用循环用正则, 调用函数
# exp = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))'
import re


def mul_div(exp):
    if '*' in exp:
        a, b = exp.split('*')
        return float(a) * float(b)
    if '/' in exp:
        a, b = exp.split('/')
        return float(a) / float(b)


def add_subtract(exp):
    if '+' in exp:
        a, b = exp.split('+')
        return float(a) + float(b)
    if '-' in exp:
        a, b = exp.split('-')
        return float(a) - float(b)


def func(exp):
    while True:
        re_exp = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?', exp)
        if re_exp:
            son_exp = re_exp.group()
            ret = mul_div(son_exp)
            exp = exp.replace(son_exp, str(ret))
            print(exp)
        else:
            re_exp = re.search('\d+(\.\d+)?[-+]-?\d+(\.\d+)?', exp)
            if re_exp:
                son_exp = re_exp.group()
                ret = add_subtract(son_exp)
                exp = exp.replace(son_exp, str(ret))
                print(exp)
            else:
                break
    return exp

exp = '1+3*4*5/6-4-7'
ret = func(exp)
print(ret)



