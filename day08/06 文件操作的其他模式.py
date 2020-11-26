# 读并追加，顺序不能错误
f = open('文件的读写', encoding='utf-8', mode='r+')
content = f.read()
print(content)
f.write('的反馈给你带给你')
f.close()


# 错误示例
# f = open('文件的读写', encoding='utf-8', mode='r+')
# f.write('先写，在读')
# content = f.read()
# print(content)
# f.close()


