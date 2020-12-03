# 1, 新特性
name = '太白'
age = 18
msg = f'我叫{name},今年{age}'
print(msg)

# 2, 可以加表达式
dic = {'name': 'alex', 'age': 111}
msg = f'我叫{dic["name"]},今年{dic["age"]}'
print(msg)

count = 7
print(f'最终结果：{count**2}')
name = 'barry'
msg = f'我的名字是{name.upper()}'
print(msg)

# 3, 结合函数写
def _sum(a, b):
    return a+b
msg = f'最终结果：{_sum(10, 20)}'
print(msg)

# ! , : {} ; 这些标点不能出现在{ }里面
# 优点：
#     1，结构更加简化
#     2，可以结合表达式，函数进行使用
#     3，效率提升很多



