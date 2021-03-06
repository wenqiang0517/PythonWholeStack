# 代码块
# 	* 代码块：我们的所有代码都需要依赖代码块执行，Python程序是由代码块构造的。块是一个python程序的文本，他是作为一个单元执行的。
# 	* 一个模块，一个函数，一个类，一个文件等都是一个代码块
# 	* 交互式命令下一行就是一个代码块

# 两个机制同一个代码块下，有一个机制，不同的代码块下，遵循另一个机制
# 同一代码块下的缓存机制
# 	* 前提条件：同一代码块内
# 	* 机制内容：pass
# 	* 适用的对象：int bool str
# 	* 具体细则：所有的数字，bool，几乎所有的字符串
# 	* 优点：提升性能，节省内存

# 不同代码块下的缓存机制: 小数据池
# 	* 前提条件：不同代码块内
# 	* 机制内容：pass
# 	* 适用的对象：int bool str
# 	* 具体细则：-5-256数字，bool，满足规则的字符串
# 	* 优点：提升性能，节省内存

"""
总结：
1，面试题考
2，一定要分清楚：同一代码块下适应一个就缓存机制，不同的代码块下适用另一个缓存机制(小数据池)
3，小数据池：数字的范围是 -5-256
4，缓存机制的有点：提升性能，节省内存
"""

