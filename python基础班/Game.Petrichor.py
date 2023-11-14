#石头剪刀布游戏:#一局定输赢

print("石头剪刀布游戏")
import random# 调用了random（随机）模块，来实现电脑的随机出拳

player = int(input("请输入您的选择：|n剪刀 (0) 石头 (1) 布 (2): "))# 用 0、1、2、分别代表剪刀、石头、布

computer = random.randint(0,2)# randint（随机）

print(computer)

if (player == 0 and computer == 1)or(player == 1 and computer == 2)or(player == 2 and computer == 0):# 定义游戏规则

    print("很遗憾,你输了")
elif player == computer:
    print("很幸运,打了个平局")
else:
    print("恭喜你赢了")








