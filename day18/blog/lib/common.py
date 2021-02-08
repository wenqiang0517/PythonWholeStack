import json
from conf import settings


def read_user_status():
    with open(settings.user_status, encoding='utf-8') as f:
        user_status = json.load(f)
    return user_status


def write_user_status(user_status):
    with open(settings.user_status, encoding='utf-8', mode='w') as f:
        json.dump(user_status, f)


def auth(func):
    def inner(*args, **kwargs):
        user_status = read_user_status()
        if user_status['status']:
            func(*args, **kwargs)
        else:
            print('请先登陆')
    return inner
