# md5加密
import hashlib
import os

s1 = 'kfdslfjasdlfgjsdlgkhsdafkshdafjksdfsdkfhjsdafj老fhdskafhsdkjfdsa男孩教育'
ret = hashlib.md5()
ret.update(s1.encode('utf-8'))
print(ret.hexdigest())

"""
def MD5(pwd):
    ret = hashlib.md5()
    ret.update(pwd.encode('utf-8'))
    return ret.hexdigest()


def register():
    username = input('请输入用户名：').strip()
    password = input('请输入密码：').strip()
    password_md5 = MD5(password)
    with open('register', encoding='utf-8', mode='a') as f1:
        f1.write(f'\n{username}|{password_md5}')


register()
"""

# 普通加密
s2 = '19890425'
ret = hashlib.md5()
ret.update(s2.encode('utf-8'))
print(ret.hexdigest())  # 6e942d04cf7ceeeba09e3f2c7c03dc44

# 加盐
s2 = '19890425'
ret = hashlib.md5('abcde'.encode('utf-8'))
ret.update(s2.encode('utf-8'))
print(ret.hexdigest())  # 7dd0ae4819090756e3938ba73c5b3195

# 动态的盐
s2 = '19890425'
ret = hashlib.md5('abcde'[::2].encode('utf-8'))
ret.update(s2.encode('utf-8'))
print(ret.hexdigest())  # 1b29bf0c910f8c9494f7931fff2179df


# sha系列  金融类,安全类.用这个级别.
# 随着sha系列数字越高,加密越复杂,越不易破解,但是耗时越长.
s2 = 'fdsklgfjsdlgdsjlfkjsdalfksjdal90425'
ret = hashlib.sha3_512()
ret.update(s2.encode('utf-8'))
print(ret.hexdigest())  # 008d902308fb2926f8e4261951bf0b3bedfc1db9d2b3ec7b92803c6599b6eec31b5eb2a20cd2523a0e3e1b44b0ab045aac03206968a68f5cf2aed991c8c13d4e


# 文件的校验
# linux中一切皆文件: 文本文件,非文本文件,音频,视频,图片....
# 无论你下载的视频,还是软件(国外的软件),往往都会有一个md5值

"""
s1 = '我叫太白金星 今年18岁'
ret = hashlib.sha256()
ret.update(s1.encode('utf-8'))
print(ret.hexdigest())  # 54fab159ad8f0bfc5df726a70332f111c2c54d31849fb1e4dc1fcc176e9e4cdc

ret = hashlib.sha256()
ret.update('我叫'.encode('utf-8'))
ret.update('太白金星'.encode('utf-8'))
ret.update(' 今年'.encode('utf-8'))
ret.update('18岁'.encode('utf-8'))
print(ret.hexdigest())  # 54fab159ad8f0bfc5df726a70332f111c2c54d31849fb1e4dc1fcc176e9e4cdc
"""

# b6450e590a37c5bccf049b1176c441f0964796995e80d4c7c7d9fb74f9ad817107c303b6b83ed3d71c9251b2b8acf334b90a4abdf9deea122e338643cece0766 *apache-tomcat-9.0.41.tar.gz

# low版校验
"""
def file_md5(path):
    ret = hashlib.sha512()
    with open(path, mode='rb') as f1:
        b1 = f1.read()
        ret.update(b1)
    return ret.hexdigest()

result = file_md5('apache-tomcat-9.0.41.tar.gz')
print(result)
"""

# 高级版校验
def file_md5(path):
    ret = hashlib.sha512()
    byte_size = os.path.getsize('apache-tomcat-9.0.41.tar.gz')
    with open(path, mode='rb') as f1:
        while 1:
            content = f1.read(1024)
            if content:
                ret.update(content)
            else:
                return ret.hexdigest()

result = file_md5('apache-tomcat-9.0.41.tar.gz')
print(result)

