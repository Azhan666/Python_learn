import time


class Weapon:
    print('\t\t\t欢迎来到和平精英如家vip专享版')

    def __init__(self, name, num, magazine):
        self.name = name
        self.num = num
        self.magazine = magazine

    def __str__(self):
        return '武器简介:%s\t子弹数量：%d\t弹夹：%d' % (self.name, self.num, self.magazine), '补充弹夹%s' % self.magazine


Weapon.magazine = 'VIP特制弹夹'
magazines = Weapon.magazine
rifle = Weapon('如家特制黄金步枪vip版', 999999, 9999999)  # vip专属武器
uzi = Weapon('如家精选冲锋枪第一代vip版', 999999, 999999)  # vip专属武器
pistol = Weapon('如家炫彩小手枪vip版', 999999, 999999)  # vip专属武器
pistol_1 = Weapon('不知道哪来的破烂小手枪平民版', 6, 0)


class Game:
    character = {1: '如家炫彩突击兵', 2: '平民', 3: '如家精英工程兵', 4: '充值10000获得如家VIP', 5: '如家VIP'}  # 设定游戏角色

    def __init__(self, name):
        self.name = name
        self.weapon_list = []

    def __str__(self):
        return '\n玩家名称：%s' % self.name

    def weapon(self, weapon):
        print('\n系统为您自动解锁了%s\t子弹数:%d\t弹匣：%d' % (weapon.name, weapon.num, weapon.magazine))
        while 3 <= weapon.num <= 6:
            time.sleep(1)
            print('子弹剩余', weapon.num)
            time.sleep(2)
            print('\n破烂小手枪：存有子弹，可以开火')
            print('\n', '·'*5, '限速模式随机运行中', '·'*5,)
            time.sleep(2)
            print('\n\t\t\t每次开火消耗三颗子弹')
            print('\t\t\t哒哒哒~~~~~~~兄弟们充钱啊~~')
            weapon.num -= 3
        while weapon.num == 0:
            time.sleep(2)
            print('\n子弹耗尽，无法开火')
            time.sleep(1)
            print('\n\t\t\t系统随机赠送弹匣')
            weapon.num = 6
            weapon.magazine = 0
            print('\n', '·' * 5, '限速模式随机运行中', '·' * 5 )
            time.sleep(2)
            break
        if weapon.num == 999999:
            time.sleep(1)
            print('\n\tVIP玩家子弹无限', '当前武器：', weapon.name)
            time.sleep(1)
            print('正在装备VIP皮肤', Game.character[1])
            time.sleep(1)
            print(Game.character[1], '装备成功')
            time.sleep(1)
            print('哒哒哒'*20, '兄弟们冲啊~~~~~')
            time.sleep(1)


play = Game(input('请输入想要创建的名字：'))  # 进入游戏
nums = Game.character.keys()
print(Game.character, '\n')
count = 5
while count:
    role = int(input('选择你想要的角色编号,系统提示，目前1.0版本，1，3，5需要选择充值VIP才能获取，系统建议您选择4,选2也不阻拦你\t请谨慎选择：'))
    if role in nums and role == 2:
        print('由于您选择角色平民，限速模式随机启动')
        time.sleep(4)
        print('\n玩家：', Game.character[role])
        print(play, '角色：' + Game.character[role])
        print('\n', '·'*5, '限速模式随机运行中', '·'*5)
        time.sleep(3)
        print('\n平民玩家本来无法获得武器，系统看你可怜，送你一把')
        print('\n', '·'*5, '限速模式随机运行中', '·'*5)
        time.sleep(3)
        play.weapon(pistol_1)
        time.sleep(2)
        print('\n获得系统随机赠送的弹匣，自动更换成功')
        play.weapon(pistol_1)
        time.sleep(3)
        print('由于角色为平民，只能获得系统随机赠送机会1次\n')
        time.sleep(2)
        print('\t\t\t\t\t恭喜玩家被VIP玩家击杀')
        time.sleep(2)
        print('\n', '='*30, '游戏自动结束' + '='*30)
        break

    elif role == 4:
        time.sleep(1)
        print("充值成功！")
        print('尊敬的如家大佬，欢迎您的到来，自动为您解锁vip人物\n')
        print('恭喜获得：', Game.character[5])
        print('成功解锁皮肤', Game.character[1], '  ', Game.character[3], '游戏中可自由切换', '\n')
        time.sleep(1)
        print(play, '角色：' + Game.character[5])
        print('大佬请稍等,正在加载VIP专属道具，大佬请稍等...\n')
        time.sleep(1)
        print('加载完成\n')
        time.sleep(1)
        player = Game(play)
        time.sleep(1)
        player.weapon(uzi)
        time.sleep(1)
        print('自动切换武器中')
        time.sleep(1)
        player.weapon(rifle)
        print('自动切换武器中')
        time.sleep(1)
        player.weapon(pistol)
        print('平民玩家已被全部击杀，\n恭喜VIP玩家获胜~')
        time.sleep(2)
        print('\n', '=' * 30, '游戏自动结束' + '=' * 30)
        break
    else:
        count -= 1
        print('不遵守规则，剩余', count, '次机会！')
