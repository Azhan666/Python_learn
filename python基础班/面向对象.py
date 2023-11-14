# 类和对象的定义和使用:

# 在程序设计中，要设计一个类，要满足以下两个要素:
# 1. 类名  需要满足大驼峰命名规则（首字母大写）
# 2. 属性  事物具有什么特征
# 3. 方法  事物具有什么行为

# 在Python里面用 class 来定义类

class Person:
    """人类"""

    def eat(self,name):
      print('%s在敲代码'% name)

    def drink(self,name):
      print('%s在写作业'% name)

hezhan = Person()
hezhan.drink('何展')  #对象名.方法名 叫做调用方法

hezhan.eat('何展')
print('\n')
litao = Person()

litao.drink('李涛')

litao.eat('李涛')

a = 1

#在Python中，对象是无处不在的，我们之前学的变量、函数、数据、都是对象，在Python中一切皆对象

print(litao)
print('%x'% id(litao))

#_new_方法 创建对象时会被自动调用

#_init_方法 对象被初始化时，会被自动调用

#_del_方法 对象在内存中被销毁前，会被自动调用

#_str_方法 放回对象的描述信息，print函数输出返回信息

class Person:
    """人类"""
    def _init_(self,name):
      self.name = name  #self.属性名 = 属性的初始值（形参） self就是给对象增加属性的

      def write(self):
        print('%s在敲代码'% self.name)
      def write(self):
        print('%s在写代码'% self.name)
litao = Person('李涛')  #实例化对象
litao.write()
litao.drink()
hezhan = Person('何展')
hezhan.drink()  #对象名.方法名，叫做调用方法
hezhan.write()

#由哪一个对象调用的方法，方法内的self就是那一个对象的引用

#在类里面，self就表示当前调用方法的对象自己



