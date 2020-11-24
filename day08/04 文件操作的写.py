# w
# 没有文件，创建文件，写入内容
# f = open('文件的写', encoding='utf-8', mode='w')
# f.write('随意ssssss')
# f.close()

# 如果文件存在，先清空源文件内容，在写入新内容
# f = open('文件的写', encoding='utf-8', mode='w')
# f.write('saddadasadadas')
# f.close()

# wb
f = open('佩恩.jpg', mode='rb')
content = f.read()
f.close()

f1 = open('佩恩2.jpg', mode='wb')
f1.write(content)
f1.close()

