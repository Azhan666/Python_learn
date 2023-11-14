# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""3.3 数据文件读写
    有了数据,自然就需要对数据进行存储、读写和分发。数据的存储、读写和分发一般有两大模式:数据库模式和
数据文件模式。最常见的数据文件类型是Excel表格和CSV文件,在科研领域, HDF和netCDF也是常用的数据文件格式。

    3.3.1 读写Excel文件
    Excel文件有两种格式,分别对应.xls和.xlsx两种扩展名(XLS格式和XLSX格式),前者使用97-2003模板,是早期
的文件格式,现在已经逐渐被后者所淘汰,但仍然会遇到XLS格式的数据文件需要处理. openpyxl模块专门用于读写
XLSX格式的文件, xlrd模块和xlwt模块则专门用于读写XLS格式的数据文件。这3个模块都可以使用pip命令安装,
如果不需要处理XLS格式的数据文件,那么只需要安装openpyxl模块就可以了。
pip install openpyxl
pip install xlrd
pip install xlwt

    1.使用openpyxl模块读写XLSX格式的文件
    Excel文件的基本操作就是对文件（book）和工作表（sheet）进行的操作，使用openpyxl模块读写Excel
文件，需要使用到book和sheet的概念，Openpyxl模块使用load_workbook()函数将已有的Excel文件读写成book
对象，这两种方式得到的book对象都可以读写。

    下面的代码演示了如何使用openpyxl模块编辑XLSX格式的Excel文件。"""

# from openpyxl import load_workbook
#
# wb = load_workbook(r'D:\桌面\招聘\猎聘网\数据分析前两页(河北).xlsx')
# print(wb.sheetnames)
# # ['数据分析岗位_河北']
# sh = wb['数据分析岗位_河北']  # 选择表
# print(sh.max_row)  # 有效行数
# print(sh.max_column)  # 有效列数
#
# print(sh['C1'])  # 返回C1单元格对象
# # print(sh['C1'].value) # 返回C1单元格内容
#
# # print(sh[1][2].value) # 也可以这样指定单元格
# alter = sh['C1'].value = '美股上市'  # alter：修改
# print(alter)
# wb.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\数据分析前两页(河北)_demo.xlsx')

"""    下面的代码演示了如何使用openpyxl模块创建XLSX格式的Excel文件"""

# from openpyxl import Workbook
# wb = Workbook() # 创建book，（方法名需要加括号）
# sh0 = wb.active # 激活默认的sheet，active：积极的，活跃的
# sha = wb.create_sheet("成绩表") # 创建新表，create：创建
# shb = wb.create_sheet("收支表") # 创建新表
# sha.append(['姓名','大学语文','高数','计算机文化基础','大学俄语','大学政治','Python']) # 可以在末尾追加一行
# sha.append(['Hezhan','98','96','100','95','97','100'])
# sha['B2'] = 99 # 也可以单独写单元格
# print(wb.sheetnames) # 显示全部表名
# del wb['Sheet'] # 删除表
# wb.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\创建Excel_demo.xlsx')


"""    下面代码演示了如何使用openpyxl模块设置字体、单元格等的样式"""

# from openpyxl import Workbook
# from openpyxl.styles import Font, colors, Alignment # Alignment:对齐
#
# wb = Workbook() # 创建book
# sh = wb.active # 激活默认的sheet
# f1 = Font(name='微软雅黑', size=16, italic=True, color=colors.BLACK, bold=True) # italic：斜体
# # bold：粗体
# sh['A1'].font = f1 # 设置字体
# align = Alignment(horizontal='center', vertical='center') # horizontal：水平，vertical：垂直
# sh['B2'].alignment = align # 设置对齐方式
# sh.row_dimensions[2].height = 24 # 设置第二行高度，dimensions：规模，大小
# sh.column_dimensions['C'].width = 20 # 设置C列宽度, column:纵队（列）
# sh.merge_cells('A3:C4') # 合并A3到C4的单元格，merge：合并
# wb.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\创建Excel.styles_demo.xlsx')

"""2.使用xlrd模块读写XLS格式的文件
    使用xlrd模块读写Excel文件的方法与使用openpyxl模块读写Excel文件非常类似。用xlrd模块打开一个Excel文件
,返回的是一个book对象,使用sheet名或序号从book的数据表中选择一个sheet,即可从中读取数据。
    下面列出了xlrd模块的book对象的常用方法。
        方法                                功能描述
                                        
    sheets()                      ：     取得所有的工作表对象列表
    sheet_by_index(sheet_indx)    ：     通过索引顺序获取工作表对象
    sheet_by_name(sheet_name)     ：     通过名称获取工作表对象
    sheet_names()                 ：     返回book中所有工作表的名字
    sheet_loaded(sheet_name or indx)：   检查某个sheet是否导入完毕
    
    下面列出了xlrd模块的sheet对象的常用方法:
    
        方法                                 功能描述
        
        nrows 获取sheet中的有效行数
        ncols 获取sheet中的有效列数
        row(row_idx) 返回指定行中所有单元格对象组成的列表
        row_slice(row_idx,start_cols=0,end_cols=None) 返回指定行中所有单元格对象组成的列表
        row_types(row_idx,start_cols=0,end_cols=None) 返回指定行中所有单元格数据类型组成的列表
        row_values(row_idx,start_cols=0,end_cols=None) 返回指定行中所有单元格数据组成的列表
        row_len(row_idx) 返回指定有效单元格长度
        col(col_idx,start_rowx=0,end=None) 返回指定列中所有单元格对象组成的列表
        col_slice(col_idx,start_rowx=0,end_rowx=None) 返回指定列中所有单元格对象组成的列表
        col_types(col_idx,start_rowx=0,end_rowx=None) 返回指定列中所有单元格数据类型组成的列表
        col_values(col_idx,start_rowx=0,end_rowx=None) 返回指定列中所有单元格数据组成的列表
        cell(row_idx,col_idx)   返回指定单元格对象
        cell_type(row_idx,col_idx)   返回指定单元格中的类型数据
        cell_value(row_idx,col_idx) 返回指定单元格中的数据
        
    下面的代码演示了使用xlrd模块从Excel文件中读取数据的方法"""

# import xlrd
# book = xlrd.open_workbook(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\test_demo_files\副本腾讯招聘1.xls')
# print(book.sheet_names()) # 获取全部表名
# # ['腾讯招聘']
# sh = book.sheet_by_name('腾讯招聘') # 通过表名取得sheet对象
# sh = book.sheet_by_index(0) # 通过索引取得sheet对象
# print(sh.nrows) # 有效行数
# # 34655
# print(sh.ncols) # 有效列数
# # 6
# sh.row_values(3, start_colx=3, end_colx=8) # 读取第3行的第3列至第8列的值
# print(sh.row_values(3, start_colx=3, end_colx=8))
# # ['', '', '']
# sh.col_values(2, start_rowx=3, end_rowx=10) # 读取第2列的第3行至第10行的值
# print(sh.col_values(2, start_rowx=3, end_rowx=10))
# # ['', '', '', '', '', '', '']
# sh.cell_value(3,4) # 返回第3列至第4列的值
# print(sh.cell_value(3,4))

"""3.使用xlwt模块生成XLS格式的文件
    使用xlwt模块只能生成新的Excel文件,不能对已有的Excel文件进行编辑。其使用方法与使用xlrd读取Excel文
件有点类似,首先创建一个book对象,然后添加sheet,并对sheet做写入操作。另外, xlwt模块还提供了单元格、字体、
边框等样式的设置方法。
    下面的代码演示了使用xlwt模块创建XLS格式的Excel文件,并向其中添加太阳系八大行星数据,最后合并单元格,
并插入求和公式。
"""
# data = [('水星',0.58,0.5), ('金星',1.08,0.82), ('地球',1.50,1.00), ('火星',2.28,0.11),
#         ('木星',7.78,317.94), ('土星',14.27,95.18), ('天王星',28.70,14.63),
#         ('海王星',44.97,17.22)]
# import xlwt
# book = xlwt.Workbook() # 创建book对象
# sh = book.add_sheet("太阳系行星") # 添加名为太阳系行星的sheet
# col_names = ['行星', '距离(亿千米)', '与地球的质量比'] # 列名称
# for col, name in enumerate(col_names): # 列名写在第0行
#     sh.write(0, col, name)
#     sh.col(col).width = 256 * 20 # 设置列宽度为20个字符宽度
# for i, line in enumerate(data): # 逐行逐列写入数据
#     for j, item in enumerate(line):
#         sh.write(i+1, j, item)
# sh.write_merge(9, 9, 0, 2, xlwt.Formula('SUM(C2:C9)')) # Formula：公式
# book.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\test_demo_files\Xlwt_生成_Excel_.xls')

"""如果需要编辑已有的Excel文件，则需要借助于xlutils模块复制一个book对象，由于XLS格式已经被XLSX格式
所取代，这里就不再详细介绍xlutils模块的使用方法了。

    3.2.2 读写CSV文件
    csv是Comma-Separated Values的缩写,意为逗号分隔值,但分隔符不仅限于逗号。CSV是一种通用的、相对简单
的文件格式,以纯文本形式存储表格数据。CSV文件由任意数目的记录组成,记录间以某种换行符分隔;每条记录由字段
组成,字段间的分隔符采用其他字符或字符串,最常见的是逗号和制表符。通常情况下,所有记录都有完全相同的字段序
列。尽管很多数据处理模块自带CSV文件读写功能,但不依赖任何第三方模块,有时候只用Python的标准函数open()读
写CSV文件会更加方便和灵活。"""

# def read_csv(csv_file, sep=','):
#     data = list()
#     with open(csv_file, 'r') as fp:
#         for line in fp.readlines():
#             row = [float(item) for item in line.strip().split(sep)]
#             data.append(row)
#         return data
#
# def write_csv(data, csv_file, sep=','):
#     with open(csv_file, 'w') as fp:
#        for row in data:
#         fp.write(sep.join([str(item) for item in row]))
#         fp.write('\n')
# data = read_csv(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\test_demo_files\tieba.csv')
# # 读取csv文件
# print(data)
# # [[0.9998776, -263848.0, 0.7655788]]
#
# write_csv(data, r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\test_demo_files\test.csv')

"""3.3.3 读写HDF文件
    HDF(Hierarchical Data File, 多层数据文件),是美国国家高级计算应用中心(NationalCenter for 
Supercomputing Application, NCSA)为满足各种领域研究需求而研制的,是一种能高效存储和分发科学数据的新
型数据格式。HDF可以表示出科学数据存储和分布的许多必要条件、HDF提供6种基本数据类型:光栅图像、调色板、
科学数据集、注解、虚拟数据和虚拟组。
HDF有多个版本,最新版本的HDF发布于1998年。读写HDF5格式的文件需要使用h5py模块,该模块可以使用pip命令直
接进行安装。
pip install h5py
    下面以精度为0.5°的全球经纬度网格和对应该网格的全球温度数据（使用随机数模拟）为例，演示如何创建和
使用HDF文件。"""

# import numpy as np
# lats, lons = np.mgrid[-90:90:361j, -180:180:721j] # mgrid：制造网格
# temp = np.random.randint(100, 300, lons.shape) # temp：温度
# print(lons.shape, lats.shape, temp.shape)

# lons和lats分别指的是经度网格和纬度网格，temp是对应经度网格的开氏温度（热力学温度）数据，它们都是
# 361行721列的二维数组，生成经度网格和模拟的全球温度数据都使用了NumPy模块创建数组的网格构造语法，
# 网格构造语法在高手修炼之道4.2.6小节有详细讲解。

# import h5py
# fp = h5py.File(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\test_demo_files\hdf_file.hdf', 'w')
# lons_dataset = fp.create_dataset("lons", data=lons) # 写入经度数据集 create:创造
# lats_dataset = fp.create_dataset("lats", data=lats) # 写入纬度数据集
# temp_dataset = fp.create_dataset("temp", data=temp) # 写入温度数据集
# lons_dataset.attrs["lons_range"] = [-180, 180] # 写入经度属性,attrs:属性
# lats_dataset.attrs["lats_range"] = [-90, 90] # 写入纬度属性
# temp_dataset.attrs["temp_range"] = [100, 300] # 写入温度属性
# fp.close()

# 几行代码就把3个数据集写入了HDF文件，同时还写入了各个数据集的值域范围，如果有必要，还可以写入
# 数据集的其他属性，读出这些数据集的操作也非常简单，其代码形式如下：

# fp = h5py.File(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\test_demo_files\hdf_file.hdf', 'r')
# lons = fp["lons"].value
# lats = fp["lats"].value
# temp = fp["temp"].value
# print("LONS:", lons.shape, fp["lons"].attrs["lons_range"])
# print("LATS:", lats.shape, fp["lats"].attrs["lats_range"])
# print("TEMP:", temp.shape, fp["temp"].attrs["temp_range"])
# fp.close()

"""3.3.4 读写netCDF文件
    netCDF (network Common Data Form,网络通用数据格式)是由美国大学大气研究协会(Unversity 
Corporation for Atmospheric Research, UCA)的Unidata项目科学家针对科学数据的特点开发的,是一种面向
数组型并适用于网络共享数据的描述和编码标准。目前, netCDF广泛应用于大气科学、水文、海洋学、环境模拟、
地球物理等领域。
    读写netCDF文件需要使用netCDF4模块,该模块可以使用pip命令直接进行安装。
pip install netCDF4
    本节以上一节生成的经纬度网格数据和对应该网格的全球温度数据为例,演示如何创建和使用netCDF文件。
和生成HDF文件不同,生成netCDF文件前需要先指定基础变量的维度信息。
    在本案例中,我们需要指定经度、纬度这两个基础变量的维度为721和361.
"""

# import netCDF4
# import numpy as np
#
# fp = netCDF4.Dataset(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\test_demo_files\netCDF_file.nc', 'w', format='NETCDF4')
# fp.createDimension('lons', size=721) # 设置经度的维度
# fp.createDimension('lats', size=361) # 设置纬度的维度
# lons_var = fp.createVariable("lons", 'f' ,("lons",)) # 创建lons数据集
# lats_var = fp.createVariable("lats", 'f' ,("lats",)) # 创建lats数据集
# fp.Variables['lons'][:] = np.linspace(-180,180,721) # lons数据集赋值
# fp.Variables['lats'][:] = np.linspace(-90,90,361) # lata数据集赋值
# lons_var.lon_range = [-180, 180]
# lats_var.lat_range = [-90, 90]
# fp.createVariable('temp','f8',('lats','lons')) # 创建temp数据集
#
# fp.variables['itemp'][:] = np.random.randint(100, 300, (361, 721)) # temp数据集赋值
# # 虽然生成netCDF文件的过程比较繁琐，但netCDF文件使用起来非常方便，使用netCDF文件的代码如下：
#
# fp = netCDF4.Dataset(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\test_demo_files\netCDF_file.nc', 'r', format='NETCDF4')
# lons = fp.variables['lons'][:]
# lats = fp.variables['lats'][:]
# temp = fp.variables['temp'][:]
# print(lons.shape, fp.variables['lons'].last_range)
# print(lats.shape, fp.variables['lats'].last_range)
# print(temp.shape)
# fp.close()








