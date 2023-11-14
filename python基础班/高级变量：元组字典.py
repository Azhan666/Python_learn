#字典遍历目录:
dict_1 = {1:'!',2:'@',3:'#',4:'$',5:'%',6:'^',7:'&',8:'*' }

a = dict_1.keys()
print(list(a))
a = int(input('请输入数字:'))
for k in dict_1.keys():
 if a == k:
     print(dict_1[a])
if a != k:
   print('数字不在列表里，请重新输入')