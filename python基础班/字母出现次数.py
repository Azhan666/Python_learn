#给定的字符串
s = " Nowadayspetsbecome so close and friendly to our humanbeings that more and m\
 ore people enjoy keeping themPets can\
 bring them a lot of joys and happiness  because play\
 ing with pets is a good way to communicate with the natureBesidespets can\
 comfort old people who live alonebecause playing with pets is a good way t\
 o communicate with the natureBesidespets can comfort old people who live alone\
 because playing with pets is a good way to communicate with the na\
 tureBesidespets can comfort old people who live alone because playing w\
 ith pets is a good way to communicate with the natureBesidespets c\
 an comfort old people who live alone\
 becasue playing with pets is a good way to communicate with the natur\
 eBesidespets can comfort old people who live alone\
 With the companion of petsthey wont feel lonely Nevertheles\
 sIm not interested in keeping pets at allFor one thingkeepin\
 g pets is bad for environmental protection\
 since pets usually make a lot of noise and contaminate the\
 roads For anotherthe virus carried by pets may cause fatal disease Whats\
 more sometimes pets may attack people when they are unhappy\
 Consequently we had better not keep too many petsso as to ensure our health\
 and security\
 Besides those pet lovers must take some effective measure\
 s to prevent their pets from hurting people and pollutingourenvironment"

#新建一个字典
d={}
#遍历s
for c in s:
    # 检查字典d中是否含有键为c的项
    if ( c in d):
        # 如果有 则键对应的值+1
        d[c]=(d[c]+1)
    else:
        #否则键对应的值为1
        d[c]=1
print (d)