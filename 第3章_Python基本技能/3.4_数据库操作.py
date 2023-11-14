# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""3.4 数据库操作"""

# 参考官方文档：https://docs.python.org/2/library/sqlite3.html
"""
    掌握数据库操作属于程序员的基本功,因为不管使用哪一种编程语言都需要和数据库打交道。大体上、数据库分
为两大流派:关系型数据库和非关系型数据库。常用的关系型数据库有MySOL和Oracles,常用的非关系型数据库有
MongoDB和Redis。所有的关系型数据库都支持SQL语法,因此,花上30分钟了解SQL语法是掌握数据库操作的必要前提。

    3.4.1使用SQLite数据库
SQLite是一款轻型的数据库,它的设计目标是嵌入式领域,目前已经应用在很多嵌入式产品中. SOLite占用的资源
非常低,在嵌入式设备中,可能只需要几百KB的内存。 sqlites是Python内置的标准模块,提供轻量型文本数据库的
全部功能。 SQLite是一个进程内的库,是一个实现了自给自足的、无服务器的、零配置的、事务性的SQL数据库引擎。
零配置的数据库意味着SQLite与其他数据库不一样,它不需要在系统中做任何配置。
"""

# sqlite3.connect()用于创建数据库连接，可以接受一个文件名作为参数，若该文件存在，则打开这个数据库文件，
# 若不存在，则自动创建文件。

# import sqlite3
# connection = sqlite3.connect(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\liting.db')
 # 返回一个游标
# connection:连接

# 1.连接数据库，创建一个数据库对象：
# db = sqlite3.connect(host='localhost',user='root',db='liting',
#                      password='521liting',port=3306,charset='utf8')
# 注意：
#
# 我们要操作的是liting这个数据库中的表，因此在连接的时候使db这个参数来指明要使用哪一个数据库；
# 由于mysql数据库就装在本机上，因此可以写localhost，当然你也可以写成主机名，或者主机ip；

# 2.开启游标功能，创建游标对象
# 这里使用的是数据库对象db中的cursor()方法，cursor:游标
# 关于游标：https://blog.csdn.net/pdcfighting/article/details/104085622/
# cursor = db.cursor() # 返回一个游标

# 3.使用execute()方法，执行SQL语句

# cursor.execute('select sname,ssex from student')
# 注意：当开启游标功能执行这个SQL语句后，系统并不会将结果直接打印到频幕上，而是将上述得到的结果，
# 找个地方存储起来，提供一个游标接口给我们，当你需要获取数据的时候，就可以从中拿数据。

# 4.使用fetchone()或fetchall()获取数据

# 一次性获取一条数据
# a = cursor.fetchone()
# 一次性获取所有数据
# a = cursor.fetchall()
# 注意：使用游标获取数据，需要用一个变量将结果存储起来，才能被我们拿来做二次使用，这里在下面的案例中
# 会体现出来。

# 5.断开数据库，释放资源
# db.close()

# sqlite3.connect()也可以用于创建内存数据库，该内存数据库仅运行在内存中而不保存为文件，进程结束后，
# 内存被释放，其代码如下：

# import sqlite3
# # connection = sqlite3.connect(':memory:') # memory:内存
# ":memory:"用来打开与驻留在RAM中而不是磁盘上的数据库的数据库连接
# # cursor = db.cursor()
# # print(sqlite3.apilevel)        # 数据库模块的 API 版本号
# # print(sqlite3.threadsafety)    # 数据库模块的线程安全等级
# # print(sqlite3.paramstyle)      # SQL 语句的参数风格（qmark 表示 SQL 语句原生风格）
#
# # 1、打开数据库连接
# conn = sqlite3.connect('test.db')
#
# # 2、打开游标
# c = conn.cursor()
#
# # 3、使用游标的 execute 方法执行 SQL 语句（DDL）
# c.execute('''
#     create table user_tb(
#         _id integer primary key autoincrement,
#         name text,
#         pass text,
#         age integer)
# ''')         # SQLite 可以忽略数据列的类型（即 name，pass，age）
#
# c.execute('''
#     create table order_tb(
#         _id integer primary key autoincrement,
#         item_name text,
#         item_price real,
#         item_number integer,
#         user_id integer,
#         foreign key(user_id) references user_tb(_id))
# ''')
#
# # 4、关闭游标
# c.close()
#
# # 5、关闭数据库连接
# conn.close()

# 通常，查询和返回数据是游标操作，提交和事务回滚是数据库连接操作，数据库连接和游标的方法有很多，
# 下面列出了最常用的几种方法：

# 1.cursor.execute(sql[,optional parameters]):执行一个SQL语句，该SQL语句可以被参数化，
# 即:使用占位符代替SQL文本
# 例如：cursor.execute("insert into water values(?,?)",('btq',28.55))

# 2.cursor.executemany(sql,seq_of_parameters):批量执行SQL语句
# 例如：cursor.executemany("insert into water values(?,?)",(('btq',28.55),('hhq',28.53)))

# 3.cursor.fetchone():获取查询结果集中的下一行，返回一个单一的序列，当没有更多的可用数据时，返回none

# 4.cursor.fetchmany([size=cursor.arraysize]):获取查询结果集中的下一组，返回一个列表，当没有更多
# 的可用行时，返回一个空列表，该方法尝试获取由size参数指定尽可能多的行。

# 5.cursor.fetchall():获取查询结果集中所有（剩余）的行，返回一个列表，当没有可用的行时，则返回
# 一个空列表。

# 6.cursor.close()：关闭游标

# 7.connection.commit():提交当前的事务，如果未调用该方法，那么自上一次调用commit()以来所做的任
# 何动作对其他数据库连接不可见。commit：提交

# 8.connection.rollback():回滚上一次调用commit()以来对数据库所做的更改。

# 9.connection.close():关闭数据库连接，请注意，关闭操作不会自动调用commit(),如果之前未调用commit(),
# 就直接关闭数据库，则所有更改将全部丢失！！

"""下面的代码是一个初始化以及读写SQLite数据库的实例："""

# import sqlite3
#
# class Sqlite3Client: # client:客户端
#     """读取SQLite数据库的客户端类"""
#     def __init__(self, db_file):
#         """构造函数"""
#         self._conn = sqlite3.connect(db_file)
#
#     def create_table(self, sql): # 创建表
#         """创建数据表"""
#         self.execute(sql)
#         self._conn.commit()
#
#     def execute(self, sql, args=()):
#         """运行SQL语句"""
#         cursor = self._conn.cursor()
#         if isinstance(args, list): # 批量执行SQL语句
#             cursor.executemany(sql, args)
#         else: # 单次执行SQL语句，此时parameter是tuple或None
#             cursor.execute(sql, args)
#         if sql.split()[0].upper() != 'SELECT': # 非select语句
#             self._conn.commit()
#         result = cursor.fetchall()
#         cursor.close()
#
#         return result
#
#     def close(self):
#         """关闭数据库连接"""
#         self._conn.colse()
#
# if __name__ == '__main__':
#     sql_table = """CREATE TABLE spring(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         date DATE,
#         btq REAL,
#         hhq REAL
#     )"""
#
#     db = Sqlite3Client(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\water.db')
#     db.create_table(sql_table)
#
#     sql = 'insert into spring (date, btq, hhq) values(?,?,?)'
#     db.execute(sql, ('2021-05-13', 27.58, 27.56))
#
#     sql = 'select * from spring where date = ?'
#     result = db.execute(sql, ('2021-05-13',))
#     print(result)

"""3.4.2 使用MySQL数据库

    学习关系型数据库,你可以不知道Orcale,可以不知道SQLServer,甚至可以不知道DB2,但必须知道MySQL这个
应用最为广泛的数据库。MySQL是一个经典的关系型数据库,由瑞典MySQLAB公司开发, 目前属于Oracle旗下产品。
    大部分Python程序员使用PyMySQL模块和mysqlclient模块访问MySQL数据库。有趣的是,不管是PyMySQL模块
,还是mysqlclient模块,它们在用法上几乎一致,都是基于Python database API version 2.0标准使用的,这个
标准也被称作PEP-0249,这意味着,不用修改代码,只要更换模块名就可以更换数据库客户端。这两个模块的安装都
非常简单,选择其中之一或全部安装均可。PyMySQL模块明确支持访问最新版本的MySQL和MariaDB数据库,而
mysqlien模块关于是否支持访问最新版本数据库的描述模棱两可,因此很多人会把PyMysQL模块作为首选。
但从实际应用来看, mysqlelient模块并没有受到数据库版本的限制。安装命令如下。
1.pip install PyMySQL
2.pip install mysqlclient
    所以我们以PyMySQL模块为例，其最常见的用法是以元组形式返回查询记录，代码如下：把代码中的pymysql
改为MySQLdb即可轻松将PyMySQL模块切换成mysqlclient模块。"""

# import pymysql
# db = pymysql.connect(host='localhost', port=3306, user='liting', password='521liting',
#                      db='demo', charset='utf8')
# cursor = db.cursor()
# cursor.execute('select * from member where id = %s', (100,))

"""    查询记录以元组形式返回会有很多不便,我们需要知道元组各元素对应表结构中的哪一个字段(列)。
下面的代码实现了以字典形式返回查询记录。同样,把代码中的MysQLab改为pymysql,可以轻松将mysqlclient
模块切换成PyMySQL模块。
"""

# import MySQLdb.cursors
# db = MySQLdb.connect(host='localhoost', port=3306, uesr='liting', password='liting521',
#                      db='demo', charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
# cursor = db.cursor()
# cursor.execute('select * from member where id = %s', (100,))
# print(cursor.fetchall())

"""    事务是关系型数据库的重要特性, NoSQL数据库和分布式数据库通常会淡化甚至放弃事务,所谓事务是将
一组DMIL(inert, upate, delet) 多组合在一起形成一个逻辑单元,这些操作如果全部执行并成功提交(commit),
表示事务完成:如果不成功就要回退到事务开始之前的状态(rollack),以确保不会停留在错误的中间状态。
下面的代码演示了MySQL典型的事务回滚应用。
"""

# def transaction(db):
#     try:
#         db.begin()
#         # 此处加入出错之后需要回滚的DML(insert、update、delete)语句
#         db.commit()
#         return True
#     except:
#         db.rollback()
#         return False

"""3.4.3 使用MongoDB数据库
    
    提到NosQL数据库,程序员们首先会想到MongoDB数据库。MongoDB数据库是一个基于分布式文件存储的开源
数据库,被称为最像关系型数据库的非关系型数据库。在实际应用中,程序员会用它来存储一些结构化的数据。我觉
得MongoDB数据库就像一个个性鲜明的优秀青年,既有能力,也有脾气,优点和缺点一样突出。要用好MongoDB数据库
,首先要清楚是否真的需要NoSQL数据库。因为MongoDB数据库的缺点虽然不多,但很致命,这就是被很多人诟病的
“内存贪婪”:它会占用操作系统绝大部分的空闲内存,让其他进程“活得不舒适”。其使用者必须重视这个问题。
不同于关系型数据库, MongoDB数据库只有库的概念而没有表的概念,它使用集合(collection)来代替表,集合中
的每一条数据记录称为文档(.doc),文档可以理解为字典或json对象,也就是若干键值对的组合。关系型数据库要求
同一个数据表中的记录都要保持相同的列结构,但MongoDB数据库并不要求同一个集合中的各个文档保持相同的键,
这就是NosQL数据库最重要的特性之一:无模式。
    从MongoDB的官方网站下载相应的社区版安装程序,安装并启动服务,就可以拥有一个MongoDB服务器。
pymongo模块是Python访问MongoDB数据库的专用模块,使用pip命令即可直接进行安装。
pip install pymongo
用pymongo模块连接MongoDB数据库后,可以查看所有的数据库、删除数据库、选择当前数据库、创建新的数据库
作为当前数据库、在当前数据库创建新的集合、删除当前数据库的某个集合、对集合进行增删改查操作等。
"""

# import pymongo
# conn = pymongo.MongoClient('localhost', 27017) # 连接MongoDB数据库
# conn.list_database_names() # 列出所有的数据库
# db = conn['demo'] # 选中demo库，若不存在，则新建
# db.create_collection('roster')
# db.roster. insert_one({'name':'jack', 'math':95}) # 插入文档
# db.roster. insert_one({'name':'hezhan','math':95}) # 插入文档
# for doc in db.roster.find(): # 查询全部文档
#     print(doc)
# db.roster.update_one({'name':'jj'}, {'$set':{'math':99}}) # 修改文档
# db.roster.delete_one({'name':'jj'}) # 删除文档
# db.list_collection_names() # 列出当前数据库的所有集合
# db.drop_collection('roster') # 删除集合
# conn.drop_database('demo') # 删除库
# conn.close() # 关闭连接

"""
    以上代码简单地演示了MongoDB数据库的基本操作,但MongoDB数据库的价值远远不止增删改查,索引、排序、
聚合、map-reduce等功能才是它大显身手的地方。另外, MongoDB数据库的文件存储(GridFS)、负载扩展、
用户及权限管理等也都极具特色。
"""




