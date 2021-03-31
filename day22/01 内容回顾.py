# 递归练习
# 遍历文件夹下的所有文件  -- 掌握
# 斐波那契数列练习 -- 会写
# 三级菜单  -- 看懂并知道实现方法
# 查看文件夹的总大小 -- 看懂并知道实现方法
# sys
# sys.path
# sys.argv 在执行python脚本的时候 写在python 之后的所有的内容,形成了一个列表
# sys.modules 查看已经加载到内存中的所有模块
# os
# 和文件 文件夹相关的
# 和工作目录相关的
# 和执行操作系统命令相关的
# .path系列
# logging
# 排错 数据分析 操作审计
# 普通的输出(文件/屏幕)
# 切分日志(时间/文件大小)
# shutil
# 和文件相关的内容

# 算法
# 二分查找  [1,2,3,4,5,6,7,8,9,10,27,36,46,58,69] - 有序列表
# in index 从列表中找到一个值的位置
# 实现上面的功能 - 用代码

l1 = [2, 3, 5, 10, 15, 16, 18, 22, 26, 30, 32, 35, 41, 42, 43, 55, 56, 66, 67, 69, 72, 76, 82, 83, 88]


def func(lis, number):
    mid_number = (len(lis) - 1) // 2
    if number > lis[mid_number]:
        new_lis = lis[mid_number + 1:]
        func(new_lis, number)
    elif number < lis[mid_number]:
        new_lis = lis[:mid_number]
        func(new_lis, number)
    else:
        print(mid_number)


func(l1, 22)

# sys.argv练习
# 写一个python脚本,在cmd里执行
# python xxx.py 用户名 密码 cp 文件路径 目的地址
# python xxx.py alex sb cp D:\python_22\day22\1.内容回顾.py D:\python_22\day21
# python xxx.py alex sb rm D:\python_22\day22
# python xxx.py alex sb rename D:\python_22\day22  D:\python_22\day23

# 使用walk来计算文件夹的总大小
# import os
# g = os.walk('D:\python_22')
# for i in g :
#     path,dir_lst,name_lst = i
#     print(path,name_lst)



l1 = [1, 2, 4, 5, 7, 9]
def two_search(l,aim,start=0,end=None):
    end = len(l)-1 if end is None else end
    mid_index = (end - start) // 2 + start
    if end >= start:
        if aim > l[mid_index]:
            return two_search(l,aim,start=mid_index+1,end=end)

        elif aim < l[mid_index]:
            return two_search(l,aim,start=start,end=mid_index-1)

        elif aim == l[mid_index]:
            return mid_index
        else:
            return '没有此值'
    else:
        return '没有此值'
print(two_search(l1,2))
