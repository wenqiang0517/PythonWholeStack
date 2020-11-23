# 1，看代码写结果，并解释每一步流程
v1 = [1, 2, 3, 4, 5]
v2 = [v1, v1, v1]
v1.append(6)
print(v1)  # [1,2,3,4,5,6]
print(v2)  # [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]

# 2，看代码写结果，并解释每一步流程
v1 = [1, 2, 3, 4, 5]
v2 = [v1, v1, v1]
v2[1][0] = 111
v2[2][0] = 222
print(v1)  # [222, 2, 3, 4, 5]
print(v2)  # [[222, 2, 3, 4, 5],[222, 2, 3, 4, 5],[222, 2, 3, 4, 5]]

# 3，看代码写结果，并解释每一步流程   **********
v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v2 = {}
for item in v1:
    if item < 6:
        continue
    if 'k1' in v2:
        v2['k1'].append(item)
    else:
        v2['k1'] = [item]
print(v2)   # {'k1': [6,7,8,9]}

# 4，简述深浅copy

# 5，看代码写结果，并解释每一步流程   *************
import copy

v1 = 'alex'
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
print(id(v1), id(v2), id(v3))
print(v1 is v2)  # True
print(v1 is v3)  # True

# 6，看代码写结果，并解释每一步流程
import copy

v1 = [1, 2, 3, 4, 5]
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
print(v1 is v2)  # False
print(v1 is v3)  # False

# 7，看代码写结果，并解释每一步流程
import copy

v1 = [1, 2, 3, 4, 5]
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
print(v1[0] is v2[0])  # True
print(v1[0] is v3[0])  # True
print(v2[0] is v3[0])  # True

# 8，看代码写结果，并解释每一步流程
import copy

v1 = [1, 2, 3, 4, [11, 22]]
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
print(v1[-1] is v2[-1])  # True
print(v1[-1] is v3[-1])  # False
print(v2[-1] is v3[-1])  # False

# 9,看代码写结果，并解释每一步流程
import copy

v1 = [1, 2, 3, {'name': '太白', 'numbers': [7, 77, 88]}, 4, 5]
v2 = copy.copy(v1)
print(v1 is v2)  # False
print(v1[0] is v2[0])  # True
print(v1[3] is v2[3])  # True
print(v1[3]['name'] is v2[3]['name'])  # True
print(v1[3]['numbers'] is v2[3]['numbers'])  # True
print(v1[3]['numbers'][1] is v2[3]['numbers'][1])  # True

# 10,看代码写结果，并解释每一步流程
import copy

v1 = [1, 2, 3, {'name': '太白', 'numbers': [7, 77, 88]}, 4, 5]
v2 = copy.deepcopy(v1)
print(v1 is v2)  # False
print(v1[0] is v2[0])  # True
print(v1[3] is v2[3])  # False
print(v1[3]['name'] is v2[3]['name'])  # True    ***************
print(v1[3]['numbers'] is v2[3]['numbers'])  # False
print(v1[3]['numbers'][1] is v2[3]['numbers'][1])  # True       ******************

# 11, a b c 三个变量的类型
a = ('太白金星')  # str
b = (1,)  # tuple
c = ({'name': 'barry'})  # dict
print(type(a), type(b), type(c))

# 12, 列表排序
l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]
# 从大到小排序
# l1.sort(reverse=True)
# print(l1)
# 从小到大排序
# l1.sort()
# print(l1)
# 反转列表l1
# l1.reverse()
# print(l1)

# 13，构建一个列表
# [['_','_','_'],['_','_','_'],['_','_','_']]

# 14,看代码写结果，并解释每一步流程
l1 = [1, 2, ]
l1 += [3, 4]
print(l1)  # [1,2,3,4]

# 15,看代码写结果，并解释每一步流程
dic = dict.fromkeys('abc', [])
dic['a'].append(666)
dic['b'].append(111)
print(dic)  # {'a': [666,111],'b': [666,111],'c': [666,111]}

# 16, 把索引为奇数对应的元素删除（不能一个个删，里面元素不定)  已做过
# l1 = [11, 22, 33, 44, 55]

# 17，将字典中所有键带k元素的键值对删除   做过
# dic = {'k1': '太白', 'k2': 'barry', 'k3': '白白', 'age': 18}


# 18，bytes数据类型事python的基础数据类型，bytes类型存在的意义是什么
# 网络的数据传输，数据存储

# 19，列举 bytes 类型和 str 类型的三个不同点
# 内存中的编码方式不一样
# 中文的表现形式不一样

# 20，完成以下需求
s1 = '太白金星'
# 将s1转换成 utf-8 的bytes类型
b1 = s1.encode('utf-8')
print(b1, type(b1))

# 将s1转换成 gbk 的bytes类型
b2 = s1.encode('gbk')
print(b2, type(b2))

# b为 utf-8 的bytes类型，转换成 gbk 的bytes类型
b = b'\xe5\xa4\xaa\xe7\x99\xbd\xe6\x9c\x80\xe5\xb8\x85'
b3 = b.decode('utf-8').encode('gbk')
print(b3, type(b3))

# 21，用户输入一个数字，判断一个数是否为水仙花数
# 水仙花数是一个三位数，三位数的每一位的三次方的和还等于这个数，那这个数就是水仙花数
# 153 = 1**3 + 5**3 + 3**3
content = input('请输入：').strip()
l1 = []
if content.isdecimal():
    if 99 < int(content) < 1000:
        l1.extend(str(content))
        # sum_1 = (int(l1[0])**3) + (int(l1[1])**3) + (int(l1[2])**3)
        if int(content) == ((int(l1[0]) ** 3) + (int(l1[1]) ** 3) + (int(l1[2]) ** 3)):
            print('水仙花数')
        else:
            print('不是水仙花数')
    else:
        print('输入不在范围')
else:
    print('输入错误')

# 22，把列表中所有姓周的人的信息删掉
lst = ['周老二', '周星星', '麻花藤', '周扒皮']
# 结果 lst = ['麻花藤']
l1 = []
for i in lst:
    if '周' in i:
        l1.append(i)
for i in l1:
    lst.remove(i)
print(lst)

# 23, 车牌区域划分，先给出以下车牌，根据车牌的信息，分析出各省的车牌持有量
cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C49678', '黑C46555', '沪B25041']
locals = {'沪': '上海', '黑': '黑龙江', '鲁': '山东', '鄂': '湖北', '湘': '湖南', '京': '北京'}
# 结果：{'黑龙江':2,'山东':1,'北京':1}
dic1 = {}
for i in cars:
    i = i[0]
    if i in locals.keys():
        if locals[i] in dic1.keys():
            dic1[locals[i]] += 1
        else:
            dic1[locals[i]] = 1
print(dic1)


