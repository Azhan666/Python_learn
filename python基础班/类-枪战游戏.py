print("欢迎来到和平精英,让子弹飞一会儿")
print("游戏加载成功,开始游戏吧!")

import random   # 定义随机加载游戏

class Player:   #定义玩家
    def __init__(self, name):
        self.name = name   #昵称
        self.hp = 100      #血量
        self.gun = None    #枪支

    def __str__(self):

        return "%s当前生命值为%d" % (self.name, self.hp) # 返回玩家状态调用return 显示当前玩家状态值



class Hero(Player):
    def fire(self, p):

        hit = random.randint(1,100)     # 定义hit为命中率 产生随机数
        if hit > 20:                        # 命中率为80
            if p.hp == 0:
                print("%s都死了不要打了" % p.name)     # 判断对象的血量如果等于0时输出在鞭尸
            else:
                damage = random.randint(40, 60)    # 判断打中后 产生的随机伤害值
                print("%s掏出手枪,beng!向%s开了一枪，掉了%d血" % (self.name, p.name, damage))
                if p.hp < damage:   # 判断血量小于伤害值时  血量赋值为0
                    p.hp = 0
                else:
                    p.hp -= damage    # 伤害值 - 血量值 = 当前血量值
        else:
            print("没打中%s" % self.name)



    def __str__(self):
        state = ""             # 定义一个字符串state
        if self.hp == 100:
            state = "无伤"

        elif self.hp > 70 and self.hp < 100:

            state = "轻伤"


        elif self.hp > 1 and self.hp < 70:
            state = "重伤"

        elif self.hp <= 0:
            state = "挂了"
        return "%s的当前状态为%s" % (self.name, state)


class Bad(Player):
    def fire(self, p):
        damage = random.randint(1,10)
        hit = random.randint(1,100)
        if hit > 90:
            print("%s拿出黄金双鹰,哒哒哒...向%s开了几枪，掉了%d血" % (self.name, p.name, damage))
            if p.hp < damage:
                p.hp = 0
            else:

                p.hp -= damage
        else:
            print("%s没打中大兵" % self.name)


def main():
    h = Hero("守卫者")
    bad1 = Bad("幻影")
    bad2 = Bad("突击兵")
    bad3 = Bad("大兵")
    while True:
        x = random.randint(1, 3)      # 定义随机数，等于1 时向bad1开枪.....
        if x == 1:
            h.fire(bad1)
        elif x == 2:
            h.fire(bad2)
        elif x == 3:
            h.fire(bad3)
        bad1.fire(h)
        bad2.fire(h)
        bad3.fire(h)
        print(h)
        print(bad1)
        print(bad2)
        print(bad3)
        print()
        if h.hp <= 0:
            print("%s死亡，游戏结束" % h.name)
            break
        if bad1.hp <= 0 and bad2.hp <= 0 and bad3.hp <= 0:
            print("对方全部死亡")
            break
main()