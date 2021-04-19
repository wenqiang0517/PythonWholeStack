# 内置的数据结构
    # {}  key-value 通过key找v非常快
    # []  序列 通过index取值非常快
    # ()  元组
    # {1,}集合
    # 'sx'字符串
# 不是python内置的
    # Queue队列 : 先进先出 FIFO(FIRST IN FIRST OUT)
        # put
        # get
    # Stack栈   : 后进先出 LIFO(Last In First Out)
        # put
        # get
    # 继承关系
    # 完成代码的简化

"""
class Queue:
    def __init__(self):
        self.lis = []

    def put(self, number):
        self.lis.append(number)

    def get(self):
        result = self.lis.pop(0)
        print(result)


queue = Queue()
queue.put(1)
queue.put(3)
queue.put(4)
queue.put(2)
queue.get()
queue.get()
queue.put(5)
queue.put(9)
queue.get()
queue.get()
"""

"""
class Stack:
    def __init__(self):
        self.lis = []

    def put(self, number):
        self.lis.append(number)

    def get(self):
        result = self.lis.pop()
        print(result)


stack = Stack()
stack.put(1)
stack.put(3)
stack.put(5)
stack.put(7)
stack.get()
stack.get()
stack.put(33)
stack.put(10)
stack.get()
stack.get()
"""


# class Queue:
#     def __init__(self):
#         self.lis = []
#
#     def put(self, number):
#         self.lis.append(number)
#
#     def get(self):
#         result = self.lis.pop(0)
#         print(result)
#
#
# class Stack(Queue):
#     def get(self):
#         result = self.lis.pop()
#         print(result)


# 方法一
# class Foo:
#     def __init__(self):
#         self.l = []
#
#     def put(self, item):
#         self.l.append(item)
#
#
# class Queue(Foo):
#     def get(self):
#         return self.l.pop(0)
#
#
# class Stack(Foo):
#     def get(self):
#         return self.l.pop()

# 方法二:
# class Foo:
#     def __init__(self):
#         self.l = []
#
#     def put(self,item):
#         self.l.append(item)
#
#     def get(self):
#         return self.l.pop() if self.index else self.l.pop(0)
#
# class Queue(Foo):
#     def __init__(self):
#         self.index = 0
#         Foo.__init__(self)
#
# class Stack(Foo):
#     def __init__(self):
#         self.index = 1
#         Foo.__init__(self)

# 方法三
class Foo:
    def __init__(self):
        self.l = []

    def put(self, item):
        self.l.append(item)

    def get(self):
        return self.l.pop()


class Queue(Foo):
    def get(self):
        return self.l.pop(0)


class Stack(Foo): pass


q = Queue()
s = Stack()
q.put(1)
q.put(3)
q.put(9)
q.get()
q.get()
q.put(10)
q.get()

s.put(2)
s.put(4)
s.put(5)
s.get()
s.get()
s.put(13)
s.put(23)
s.get()

# 自定义Pickle,借助pickle模块来完成简化的dump和load
# pickle dump
# 打开文件
# 把数据dump到文件里
# pickle load
# 打开文件
# 读数据

# 对象 = Mypickle('文件路径')
# 对象.load()  能拿到这个文件中所有的对象
# 对象.dump(要写入文件的对象)
import pickle


class Mypickle:
    def __init__(self, file_path):
        self.file_path = file_path

    def dump(self, obj):
        with open(self.file_path, 'ab') as f:
            pickle.dump(obj, f)

    def load(self):
        with open(self.file_path, 'rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def get(self):
        pass


python = Course('python', '6 moneth', 21800)
linux = Course('linux', '5 moneth', 19800)
go = Course('go', '4 moneth', 12800)

mypickle = Mypickle('pickle.txt')
# mypickle.dump(python)
# mypickle.dump(linux)
# mypickle.dump(go)
for i in mypickle.load():
    print(i.name)
    print(i.period)


