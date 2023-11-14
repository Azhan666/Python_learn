# !/usr/bin/env python
# -*- coding: utf-8 -*-
# import time
#
# time1 = time.time()
#
# import cv2
#
# image=cv2.imread("D:\python_learn\Python基础阶段\趣味代码\孙瑞斌.jpg")
#
# res = cv2.resize(image, (600,400), interpolation=cv2.INTER_AREA)
#
# # cv2.imshow('image', image)
#
# # cv2.imshow('resize', res)
#
# # cv2.waitKey(0)
#
# # cv2.destroyAllWindows()
#
# cv2.imwrite("D:\python_learn\Python基础阶段\趣味代码\孙瑞斌.jpg",res)
#
# time2=time.time()
#
# print (u'总共耗时：' + str(time2 - time1) + 's')

import sys
reload(sys)

sys.setdefaultencoding('utf-8')

############导入计算机视觉库opencv和图像处理库PIL####################

from PIL import Image

from PIL import ImageEnhance

from PIL import ImageFilter

import cv2

import time

time1 = time.time()

########################自定义图像压缩函数############################

def img_zip(path,filename1,filename2):

  image = cv2.imread(path+filename1)

  res = cv2.resize(image, (1280, 960), interpolation=cv2.INTER_AREA)

  cv2.imwrite(path+filename2, res)

  imgE = Image.open(path+filename2)

  imgEH = ImageEnhance.Contrast(imgE)

  img1 = imgEH.enhance(2.8)

  gray1 = img1.convert("L")

  gary2 = gray1.filter(ImageFilter.DETAIL)

  gary3 = gary2.point(lambda i: i * 0.9)

  gary3.save(path+filename2)

################################主函数##################################

if __name__ == '__main__':

  path=u"c:/pic/"

  filename1="0.jpg"

  filename2="1.jpg"

  img_zip(path,filename1,filename2)

  time2 = time.time()

  print(u'总共耗时：' + str(time2 - time1) + 's')