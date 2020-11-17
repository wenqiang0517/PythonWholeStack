# 请将列表中的每个元素通过"_"链接起来
user = ['剑圣', '盖伦', '小炮']
print('_'.join(user))

# 请将列表中的每个元素通过"_"链接起来
user = ['剑圣', '盖伦', 4543, '小炮']
s1 = ''
for i in range(len(user)):
    if i == 0:
        s1 += str(user[i])
    else:
        s1 = s1 + '_' + str(user[i])
print(s1)

# 请将元组 v1 中的所有元素追加到列表 v2 中
v1 = (11, 22, 33)
v2 = [44, 55, 66]
v2.extend(v1)
print(v2)

# 元组 v1 所有偶数索引位置的元素 追加到list v2
v1 = (11, 22, 33, 44, 55, 66, 77, 88, 99)
v2 = [44, 55, 66]
v2.extend(v1[::2])
print(v2)

# 将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
key_list = []
value_list = []
info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
key_list.extend(info.keys())
value_list.extend(info.values())
print(key_list, value_list)

# dic = {'k1': 'v1', 'k2': 'v2', 'k3': [11, 22, 33]}

av_catalog = {
    "欧美": {
        "www.太白.com": ["很多免费的，世界最大的", "质量一般"],
        "www.alex.com": ["很多免费的，也很大", "质量挺好"],
        "oldboy.com": ["多是自拍，高质量图片很多", "资源不多，更新慢"],
        "hao222.com": ["质量很高，真的很高", "全部收费，屌丝请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎么样不清楚，个人已经不喜欢日韩范了", "verygood"]
    },
    "大陆": {
        "1024": ["全部免费，真好，好人一生平安", "服务器在国外，慢"]
    }
}
# ["很多免费的，世界最大的", "质量一般"] list 第二个位置插入元素 '量很大'
av_catalog["欧美"]["www.太白.com"].insert(1, '量很大')
print(av_catalog)
# ["质量很高，真的很高", "全部收费，屌丝请绕过"]  list 中 "全部收费，屌丝请绕过" 删除
av_catalog["欧美"]["hao222.com"].pop(-1)
print(av_catalog)
# ["质量怎么样不清楚，个人已经不喜欢日韩范了", "verygood"] list "verygood" 全部变大写
av_catalog["日韩"]["tokyo-hot"][1] = av_catalog["日韩"]["tokyo-hot"][1].upper()
print(av_catalog)
# "大陆" 对应的dict 加一个键值对 '1048':['一天就封了']
av_catalog["大陆"].setdefault('1048', ['一天就封了'])
print(av_catalog)
# 删除键值对 "oldboy.com": ["多是自拍，高质量图片很多", "资源不多，更新慢"]
av_catalog["欧美"].pop("oldboy.com")
print(av_catalog)
# ["全部免费，真好，好人一生平安", "服务器在国外，慢"] list 第一个元素加上一句话  '可以爬下来'
av_catalog["大陆"]["1024"][0] += ',可以爬下来'
print(av_catalog)

# 循环打印k2对应的值中的每个元素
info = {
    'k1': 'v1',
    'k2': [('alex'), ('wupeiqi'), ('oldboy')],
}
for i in info['k2']:
    print(i)

# 字符串 "k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k1':1,'k2':2.....}
s1 = "k: 1|k1:2|k2:3 |k3 :4"
dic1 = {}
for i in s1.replace(' ', '').split('|'):
    key, value = i.split(':')
    dic1[key] = int(value)
    # dic1.setdefault(i.split(':')[0], int(i.split(':')[1]))
print(dic1)

# 将大于66的值保存至字典的第一个key对应的列表中，将小于66的值保存至第二个key对应的列表中
l1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
result = {'k1': [], 'k2': []}
for i in l1:
    if i > 66:
        result['k1'].append(i)
    elif i < 66:
        result['k2'].append(i)
print(result)

# 输出商品列表，用户输入序号，显示用户选中的商品
goods = [
    {"name": "电脑", "price": "1999"},
    {"name": "鼠标", "price": "10"},
    {"name": "游艇", "price": "20"},
    {"name": "美女", "price": "998"}
]
# 1. 页面显示 序号 + 商品名 + 价格  如
#                                   1 电脑 1999
#                                   2 鼠标 10   。。。。
# 2. 用户输入选择的商品序号，然后打印商品名称及商品价格
# 3. 如果用户输入的商品序号有误，则提示输入有误，并重新输入
# 4. 用户输入Q或者q，退出程序
# for i in range(len(goods)):
#     print(i + 1, goods[i]['name'], goods[i]['price'])
while True:
    for index, dic in enumerate(goods):
        print("{} \t {} \t {}".format(index + 1, dic["name"], dic["price"]))
    num_1 = input("请输入商品序号：")
    if num_1.isdecimal():
        num_1 = int(num_1)
        # if num_1 in range(1, 5):
        if 0 < num_1 <= len(goods):
            num_1 -= 1
            print("商品名称: {} 商品价格: {}".format(goods[num_1]['name'], goods[num_1]['price']))
        else:
            print("输入的序号超出界限")
    elif num_1.upper() == "Q":
        print("退出程序")
        break
    else:
        print("请输入非字母元素")

# 看代码写结果
v = {}
for index in range(10):
    v['users'] = index
print(v)  # {'users': 9}
