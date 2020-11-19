# bytes
b = b'hello'
print(b.upper())    # b'HELLO'
print(b, type(b))   # b'hello' <class 'bytes'>

s1 = '中国'
b1 = b'\xe4\xb8\xad\xe5\x9b\xbd'
print(b1)

# str ---> bytes
s1 = '中国'
b1 = s1.encode('utf-8')  # 编码
print(b1, type(b1))  # b'\xe4\xb8\xad\xe5\x9b\xbd'  <class 'bytes'>
b1 = s1.encode('gbk')  # 编码  b'\xd6\xd0\xb9\xfa'
# bytes ---> str
b1 = b'\xe4\xb8\xad\xe5\x9b\xbd'
s1 = b1.decode('utf-8')  # 解码
print(s1)  # 中国

# gbk ---> utf-8
b1 = b'\xd6\xd0\xb9\xfa'
s = b1.decode('gbk')
b2 = s.encode('utf-8')
print(b2)  # b'\xe4\xb8\xad\xe5\x9b\xbd'

# 英文:
#     str: 'hello'
#         内存中的编码方式: Unicode
#         表现形式: 'hello'
#     bytes:
#         内存中的编码方式: 非Unicode
#         表现形式: b'hello'

# 中文:
#     str: '中国'
#         内存中的编码方式：Unicode
#         表现形式: '中国'
#     bytes:
#         内存中的编码方式：非Unicode # utf-8
#         表现形式: b'\xe4\xb8\xad\xe5\x9b\xbd'

