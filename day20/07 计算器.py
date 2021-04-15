# 先匹配小括号里的内容, 然后先计算乘除法, 再计算加减法, 用循环用正则, 调用函数
# exp = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
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


def match_add_subtract(exp):
    re_exp = re.search('-?\d+(\.\d+)?[-+]-?\d+(\.\d+)?', exp)
    if re_exp:
        son_exp = re_exp.group()
        ret = add_subtract(son_exp)
        exp = exp.replace(son_exp, str(ret))
        print(exp)
        return exp
    else:
        return exp


def match_mul_div(exp):
    re_exp = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?', exp)
    if re_exp:
        son_exp = re_exp.group()
        result = mul_div(son_exp)
        new_exp = exp.replace(son_exp, str(result))
        print(new_exp)
        return new_exp
    else:
        return exp


def func(exp):
    re_exp = re.search('\((-?\d+[^(]*?-?\d+)\)', exp)
    if re_exp:
        son_exp = re_exp.group(1)
        while True:
            if '*' in son_exp or '/' in son_exp:
                son_exp = match_mul_div(son_exp)
            else:
                son_exp = match_add_subtract(son_exp)
                print(son_exp)
                new_exp = exp.replace(re_exp, str(son_exp))
                return new_exp


exp = '1-2*((60-30+(-40/5-5-23+12/3)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
result = func(exp)
print(result)



