from core import src


def auth(func):
    def inner(*args, **kwargs):
        if src.user_status['status']:
            func(*args, **kwargs)
        else:
            print('请先登陆')
    return inner
