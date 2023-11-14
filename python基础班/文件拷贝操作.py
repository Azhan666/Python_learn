# 文件拷贝操作:
# 输入目标文件名 or 提示缺少目标文件
current_file_name = input('请输入文件名:') # 打开、读取内容:

open_file = open(current_file_name, 'r', encoding='utf8')   # "r" : 打开文件

if open_file:
    # 提取文件的后缀:
    flag_file = current_file_name.rfind('.') # 找到文件名与后缀的分割点   “rfind" : 打开查找文件  '.' : 分割点

    if flag_file > 0:      # "flag" : 标记，即文件后缀

        file_flag = current_file_name[flag_file:] # 由分割点的位置取出文件后缀

        # 创建新的文件名
        new_file_name = current_file_name[:flag_file] + '[复制]' + file_flag

        # 创建新的文件名并写入内容

        new_file = open(new_file_name,'w',encoding='utf8')

        for i in open_file.readlines():     # read（）、readline（）、readlines（）的区别 ：

                                            # read（）：一次性读取文本中字符串的全部内容，以字符串的形式返回结果

                                            # readline（）；只读取第一行的内容，以字符串的形式返回结果

                                            # readlines（）：读取文本所有内容，并以数列的形式返回结果，一般配合 for in 使用
            new_file.write(i)

        open_file.close()
        new_file.close()
    else:
        print('目标文件不存在，请检查！')








