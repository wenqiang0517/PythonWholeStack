# 第二次周末大作业：博客园
# 作业：用代码模拟博客园系统。
# 项目分析：
# 一．首先程序启动，页面显示下面内容供用户选择：
# 1. 请登录
# 2. 请注册
# 3. 进入文章页面
# 4. 进入评论页面
# 5. 进入日记页面
# 6. 进入收藏页面
# 7. 注销账号
# 8. 退出整个程序

# 二．必须实现的功能：
# \1. 注册功能要求：
# a.用户名、密码要记录在文件中。
# b.用户名要求：只能含有字母或者数字不能含有特殊字符并且确保用户名唯一。
# c.密码要求：长度要在6~14个字符之间。
import os
import sys
user_status = {'name': None, 'status': False}
user_comment = {}

def user_dic():
    with open('user.txt', encoding='utf-8') as f:
        user_dic_ = {}
        for i in f:
            i = i.strip().split('|')
            user_dic_[i[0]] = i[1]
    print(user_dic_)
    return user_dic_


def login():
    global user_status
    user_dic_ = user_dic()
    for i in range(3):
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        if username in user_dic_.keys():
            if user_dic_[username] == password:
                print('登陆成功')
                user_status.update(name=username, status=True)
                return username
            else:
                print('密码错误')
                user_status.update(name=username, status=False)
        else:
            print('用户名不存在')
    else:
        exit_s()


def register():
    user_dic_ = user_dic()
    username = input('请输入用户名：').strip()
    password = input('请输入密码：').strip()
    if username in user_dic_.keys():
        print('用户名已存在，请重新输入')
    else:
        if username.isalnum():
            if 5 < len(password) < 15:
                with open('user.txt', encoding='utf-8', mode='a') as f:
                    f.write(f'{username}|{password}\n')
                    print('注册成功')
            else:
                print('密码长度要在6~14个字符之间')
        else:
            print('用户名只能包含字母或者数字')


def auth(func):
    def inner(*args, **kwargs):
        if user_status['status']:
            func(*args, **kwargs)
        else:
            print('请先登陆')
            # login()
    return inner


@auth
def article():
    print(f'欢迎{user_status["name"]}进入文章页面')
    while 1:
        choose = input('请选择 1,直接写入内容 2,导入md文件 3,退出: ')
        if choose.isdecimal():
            if choose == '1':
                file_name = input('请输入文件名：')
                file_content = input('请输入文件内容：')
                with open(file_name, encoding='utf-8', mode='w') as f:
                    f.write(file_content)
            elif choose == '2':
                file_name = input('请输入要导入的md文件路径：')
                with open(file_name, encoding='utf-8') as f, open(f'{file_name[:-3]}.txt', encoding='utf-8', mode='w') as f1:
                    for i in f:
                        f1.write(i)
                os.remove(file_name)
            elif choose == '3':
                break
            else:
                print('请输入1或2')
        else:
            print('输入有误')


@auth
def comment():
    global user_comment
    file_dict = {}
    sensitive = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
    print(f'欢迎{user_status["name"]}进入评论页面')
    file_list = os.listdir(r'article/')
    for x, y in enumerate(file_list):
        file_dict[x+1] = y
    print(file_dict)
    while 1:
        serial = input('请选择要评论的文件: ').strip()
        if serial.isdecimal():
            if int(serial) in file_dict.keys():
                with open(f'article/{file_dict[int(serial)]}', encoding='utf-8') as f:
                    for i in f:
                        print(i.strip())
                print("""评论区：
-----------------------------------------""")
                if file_dict[int(serial)] in user_comment.keys():
                    for i in user_comment[file_dict[int(serial)]]:
                        for x, y in i.items():
                            print(f"""{x}:
{y}""")
                else:
                    pass
                user_comment_ = input('请输入你的评论：').strip()
                for i in sensitive:
                    if i in user_comment_:
                        user_comment_ = user_comment_.replace(i, '*' * len(i))
                print(user_comment_)
                print(file_dict[int(serial)])
                print({user_status["name"]: user_comment_})
                print(user_comment[file_dict[int(serial)]])
                # user_comment[file_dict[int(serial)]] = user_comment[file_dict[int(serial)]].append({user_status["name"]: user_comment_})
            else:
                print('输入序号不在范围')
        else:
            print('输入有误，重新输入')

@auth
def diary():
    print(f'欢迎{user_status["name"]}进入日记页面')

@auth
def collect():
    print(f'欢迎{user_status["name"]}进入收藏页面')

@auth
def logout():
    print('注销账号')
    user_status['status'] = False


def exit_s():
    exit()


def run():
    options = {1: ['请登录', login], 2: ['请注册', register], 3: ['进入文章页面', article], 4: ['进入评论页面', comment],
               5: ['进入日记页面', diary], 6: ['进入收藏页面', collect], 7: ['注销账号', logout], 8: ['退出整个程序', exit_s]}
    while 1:
        for x, y in options.items():
            print(f'{x}. {y[0]}')
        choose = input('请选择：').strip()
        if choose.isdecimal():
            if int(choose) in options.keys():
                options[int(choose)][1]()
            else:
                print('输入不在范围')
        else:
            print('输入有误，请重新输入')


run()

# \2. 登录功能要求：
# a.用户输入用户名、密码进行登录验证
# b.登录成功之后，才可以访问3~7选项，如果没有登录或者登录不成功时访问3~7选项，不允许访问，让其先登录。（装饰器）
# c.超过三次登录还未成功，则退出整个程序

# \3. 进入文章页面要求：
# a.提示欢迎xx进入文章页面。
# b.此时用户可以选择：直接写入内容，还是导入md文件。
# ①如果选择直接写内容：让学生直接写文件名 | 文件内容......最后创建一个文章。
# ②如果选择导入md文件：让用户输入已经准备好的md文件的文件路径（相对路径即可：比如函数的进阶.md），然后将此md文件的全部内容写入文章（函数的进阶.text）中。

# \4. 进入评论页面要求：提示欢迎xx进入评论页面。
# \5. 进入日记页面要求：提示欢迎xx进入日记页面。
# \6. 进入收藏页面要求：提示欢迎xx进入收藏页面。
# \7. 注销账号要求：不是退出整个程序，而是将已经登录的状态变成未登录状态（访问3~7选项时需要重新登录）。
# \8. 退出整个程序要求：就是结束整个程序。

# 三． ** 选做功能 **：
# \1. 评论页面要求：
# a.提示欢迎xx进入评论页面
# b.让用户选择要评论的文章
# 这个需要借助于os模块实现此功能。将所有的文章文件单独放置在一个目录中，利用os模块listdir功能, 可以将一个目录下所有的文件名以字符串的形式存在一个列表中并返回。
# 例如：在 article 目录下存放文件
# 代码：
# import os
# print(os.listdir(r'D:\teaching_show\article'))    # ['01 函数的初识.text', '02 函数的进阶.text']

# c.选择要评论的文章之后，先要将原文章内容全部读一遍，然后输入的你的评论，评论要过滤掉这些敏感字符：
# "苍老师", "东京热", "武藤兰", "波多野结衣"，替换成等长度的 "*" 之后，写在文章的评论区最下面。
# 文章的结构：
# 文章具体内容
# .......

# 评论区：
# -----------------------------------------
# ​          (用户名) xx:
# ​          评论内容
# ​          (用户名) oo:
# ​          评论内容

# 原文章最下面如果没有以下两行：
# 评论区：
# -----------------------------------------

# 就加上这两行在写入评论，如果有这两行则直接在下面顺延写上：
# (用户名) xx:
# ​    评论内容

