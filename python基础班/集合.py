# 引用:
a = 1
b = 1
print('a,b')
# 集合(set):
# For example:
a = {}
b = set()
list_1 = ['a','b']
dict_1 = {'x','y'}
# 添加（add): # 不能添加字典和列表
# len查看集合元素个数：
print(len(a))
print(len(b))
# 列表,字典,集合,推导式：
# 列表推导式:
a = []
for i in range(1,10):
  if i %2 == 0:
   a.append(i)
print(a)
list_1 = [i for i in range(1,10) if i %2 is 0]
print(list_1)
# 字典推导式:
b = input(':')
dict_1 = {'a':10,'b':20,'A':7,'Z':3}
a = {v:k for k,v in dict_1.items()}
print(a)
#集合推导式:
set_1 = {i**2 for i in [1,1,2]}
print(set_1)
# 三目运算(if,else语法）:
print('返回True时执行') if 3 < 4 else '返回False时执行'
b = 3+2,"3>2",print('victory') if 1>2 else print("never say never"),2+2
print(b)










