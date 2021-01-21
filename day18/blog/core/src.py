import os
from conf import settings
from lib import common
user_status = {'name': None, 'status': False}


def user_dic():
    with open(settings.register, encoding='utf-8') as f:
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
                with open(settings.register, encoding='utf-8', mode='a') as f:
                    f.write(f'{username}|{password}\n')
                    print('注册成功')
            else:
                print('密码长度要在6~14个字符之间')
        else:
            print('用户名只能包含字母或者数字')


@common.auth
def article():
    print(f'欢迎{user_status["name"]}进入文章页面')
    while 1:
        choose = input('请选择 1,直接写入内容 2,导入md文件 3,退出: ')
        if choose.isdecimal():
            if choose == '1':
                file_name = input('请输入文件名：')
                file_content = input('请输入文件内容：')
                with open(f'{settings.article}/{file_name}', encoding='utf-8', mode='w') as f:
                    f.write(file_content)
                    f.write("""\n评论区：
-----------------------------------------""")
            elif choose == '2':
                file_name = input('请输入要导入的md文件路径：')
                with open(file_name, encoding='utf-8') as f, open(f'{file_name[:-3]}.txt', encoding='utf-8', mode='w') as f1:
                    for i in f:
                        f1.write(i)
                    f1.write("""\n评论区：
-----------------------------------------""")
                os.remove(file_name)
            elif choose == '3':
                break
            else:
                print('请输入1或2')
        else:
            print('输入有误')


@common.auth
def comment():
    file_dict = {}
    sensitive = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
    print(f'欢迎{user_status["name"]}进入评论页面')
    file_list = os.listdir(settings.article)
    for x, y in enumerate(file_list):
        file_dict[x+1] = y
    print(file_dict)
    while 1:
        serial = input('请选择要评论的文件(q或Q退出): ').strip()
        if serial.isdecimal():
            if int(serial) in file_dict.keys():
                with open(f'{settings.article}/{file_dict[int(serial)]}', encoding='utf-8', mode='r+') as f:
                    for i in f:
                        print(i.strip())
                    user_comment_ = input('请输入你的评论：').strip()
                    for i in sensitive:
                        if i in user_comment_:
                            user_comment_ = user_comment_.replace(i, '*' * len(i))
                    print(user_comment_)
                    f.write(f'\n{user_status["name"]}:\n')
                    f.write(f'{user_comment_}')
            else:
                print('输入序号不在范围')
        elif serial.upper() == 'Q':
            break
        else:
            print('输入有误，重新输入')


@common.auth
def diary():
    print(f'欢迎{user_status["name"]}进入日记页面')


@common.auth
def collect():
    print(f'欢迎{user_status["name"]}进入收藏页面')


@common.auth
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
