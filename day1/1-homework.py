# 炸金花发牌游戏（奖品）
# 生成一副扑克牌，去除大小王
# 5个玩家，每个人发三张牌
# 最后计算谁是赢家（进阶）
a = 1
number = []
poker = []
letter = ['J', 'Q', 'K', 'A']
design_color = ['H', 'M', 'F', 'X']
while a < 10:
    a = a + 1
    number.append(str(a))
num = number + letter
for i in design_color:
    for y in num:
        poker.append(i + y)
print(poker)
# print(len(poker))
player = ['小李', '小红', '小刚', '小智', '小夏']
# for x in player:
#     pai = range(poker, 3)
