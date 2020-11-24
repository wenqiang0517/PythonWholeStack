# read 全部读出来 **
# f = open('文件的读', encoding='utf-8')
# content = f.read()
# print(content)
# f.close()

# read(n) 按照字符读取
# f = open('文件的读', encoding='utf-8')
# content = f.read(8)
# print(content)
# f.close()

# readline()  一行行的读
# f = open('文件的读', encoding='utf-8')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# readlines()   返回一个列表，列表中的每个元素是源文件的每一行
# f = open('文件的读', encoding='utf-8')
# l1 = f.readlines()
# for line in l1:
#     print(line)
# print(l1)
# f.close()

# for 读取  ******
f = open('文件的读', encoding='utf-8')
for line in f:
    print(line)
f.close()

# rb
f = open('佩恩.jpg', mode='rb')
content = f.read()
print(content)
f.close()
