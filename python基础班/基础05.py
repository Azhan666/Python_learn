# #定义变量A，默认有3个元素
#     A = ['xiaoWang','xiaoZhang','xiaoHua']
#
#     print("-----添加之前，列表A的数据-----")
#     for tempName in A:
#         print(tempName)
#
#     #提示、并添加元素
#     temp = input('请输入要添加的学生姓名:')
#     A.append(temp)
#
#     print("-----添加之后，列表A的数据-----")
#     for tempName in A:
#         print(tempName)


#字典，列表等相关操作不熟练:    info: 信息， 资料.

# 1 字典：
# <1>修改元素:
# 字典的每个元素中的数据是可以修改的，只要通过key找到，即可修改
# demo:
# info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}
#
# newId = input('请输入新的学号')
#
# info['id'] = int(newId)
#
# print('修改之后的id为%d:'%info['id'])

## <2>添加元素:     sddress: 地址符

#demo:访问不存在的元素

# info = {'name':'班长', 'sex':'f', 'address':'地球亚洲中国北京'}
#
# print('id为:%d'%info['id'])

#因为结果不存在，所以输出结果报错


#如果在使用 **变量名['键'] = 数据** 时，这个“键”在字典中，不存在，那么就会新增这个元素

#demo:添加新的元素

# info = {'name':'班长', 'sex':'f', 'address':'地球亚洲中国北京'}
#
# #print('id为:%d'%info['id'])#程序会终端运行，因为访问了不存在的键
#
# newId = input('请输入新的学号')
#
# info['id'] = newId
#
# print('添加之后的id为:%d'%info['id'])


## <3>删除元素

#对字典进行删除操作，有一下几种：







# info = {'name':'班长', 'sex':'f', 'address':'地球亚洲中国北京'}
#
# print('删除前,%s'%info ['name'])
# info['name']
# 
# print('删除后,%s'%info ['name'])
#

#demo:clear清空整个字典


# info = {'name':'monitor', 'sex':'f', 'address':'China'}
#
# print('清空前,%s'%info)
#
# info.clear()
#
# print('清空后,%s'%info)

# 字典的相关操作 2 ：
### <1>len()

#测量字典中，键值对的个数：

# dict = {"name":'hezhan','sex':'m'}
# len(dict)
#
#
# ### <2> keys
#
# # 返回一个包含字典所有key的列表
# dict = {"name":'hezhan','sex':'m'}
# dict.keys()
# ['name','sex']
#
# ### <3>values
#
# #返回一个包含字典所有values的列表
# dict = {"name":'hezhan','sex':'m'}
# dict.values()
# ['hezhan','m']
#
# ### <4> items
#
# # 返回一个包含所有（键，值）元组的列表
#
# dict = {"name":'hezhan','sex':'m'}
# dict.items()
# [('name','hezhan'),('sex','m')]
#
# ###<5> has_key
#
# # dict.has_key(key)如果key在字典中，返回true，否则返回false
# dict = {"name":'hezhan','sex':'m'}
# True
# dict.has_key('phone')
# False

# 字典的遍历：
# 通过for...in...的语法结构，我们可以遍历字符串、列表、元组、字典等数据结构

# **注意Python语法的缩进**
## 字符串遍历
# a_atr = "hello itcast"
# for char in a_atr:
#  print (char)
#
#
#
# ## 遍历字典
# a_list = [1,2,3,4,5]
# for num in a_list:
#  print (num)

## 元祖遍历

# a_turple = (1,2,3,4,5)
# for num in a_turple:
#     print (num)










