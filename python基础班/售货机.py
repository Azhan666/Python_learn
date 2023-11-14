toubi = 0  # 用来接收投币的总金额
while True:
    money = input("请投入现金，现金必须是5,10,20,100 按e退出投币：")
    if money == '5' or money == '10' or money == '20' or money == '100':
        toubi += int(money)
        print("您投入了{0}元".format(toubi))
        print("投币完成，您一共投入了{0}元，请选择商品".format(toubi))

    elif money == 'e':
        break
    else:
        print("请投入面值为5,10,20,100的纸币或硬币，其余面值不接受，请重新投币")

while True:
    choose = input("请选择您要购买的商品：1：气球 2：面膜 3：蕾丝 4：如家svip套装 5: 如家vip套装 6: 如家至尊丝滑套装 e:退出")
    Commodity = {"1": 4.5, "2": 9, "3": 15, "4": 90,"5": 80,"6": 50}

    if choose in Commodity.keys():
        if toubi > Commodity[choose]:
            print("您刚刚购买了{0}元的商品，您已支付{1}元，找零{2}元！".format(Commodity[choose], toubi, toubi - Commodity[choose]))
            break
        elif toubi < Commodity[choose]:
            print("您刚刚购买了{0}元的商品，您已支付{1}元，还需{2}元！".format(Commodity[choose], toubi, Commodity[choose] - toubi))
        else:
            print("您刚刚购买了{0}元的商品，您已支付{1}元，支付完毕！".format(Commodity[choose], toubi))
            break
    elif choose == 'e':
        print("退出选择,返还余额")
        break
    else:
        continue