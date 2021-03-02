import sys

sys.setrecursionlimit(100000000)
count = 0


def func():
    global count
    count += 1
    print(count)
    func()
    print(456)


func()
