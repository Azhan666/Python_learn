       # 私有属性和私有方法:


# 在实际的Python开发中，对象的一些属性和方法只希望在对象的内部被使用，而不希望被外部访问

# 私有属性：对象不希望公开的属性

# 私有方法：对象不希望公开的方法

# 定义私有属性、方法的方式：
# 在定义属性或方法时，在属性名或者方法名前面增加两个下划线，定义的属性或方法就是私有属性或方法


# class Handsome:    #定义一个对象"帅哥"   #如家帅哥
#     def __init__(self,age):
#
#         self.age = age     # 若为self.__age则为私有属性
#         print(self.age)    # 非私有属性，可正常输出
#
# rujia = Handsome(19)      #用私有对象、类、方法、名可以调用私有属性和方法 #可以如家了
#
# rujia.age
#
#
# # 继承（单继承、多继承）：
#
# class Animal(object):      # Python开发中默认object，但规定输入object
#     def __init__(self):
#         self.name = '二哈'  #二哈不会如家，好可怜
#
#
# class Dog(Animal):
#     pass              #继承父类"Animal",无需输入属性    #继承也不会如家
#
# class MinDog(Dog):       #定义子类继承父类属性
#     pass              #继承了"Dog"父类属性       #小二哈，不如家
#
#
# erha = Dog()        #赋值父类
# MinDog = MinDog()   #赋值子类
#
# print(MinDog.name)  #子类继承父类属性，输出"二哈"



# 多继承：

# class Q:                 #父类 1    #阿Q会如家
#     def printq(self):
#         print('__Q__')
#
#
# class W:
#     def printw(self):    #父类 2（父类2为父类1的子类）     #阿Q的儿子长大也会如家
#         print('__W__')
#
#
# class E(Q,W):             #子类1（继承了Q类和W类）
#     pass                 #E将会继承q和w的属性：     #阿Q和阿王都会如家
#
# e = E()
# e.printq()               #继承结果           # 两个一起去如家
# e.printw()

#mro:可以查看多继承时对象搜索方法的顺序,在print对象命令后输入(对象.__mro__)即可：

#print(E.__mro__)         #查看了对象E搜索方法的顺序，搜索顺序：自己、父类1、父类2，若都没有则搜索基类（object）
                         # 若object中也没有方法则会报错


#重写父类方法：在子类中，有一个和父类相同名字的方法，父类中同名字的方法会被子类方法覆盖
#super：拓展父类的方法并且保留原有的方法
#为什么要重写？：当父类的方法不能满足子类需要时，可以重写父类方法，   （子父类方法的类名需一模一样）
#要想重写父类方法的同时又可以使用原来的父类方法，则需要用到 super
class Q:

    def __init__(self):

        self.name = 'rujia'    #增加一个如家的方法来验证下面super的功能

    def printq(self):
         print('__Q__')


class W:
     def printw(self):
         print('__W__')


class E(W):
     def printw(self):
         super().printw()         #用super来拓展父类方法，增加了新功能并且保留了原有的父类方法
         print('__E__')                #保留了如家的功能，如家的功能又增加了


e = E()
e.printw()



print(E.__mro__)

#由底层代码可知，super也是一个特殊的类














