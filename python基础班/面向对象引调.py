# 定义类:

class Person:

    def __init__(self,name,weight):
      self. name = name
      self. weight = weight

    # def run(self):
    #   print('%s跑步之前，体重%.2f公斤' %(self.name,self.weight))
    #   self.weight -= 2
    #   print('%s跑了两百公里后，体重%.2f公斤' %(self.name,self.weight))


    def eat(self):
      print('%s跑完步后，体重%.2f公斤'%(self.name,self.weight))
      self.weight += 20
      print('%s吃了一顿夜宵，体重%.2f公斤'%(self.name,self.weight))
nunu = Person('努努',60)
nunu.eat()






