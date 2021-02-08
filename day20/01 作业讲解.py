import re
# 1、匹配整数或者小数（包括正数和负数）
# -?[1-9]+(.\d+)

# 2、匹配年月日日期 格式2018-12-6
# [1-9]\d+-[1-9][0-2]?-[1-9]\d?

# 3、匹配qq号
# [1-9]\d{5,10}

# 4、11位的电话号码
# 1\d{10}

# 5、长度为8-10位的用户密码 ： 包含数字字母下划线
# \w{8,10}

# 6、匹配验证码：4位数字字母组成的
# [\d|a-z|A-Z]{4}

# 7、匹配邮箱地址
# [1-9|a-z|A-Z]+@.+\.(com|cn)

# 8、从类似 这样的字符串中，
# <a>wahaha</a>
# <b>banana</b>
# <h1>qqxing</h1>
# 1）匹配出wahaha，banana，qqxing内容。
ret = re.findall('>(.+)<', """<a>wahaha</a> 
<b>banana</b>
<h1>qqxing</h1>""")
print(ret)

# 2）匹配出a,b,h1这样的内容
ret = re.findall('</(.+)>', """<a>wahaha</a> 
<b>banana</b>
<h1>qqxing</h1>""")
print(ret)

# 9、1-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-3*2))
# 1）从上面算式中匹配出最内层小括号以及小括号内的表达式
ret = re.findall('\([^()]+\)', '1-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-4*3)/(16-3*2))')
print(ret)

# 10、从类似9-25/3+7/399/42998+10568/14的表达式中匹配出从左到右第一个乘法或除法
ret = re.search('\d+[/*]\d+', '9/25*3+7/399/42998+10568/14')
print(ret.group())

