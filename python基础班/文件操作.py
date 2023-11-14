#文件操作：（使用open函数打开或创建一个文件需要加上‘w')'w':wrint,'r':read
#写完open函数记得马上写关闭close

import time

start_time = time.time()
f = open('aaa.text','r') #将’w'改成'a',不会覆盖先前的输入内容，将文件名‘aaa’更改将新创建文件进行输入

#f.write('123456')

f.close()
print(f)