# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" 3.2图像处理"""
"""    图像处理是程序员日常工作的重要内容之一,从图像批量裁切、验证码识别,到训练神经网络自动识别图像中的
特定目标,在程序员成长的每个阶段都需要图像处理技术。本节以打开、保存图像,并对图像做简单处理为学习目标,主
要介绍pillow模块和PyopenCV模块的安装和使用方法。

    3.2.1 PIL和pillow模块
    PIL是Python Imaging Library的缩写,意为Python图像库。它不是Python的标准库,但在很长一段时期内, PIL
几乎就是Python的专用图像库。后来, PIL不再更新,取而代之的是PIL的分支pillow. pillow完全继承了PIL的API,
且支持Py3的图像库。尽管我们在讲述图像处理时经常会提到PIL,但一般情况下指的是pillow. pillow的官网写着:
如果你曾经对PIL的未来表示过担忧或疑惑,请停止(If you have ever worried or wondered about the future 
of PL, pleae stop).
    pillow模块提供了广泛的文件格式支持、高效的内部表示和非常强大的图像处理功能,包含大约25个子模块,其中的
核心是Image模块。Image模块是为快速访问常用基本像素格式有储的数据而设计的,它为一般的图像处理工具提供一个
坚实的基础。表3-3列出了pillow模块中最常用的三个子模块(图像处理、编辑、截屏)以及三个辅助子模块(滤镜、颜色
、字体)。
    表3-3 pillow模块的常用子模块
    子模块             说明
                        

    Image:           Image模块提供了一个同名的类来表示PIL图像,该模块还提供了许多工厂功能、包括从文件加
                     载图像和创建新图像的功能。

    ImageDraw:      ImageDraw模块为图像对象提供了简单的二维(2D)图形,可以使用此模块创建新图像,注释或
                    修改现有图像,以及动态生成图像供Web使用。
    ImageCrab:      ImageGrab模块可用于将屏幕或剪贴板的内容复制到PIL图像内存。
    ImageFilter:    ImageFilter模块包含一组预定义的滤镜,可以与Imagefilter()方法一起使用。
    ImageColon:     ImageColor模块包含颜色表和从CSS3风格的颜色说明行到RGB元组的转换器,这个模块由PIL. 
                    Image.new()和ImageDraw等模块使用。
    ImageFont:      ImageFont模块定义了一个同名的类,配合PIL.ImageDraw.Draw.text)方法使用。
    
    处理图像需要理解图像模式。所谓图像模式就是把色彩分解成部分颜色组件,对颜色组件的不同分类形成了不同的
色彩模式,不同的色彩模式可以影响图像的通道数目和文件大小。
"""
"""
表3-4列出了pillow模块支持的图像模式。

    表3-4 pillow模块支持的图像模式        说明
    1:  黑白,每个像素用1位表示,但存储时每个像素占用1字节
    L:  黑白,每个像素用1字节表示
    P:  调色板映射,每个像素用1字节表示
    RGB:    红、绿、蓝, 3个通道,每个像素用1字节表示
    RGBA:   红、绿、蓝和透明, 4个通道,每个像素用1字节表示
    CMYK:   颜色隔离模式, 4个通道,每个像素用1字节表示
    YCbCr:  亮度、蓝色差、红色差, 3个通道,每个像素用1字节表示
    I:      每个像素用4字节整型表示
    F:      每个像素用4字节浮点型表示
    
1．安装和导入pillow模块
    使用pip命令即可直接安装pillow模块。需要说明的是,因为导入pillow模块的写法与众不同,所以很多初学者会误
把模块名pillow写成PIL,导致安装失败或无法使用。
    pillow模块安装成功后,就可以根据需要导入各个子模块了。一般情况下,不建议使用通配符(*)导入全部子模块。
    
demo:
from PIL import Image, ImageDraw, ImageGrab
from PIL import ImageFont, ImageColor
    
    2.打开和保存图像文件
    下面的代码打开一个图像文件,显示图像模式和图像分辨率后,将RGB模式(彩色)转为L模式(灰度),并将其另存为
新的图像文件,效果如下列代码所示:
"""

from PIL import Image, ImageDraw, ImageGrab
from PIL import ImageFont, ImageColor

# im = Image.open(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷.jpg')
# 打开图像文件
# print(im.mode) # 图像模式，mode：模式
# 'RGB'

# print(im.size) # 图像分辨率
# (1075, 804)

# print(im.show) # 调用系统默认的图像查看工具显示图像
# im_gray = im.convert('L') # 将RGB模式转为L模式，convert：使转换
# print(im_gray.mode) # 图像模式

# im_gray.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷_gray.jpg')
# 保存图像,gray:灰色

"""3.通道合并与拆分
    下面的代码将图像的RGB 3个颜色通道分离，交换红色通道和蓝色通道后，生成新的图像，并将其保存为文件
，效果由阿展自行查看"""

# from PIL import Image, ImageDraw, ImageGrab
# from PIL import ImageFont, ImageColor
#
# im = Image.open(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷.jpg')
# # 打开图像文件
# r,g,b = im.split() # 将RGB图像拆分成独立的3个通道
# g.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷_g.jpg')
# # 保存绿色通道为文件
# im_bgr = Image.merge("RGB",(b,g,r)) # 交换红色、蓝色通道，得到特殊的效果，merge：合并
# im_bgr.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷_bgr.jpg')
# # 保存交换通道后的图像

"""4.旋转、缩放、裁切、复制与粘贴
    图像旋转函数Image.rotate()至少需要一个angle参数，angle：角度，用以指定旋转角度，angle参数是以度
（°）为单位，以逆时针方向为正，此外，Image.rotate()函数还有4个可选的参数，rotate：旋转分别是旋转中心
center，二元组参数，默认为图像中心；扩展标记expand，expand：扩大，默认为False；插值方法resample，
resample：重新取样，默认使用Image.NEAREST，NEAREST:最近的，另外还有Image.BILINEAR，adj. 双线性的
和Image.BICUBIC，adj. [数] 双三次的，可以选择平移转换translate，translate：转换，二元组参数，默认
无平移。
    图像缩放使用Image.resize()函数，resize：vt. 调整大小，该函数按照元组参数指定的宽度和高度返回新
的图像，图像裁剪使用Image.crop()函数，crop：裁切，它接受一个四元组参数，用以指定裁切区域左上角和右下角
的坐标，Image.copy()函数用于复制图像对象，Image.paste()函数用于图像粘贴，它需要两个参数，一个是粘贴的
图像，二是粘贴图像左上角在底图上的位置。"""

# demo:
# im = Image.open(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷.jpg')
# # 打开图像文件
# im_30 = im.rotate(30) # 逆时针旋转30°，以原图分辨率返回新图像
# print(im_30.size)
# # (1075, 804)
#
# im_30.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷.jpg')
# im.rotate(30, expand=True).show() # 逆时针旋转30°，返回扩展的新图像
# im_box = im.crop((150,50,400,200)) # 裁切250×150的局部图像
# im_copy = im_box.copy() # 复制这个局部图像，不是粘贴的必要条件，这里主要用来演示复制功能
# im.paste(im_copy, (350,450)) # 粘贴到底图的右下角
# im.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷_paste.jpg')
# 保存粘贴后的图像
# 结果请查看美美的阿婷！

"""5.使用滤镜
    滤镜，也称图像滤波器，可是对图像实现平滑、模糊、锐化、边界增强、细节增强等特殊效果，ImageFilter
模块包含一组预定义的滤镜，可以与Image.filter()方法一起使用。
    BLUR：   模糊滤镜，blur：模糊
    CONTOUR：轮廓滤镜，contour：轮廓
    DETAIL： 细节增强滤镜，detail：细节
    EDGE_ENHANCE：边界增强滤镜，edge：边缘，enhance：增强，提高
    EDGE_ENHANCE_MORE：深度边缘增强滤镜
    EMBOSS：浮雕滤镜，emboss：浮雕
    FIND_EDGES：勾画边界滤镜
    SHARPEN：锐化滤镜，sharpen：锐化
    SMOOTH：平滑滤镜，smooth：顺利的，平稳的，平滑的
    SMOOTH_MORE：深度平滑滤镜
    
    下面的代码分别使用了细节增强滤镜、模糊滤镜、轮廓滤镜和勾画边界滤镜，效果使用后查看（阿婷怎样都很美）
"""

# from PIL import Image, ImageDraw, ImageGrab, ImageFilter
# from PIL import ImageFont, ImageColor

# im = Image.open(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷.jpg')
# im_detail = im.filter(ImageFilter.DETAIL)
# # 细节增强滤镜
# im_detail.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷_detail.jpg')
# im_blur = im.filter(ImageFilter.BLUR)
# # 模糊滤镜
# im_blur.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷_blur.jpg')
# im_contour = im.filter(ImageFilter.CONTOUR)
# # 轮廓滤镜
# im_contour.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷_contour.jpg')
# im_edges = im.filter(ImageFilter.FIND_EDGES)
# # 勾画边界滤镜
# im_edges.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷_edges.jpg')

"""6.绘图
    ImageDraw子模块提供了线段、圆弧、矩形等图形以及文本的绘制方法，绘制文本时需要使用ImageFont子模块
设置字体对象，和颜色相关的设置则需要导入ImageColor子模块，下面的代码首先生成一张800×300的蓝色背景图，
然后在上面演示了各种几何图形和文本的绘制方法。"""

# from PIL import Image, ImageDraw, ImageGrab, ImageFilter
# from PIL import ImageFont, ImageColor
#
# im = Image.new("RGB", (800,300), color=(32,64,128))
# draw = ImageDraw.Draw(im) # draw:绘制
# draw.line((0, 200, 800, 200), width=2, fill=(255,255,255)) # fill:填充
# draw.arc([20,20,180,180], 0, 270, fill=(0,255,255)) # arc：弧
# draw.arc([200,40,360,160], 0, 360, fill=(0,255,255))
# draw.pieslice([380,20,540,180], 30, 330, fill='red', outline='white') # pieslice：饼图
# draw.ellipse([560,20,780,180], fill='yellow', outline='white') # ellipse：拓源
# draw.point([660,100,670,100,680,100], fill='red') # point：在图像上画点
# draw.rectangle([100,220,700,280], fill=(64,192,192), outline='white') # rectangle：矩形
# font = ImageFont.truetype("simfang.ttf", 32) # truetype：新宋体，simfang：仿宋，.ttf:字体文件
# draw.text([130,230],"人生苦短，我爱阿婷，我用Python", font=font, fill='white')
# im.show() # 调用window图像查看工具查看图像

"""7.截屏
    ImageGrad子模块提供了一个截屏的函数grab(),该函数接受一个四元组参数用以指定截图区域左上角和右下角
在屏幕上的坐标，若省略参数，grab()函数将截取整个屏幕。"""
# from PIL import Image, ImageDraw, ImageGrab, ImageFilter
# from PIL import ImageFont, ImageColor
# # im = ImageGrab.grab((1200,600,1920,1080)) # 截取大小为720×480的屏幕区域
# # im.show()
# im = ImageGrab.grab() # 截取整个屏幕
# im.show()

"""3.2.2 PyOpenCV模块
    严格来讲，PyOpenCV模块并不是一个像pillow模块那样纯粹的图像库，或者说，他不只是一个图像库，OpenCV
的全称是Open Source Computer Vision Library, 意为开源的计算机视觉库,其目标是提供易于使用的计算机视
觉接口,从而帮助人们快速建立精巧的视觉应用。OpenCV和机器学习的关系非常密切,它提供了一个完备的、具有通用
性的机器学习库(ML.模块), PyOpenCV模块是OpenCV的Python封装。
    这一节内容并不是PyOpenCV模块全部功能的讲解,而是它和pillow模块重叠的一部分功能的演示。之所以把
PyOpenCV模块这样一个“重型武器”作为轻量型工具使用,是因为目前的PyOpenCV模块已经不支持以前的图像数据结构,
取而代之的是NumPy数组(numpy.ndarray).而NumPy数组正是本书的重点内容,也是程序员从初级到高级的必修课之一。

    1.安装和导入PyOpenCV模块
    在安装时，有两个PyOpenCV的模块可供选择,一个是opencv-python,包含OpenCV库的主要模块:另一个是
opencv-contrib-python,包含核心功能模块和contrib模块--一个试验性质的新功能库。对于初学者而言,选择前者
就足够用了。
安装命令：pip install opencv-python
由于历史的原因, OpenCV的版本非常复杂,只需要了解目前的导入方法就可以。
# 导包：
#import cv2

    2.打开、显示和保存图像文件
    cv2使用imread()函数打开图像文件,使用imshow()函数显示图像,使用imwrite()函数保存图像,以下代码演示
了使用cv2打开、显示和保存图像等功能,其中用到了NumPy数组的shape属性来查看数组的结构。NumPy数组的属性在
本书的4.14小节中有详细讲解。
"""


import cv2
import numpy as np

# 读取图像，解决imread不能读取中文路径的问题
# 解决办法链接：知乎:https://www.zhihu.com/question/67157462/answer/251754530
# 博客园：https://www.cnblogs.com/byteHuang/p/9597439.html

# def cv_imread(filePath):
#     cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
# # imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
# #cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
#     return cv_img
#
# if __name__=='__main__':
#
#     path='D:\桌面\img\阿婷.jpg'
#     img=cv_imread(path)
#     cv2.namedWindow('阿婷',cv2.WINDOW_AUTOSIZE)
#     cv2.imshow('阿婷',img)
#     img = cv2.imread(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷.jpg',cv2.IMREAD_UNCHANGED)
#     # RGBA模式
#     # cv2.shape
#     img = cv2.imread(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷.jpg',cv2.IMREAD_GRAYSCALE)
#     # 灰度模式
#     # cv2.shape
#     k=cv2.waitKey(0)
#     cv2.imwrite(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷_gray.jpg',img)
# #这样是保存到了和当前运行目录下
# cv2.imencode('.jpg', img)[1].tofile('阿婷.jpg')
"""     在这段代码中，图像本来是RGBA模式的，但是如果像第一行代码那样用默认的方式（cv2.IMMREAD_COLOR）
打开，则会忽略图像的透明度，如果想要保留透明通道，则需要使用cv2.IMREAD_UNCHANGED参数声明，使用
cv2.IMREAD_GRAYSCALE参数，则会以灰度模式打开图像。

    3.绘图
    使用NumPy数组作为图像格式的好处是可以直接使用NumPy数组强大的处理功能，事实上OpenCV提供的大量函数
基本上都是基于NumPy数组实现的，这里只介绍几个绘图函数"""

# import numpy as np
# import cv2
#
# im = np.zeros((300, 800, 3), dtype = np.uint8) # 生成800×300的黑色背景图
# im = cv2.line(im, (0,200),(800,200),(0,0,255), 2) # 画线
# im = cv2.rectangle(im,(20,20),(180,180),(255,0,0), 1) # 画矩形
# im = cv2.circle(im, (320,100), 80,(0,255,0), -1) # 画圆
# font = cv2.FONT_HERSHEY_SIMPLEX
# # 写文本（仅限英文，如果需要中文，需要转pillow来实现）
# im = cv2.putText(im, 'Hello, world.', (420,100), font, 2, (255,255,255), 2, cv2.LINE_AA)
# cv2.imshow('Image', im)

""" 这段代码使用NumPy函数zeros()生成黑色背景图，zeros()函数在高手修炼之道4.2.2小节有详细讲解
    
    4.cv2格式和PIL格式的互转
    前面说过，cv2格式的图像就是NumPy数组，也就是numpy.ndarray对象，只要能实现PIL对象和NumPy
数组互转，就能实现PIL对象和cv2对象互转，需要注意的是，cv2格式图像的RGB模式，三个颜色的顺序BGR，
转换时需要交换R通道和B通道。
    下面代码演示了用pillow模式读取PNG格式的图像文件，转成NumPy数组后，再用cv2保存为PNG格式的
图像文件。
"""

# import cv2
# from PIL import Image
# import numpy as np
# im_pil = Image.open(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷.jpg')
# im_cv2 = np.array(im_pil) # array:数组
# cv2.imwrite(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷.jpg', im_cv2[:,:,[2,1,0]])

""" 下面的代码用cv2读取PNG格式的图像文件，转成PIL对象后，再用pillow模块保存为jpg格式的图像文件"""

# import cv2
# from PIL import Image
# im_cv2 = cv2.imread(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷.png')
# im_pil = Image.fromarray(im_cv2[:,:,[2,1,0]])
# im_pil.save(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷.jpg')






