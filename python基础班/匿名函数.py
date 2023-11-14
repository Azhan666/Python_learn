#匿名函数:

def sum_1(a,b):
    print(a + b)
sum_1(5,6)

result = lambda a,b:a + b      # lambda是关键词，不能放句首

print(result(3,2))

dict_1 = [{'name':'6',2:'b',3:'c'},
          {'name':'4',2:'b',3:'c'},
          {'name':'5',2:'b',3:'c'}
        ]

dict_1.sort(key=lambda dict_1:
dict_1['name'])

print(dict_1)


