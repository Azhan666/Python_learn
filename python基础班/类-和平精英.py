print("欢迎来到和平精英,让子弹飞一会儿")
print("游戏加载成功,开始游戏吧!")
#定义玩家:
class Player:
    """玩家类"""
def __init__(self,name,hp=100):
    """初始化玩家属性"""

    self.name = name   #昵称
    self.hp =hp   #生命值
    self.gun =None   #枪支
def __str__(self):
  if not self.gun:
    return '%s 剩余血量 %d,目前没有枪支，无法开枪'% (self.name,self.hp)

#定义抢类:

class Gun:
    """枪类"""

def __init__(self,model,damage):
    """初始化枪的属性"""
    self.model = model #枪的型号
    self.damage = damage  #枪的杀伤力
    self.bullet_count = 0  #子弹数量

def __str__(self):
    """返回枪的描述信息"""
    return '%s 杀伤力是 %d,剩余子弹为 %d 颗' %(self.mode,self.damage,self.bullet_count)
def add_bullet(self,count):
    """添加子弹"""
    self.bullet_count +=count

def shoot(self,enemy):
        """射击敌人，造成伤害"""
        #没有子弹，不能射击
        if self.bullet_count <= 0:
            print('没有子弹了!无法射击')
            return
        #射击，造成伤害
        self.bullet_count -=1
        if enemy:
            print('%s射击 %s,造成 %d伤害'%(self.model,enemy,self.damage))
            enemy.hurt(self.damage)
        else:
            print('没有敌人，打了空枪!')


def test():
    """游戏测试"""
    #创建枪
    ak47 = Gun('ak47',99)
    print(ak47)

    #添加子弹
    ak47.add_bullet(20)
    print(ak47)

    #射击敌人
    ak47.shoot(None)
    print(ak47)
    ak47.shoot('守卫者')
    print(ak47)
    ak47.shoot('守卫者')
    print(ak47)

    print('******枪类测试结束******')

    #玩家测试

    police = Player('警察',150)
    print(police)
    badman = Player('悍匪')
    print(badman)

    #玩家捡枪

    police.take_Gun(ak47)
    print(police)

    #玩家射击

    police.fire(badman)
    print(badman)
    police.fire(badman)
    print(badman)
    police.fire(badman)
    print(badman)

def main():
    """游戏主流程"""
    #创建两个玩家
    police = Player('警察')
    badman = Player('悍匪')
    print(police)
    print(badman)

    #创建枪
    k98 = Gun('98k',20)
    k98.add_bullet(2)

    #玩家拿枪
    badman.take_Gun(k98)
    print(police)

    #开枪射击
    badman.fire(police)
    badman.fire(police)
    print(police)
    badman.fire(police)










