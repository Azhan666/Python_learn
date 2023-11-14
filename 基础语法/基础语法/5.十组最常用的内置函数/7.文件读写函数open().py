# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 文件读写是程序员最基本的技能之一。好在Python的文件读写非常简单，很容易上手。读写文件时，
# 不管正常结束还是非正常结束，一定要关闭文件————通常需要捕获异常并进行处理。为了简化代码，
# 使之更加“优雅”，建议使用with-as的语法结构来读写文件。关于with-as，在高手修炼之道2.2.6
# 小节有详细讲解。

# 下面的例子演示了如何将数据写入csv文件，以及如何读出csv文件中的数据并解析。

data = [[0.468,0.975,0.446],[0.718,0.826,0.359]]
with open(r'd:\csv_data.csv','w') as fp: # 写入csv文件
    for line in data:
        ok = fp.write('%s\n'%','.join([str(item) for item in line]))
        # join:连接 加入 参加

result = list()  # result:结果 比赛结果 成果
with open(r'd:\csv_data.csv','r') as fp: # 读出csv文件并解析
    for line in fp.readlines():
        result.append([float(f) for f in line.strip().split(',')])
        # strip:条子 脱衣 长片
result
print(data)