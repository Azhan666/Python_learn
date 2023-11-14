# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""第5章 动态渲染页面抓取 """

"""     在第4章中，了解了Ajax的分析和抓取方式，这其实也是JavaScript动态渲染页面的一种情形，通过直接分析
Ajax，用户仍然可以借助requests或urllib实现数据抓取。
    不过JavaScript动态渲染不止Ajax这一种，例如，中国青年网（http://news.youth.cn/gn）的分页部分是由
JavaScript生成的，并非原始HTML代码，这其实并不包含Ajax请求，又如，ECharts的官方实例（http://
echarts.baidu.com/echarts2/doc/example.html）中的图像都是经过JavaScript计算后生成的，再如，
像淘宝、京东这些网页中的很多页面虽然是Ajax获取的数据，但是其中的Ajax接口有很多加密参数，难以直接
找出规律，也很难直接分析Ajax来抓取。
    为了解决这些问题，可以直接使用模拟浏览器的方式来实现，这样就可以做到在浏览器中看到的是什么样，
抓取的源码就是什么样，也就是可见即可爬，这样就不用再管网页内部的JavaScript用了什么算法渲染页面，
以及网页后台的Ajax接口到底有哪些参数。
    Python提供了许多模拟浏览器运行的库，如Selenium、Splash、execjs、Ghost等，本章中着重介绍
Selenium和Splash库的用法，有了他们就不用再为动态渲染页面发愁了。
"""

"""本章主要涉及的知识点：
    1.selenium的基本用法
    2.splash的基本用法
    3.使用selenium和splash实现一个动态网页抓取练习
"""

"""5.1 Selenium 的使用
    Selenium是一个自动化测试工具，selenium测试工具直接运行在浏览器中，支持的浏览器包括ie（7、8、9）、
火狐、谷歌等等，这个工具的主要功能包括测试与浏览器的兼容性，即测试应用程序是否能够很好的工作在不同
浏览器和操作系统之上，驱动浏览器执行特定的动作，如鼠标单击、下拉列表等动作，同时还可以获取浏览器当
前呈现的网页源代码，做到可见即可爬，对于一些JavaScript动态渲染的页面来说，此种抓取方式非常有效。

    5.1.1 安装selenium库
    步骤1：安装selenium库非常简单，只需使用pip命令即可
    步骤2：安装浏览器驱动，因为selenium 3.x调用浏览器必须要有一个WebDriver驱动文件，相关下载地址如下：
    Chrome驱动文件下载：https://chromedriver.storage.googleapis.com/index.html?path=2.35
    Firefox驱动文件下载：https://github.com/mozilla/geckdriver/releases
    步骤3：设置浏览器驱动的环境变量，手动创建一个存放浏览器驱动的目录，如D:\apk\chromedriver,
将下载的浏览器驱动文件放到该目录下，如果是Linux系统，把下载的文件放在/usr/bin目录下就可以了。
    步骤4：设置【我的电脑】-->[属性]-->[系统设置]-->[高级]-->[环境变量]-->[系统变量]-->[Path],
将路径添加到Path的值中
    步骤5：在Python中执行以下代码，用chrome浏览器测试是否安装成功：
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://ww.baidu.com')
    运行这段代码，会自动打开浏览器，然后访问百度，如果程序执行错误，浏览器没有打开，那么应该是
环境变量设置出现问题。
    温馨提示：
    chromedriver的版本需要与使用的chrome浏览器版本对应，否则会报错，如果浏览器为Firefox，
需要将webdriver.Chrome()替换成webdriver.Firefox(),其他方法不变，后面所涉及的代码示例都是这样。

    5.1.2 selenium 定位方法
    selenium提供了8种元素定位方法，通过这些定位方法，用户可以定位指定元素，提取数据或给指定的元素
绑定事件，设置样式等，这8种方法分别为id、name、class name、tag name、link text、partial link text、
xpath和css selector。这8种定位方法在Python Selenium中所对应的方法格式为：find_element_by_id()、
find_element_by_name、find_element_by_class_name()等等

    下面来看看这些方法应该如何使用，以百度首页为例，通过前端工具（如Chrome或Firebug）查看一个元素的属性
根据属性来使用对应的比较方便的定位方法：

    （1）通过id定位：
    browser.find_element_by_id("kw")
    （2）通过name定位：
    browser.find_element_by_name("wd")
    （3）通过class name定位：
    browser.find_element_by_class_name("wd")
    （4）通过....一样的，不再演示嘿嘿
    
    关于selenium的定位使用的基本情况已经介绍完毕，在实际开发中可能用不了这么多，用户根据实际情况选择
一两种就可以了。

    5.1.3 控制浏览器操作
    selenium不仅能定位元素，还能控制浏览器的操作，如设置浏览器的大小、控制浏览器前进、后退、刷新页面等。
    1.设置浏览器大小
    有时用户会希望页面可以以某种浏览器尺寸打开，让访问的页面在这种尺寸下运行，例如，将浏览器设置成
移动端大小（480px×800px），然后访问移动站点，并对其样式进行评估，WebDriver提供了set_window_size()
方法来设置浏览器的大小，实例代码如下："""

# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com')
# # 参考数字为像素点
# print("设置浏览器宽480px、高800px显示")
# browser.set_window_size(480,800)
# browser.quit()

# 执行此代码，将会弹出谷歌浏览器到百度首页，并将浏览器窗口大小设置成480×800px，由于在弹出浏览器之后
# 执行了browser.quit()方法，所以会在打开浏览器几秒后自动关闭。

""" 2.控制浏览器后退、前进
    在使用浏览器浏览网页时，浏览器提供了后退和前进按钮，可以方便地在浏览过的网页之间切换，WebDriver
也提供了对应的back()和forward()方法来模拟后退和前进按钮，下面通过例子来演示这两个方法的使用："""

# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
#
# # 访问百度首页
# first_url = 'http://www.baidu.com'
# print("now access %s"%(first_url))
# browser.get(first_url)
# time.sleep(2)
# # 访问新闻页面
# second_url = 'http://news.baidu.com'
# print("now access %s"%(second_url))
# browser.get(second_url)
# time.sleep(2)
# # 返回（后退）到百度首页
# print("back to %s"%(first_url))
# browser.back()
# time.sleep(2)
# # 前进到新闻页
# time.sleep(2)
# print("forward to %s"%(second_url))
# browser.forward()
# browser.quit()

# 为了看清楚脚本的执行过程，上面每操作一步都通过print()来打印当前的url地址，
# 执行代码后将会在控制台看到url结果
# 由结果可知，他已经访问了三个不同的url

""" 3.刷新页面
    刷新页面非常简单，只需要使用browser.refresh()方法就可以刷新页面，示例代码如下："""

# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# # 访问csdn
# url = 'https://www.csdn.net'
# browser.get(url)
# # 刷新当前页面
# browser.refresh()

""" 5.1.4 WebDriver 常用方法
    前面已经学习了定位元素，定位只是第一步，定位之后需要对这个元素进行操作，或单击（按钮）或输入（输入框），
下面就来认识WebDriver中最常用的几个方法
    1.clear() 清除文本
    通过clear()方法，可以清除如input、textarea等From表单文本，如下代码通过选择器获取到元素后调用clear()
方法清除，如书本p103的图5-3，清除出发城市input输入框的默认值。
    下面我也来访问南方航空，清除出发城市默认值："""

# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
#
# # 访问南方航空
# url = 'https://www.csair.com/cn/'
# browser.get(url)
# # 定位出发城市输入框
# # 通过观察，我们可以使用id定位：
# time.sleep(2)
# # 使用clear()方法清除
# # browser.find_element_by_id("fDepCity").clear()

""" 2.send_keys(value)模拟按键输入
    如果用户想要模拟表单输入，可以使用send_keys()方法，通过它就能设置input的值，实例代码如下："""

# browser.find_element_by_id("fDepCity").send_keys("上海")
# 运行这段代码可能会报错，这是因为通过find_element_by_id()方法返回的是一个webElements列表，
# 所以需要对代码进行修改，改为取第0个，修改后的代码如下：
# browser.find_elements_by_id("fDepCity")[0].send_keys("上海")

"""细心的读者在实际操作中会发现，根据id定位会提示有两种方法，find_elements_by_id()和
find_element_by_id()，前者返回的是一个列表，后者返回的是一个单一对象，所以这里推荐大家在
实际开发过程中使用后者，这是代码可以修改如下："""

# browser.find_element_by_id("fDepCity").send_keys("上海")

""" 3.click()模拟单击
    在表单提交时需要单击按钮，这时用selenium的click()方法就可以了，通过选择器获取到按钮元素，
直接调用click()方法，相关示例代码如下：
"""
# browser.find_element_by_id("fDepCity").click()

""" 4.submit()提交
    在访问csdn时，需要在搜索框中输入关键词，然后单击搜索按钮提交，在selenium中，除了可以使用click()
方法外，还可以使用submit()方法模拟，示例代码如下：
"""
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://www.csdn.net")
# search_text = driver.find_element_by_id('toolbar-search-input')
# search_text.send_keys('selenium')
# driver.find_element_by_id("toolbar-search-button").click()
# search_text.submit()
# time.sleep(2)
# driver.quit()

# 有时submit()方法可以与click()方法互换来使用，submit()方法同样可以提交一个按钮，但submit()方法的
# 应用范围远不及click()方法广泛。

# 再来在上面使用click()点击一下搜索:driver.find_element_by_id("toolbar-search-button").click()

""" 5.1.5 其他常用方法
    除了前面的几种方法外，还有几种方法也是实际开发中用得比较多的，具体如下：
（1）size：返回元素的尺寸
（2）text：获取元素的文本
（3）get_attribute(name)：获取属性值
（4）is_displayed()：设置该元素是否用户可见
相关示例代码如下："""

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.csdn.net")
# # 获取输入框的尺寸
# size = driver.find_element_by_id("toolbar-search-input").size
# print(size)
# # 返回csdn首页底部备案信息
# text = driver.find_element_by_id("csdn-copyright-footer").text
# print(text)
# # 返回元素的属性值，可以是id、name、type或其他任意属性
# attribute = driver.find_element_by_id("toolbar-search-input").get_attribute('type')
# print(attribute)
# # 返回元素的结果是否可见，返回结果为True或False
# result = driver.find_element_by_id("toolbar-search-input").is_displayed()
# print(result)
# driver.quit()

"""5.1.6 鼠标键盘事件
    在selenium webdriver中也提供了一些关于鼠标和键盘操作的方法，如鼠标指针悬浮、鼠标指针滑动、
键盘输入等。
    1.鼠标事件
    在selenium webdriver中，将关于鼠标操作的方法封装在ActionChains类中来使用，ActionChains
类方法如下所示：
    方法：
    Action_Chains(driver):   构造ActionChains对象
    context_click():         单击鼠标右键
    double_click():          双击鼠标左键
    drag_add_drop(source,target):   拖拽到某个元素后松开
    drag_and_drop_by_offset(source,xoffset,yoffset):    拖拽到某个坐标后松开
    key_down(value,element=None):   按下某个键盘上的键
    key_up(value,element=None):     松开某个键
    move_by_offset(xoffset,yoffset):    鼠标从当前位置移动到某个坐标
    move_to_element(to_element):    鼠标移动到某个元素
    move_to_element_with_offset(to_elemnet,xoffset,yoffset):    移动到某个元素（左上角坐标）
    多少距离的位置
    release(on_element=None):   在某个元素位置松开鼠标左键
    send_keys(*keys_to_send):   发送某个键到当前焦点的元素
    send_keys_to_element(element,*keys_to_send):    发送某个键到指定元素
    
    下面通过一个示例来看看如何使用鼠标事件，以csdn首页（https://www.csdn.net)为例，通
常来说，如果用户把鼠标指针移动到csdn首页的【更多】菜单项上悬浮，此时会出现一个隐藏的菜单，
如果将鼠标移开，它就又会消失，下面使用selenium webdriver实现模拟鼠标指针移动到csdn首页
更多菜单项悬浮的事件，相关示例代码如下："""

# from selenium import webdriver
# # 引入ActionChains类
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
# driver.get("https://www.csdn.net")
#
# # 定位到要悬停的元素 above：...上面
# above = driver.find_element_by_xpath('//*[@id="floor-nav_62"]/div/div/div[2]/ul/li[16]/a')
# # 对定位到的元素执行鼠标指针悬停操作
# ActionChains(driver).move_to_element(above).perform() # perform:执行

"""     通过上面的代码可以看到，其实关键就是ActionChins(driver).move_to_element(above).perform()
这句代码，使用ActionChins类去调用move_to_element(above)悬浮事件，然后执行perform()方法提交动作。

    2.键盘事件
    前面了解到，send_keys()方法可以用来模拟键盘输入，除此之外，还可以用它来输入键盘上的按键，甚至是
组合键，如[Ctrl+A]组合键和[Ctrl+C]组合键，Keys()类提供了键盘上几乎所有按键的使用方法。

    Keys类常用方法如下：
    方法：
    send_keys(Keys.BACK_SPACE):     删除键（Backspace）
    send_keys(Keys.SPACE):  空格键（Space）
    send_keys(Keys.TAB):       制表建（Tab）
    send_keys(Keys.ESCAPE):     回退键（Esc）
    send_keys(Keys.ENTER):      回车键（Enter）
    send_keys(Keys.CONTROL,'a'):    全选（ctrl+A）
    send_keys(Keys.CONTROL,'c'):    粘贴（ctrl+C）
    send_keys(Keys.CONTROL,'x'):    剪切（ctrl+X）
    send_keys(Keys.CONTROL,'v'):    粘贴（ctrl+V）
    send_keys(Keys.F1):     F1键
    send_keys(Keys.F12):     F12键
    
    关于selenium webdriver常用的鼠标键盘事件方法已经介绍完毕，下面以csdn首页为例，键盘事件方法
的相关示例代码如下："""

# from selenium import webdriver
# # 引入Keys模块
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://www.csdn.net")
#
# # 在输入框中输入内容
# driver.find_element_by_id("toolbar-search-input").send_keys("seleniumm")
# time.sleep(1)
# # 删除多输入的内容
# driver.find_element_by_id("toolbar-search-input").send_keys(Keys.BACK_SPACE)
# # 此方法默认只删除一下
# time.sleep(1)
# # 输入空格键+“教程”
# driver.find_element_by_id("toolbar-search-input").send_keys(Keys.SPACE)
# driver.find_element_by_id("toolbar-search-input").send_keys("教程")
# time.sleep(1)
# # 按【Ctrl+A】组合键全选输入框的内容
# driver.find_element_by_id("toolbar-search-input").send_keys(Keys.CONTROL,'a')
# time.sleep(1)
# # 按【Ctrl+X】组合键剪切输入框的内容
# driver.find_element_by_id("toolbar-search-input").send_keys(Keys.CONTROL,'x')
# time.sleep(1)
# # 按【Ctrl+V】组合键粘贴输入框的内容
# driver.find_element_by_id("toolbar-search-input").send_keys(Keys.CONTROL,'v')
# time.sleep(1)
# # 按【Enter】键代替单击操作
# driver.find_element_by_id("toolbar-search-button").send_keys(Keys.ENTER)
# time.sleep(1)
#
# driver.quit()


"""5.1.7 获取断言信息
    不管是做功能测试还是自动化测试，最后一步都需要将实际结果与预期进行比较，这个比较
称为断言，通常可以通过获取title、url和text等信息进行断言，text方法在前面已经讲过，
它用于获取标签之间的文本信息，下面同样以csdn为例，介绍如何获取这些信息，示例代码如下："""

# from selenium import webdriver
# from time import sleep
# import time
#
# driver = webdriver.Chrome()
# driver.get("http://www.csdn.net")
# print('=======搜索以前======')
#
# time.sleep(1)
# # 打印当前页面title
# title = driver.title
# print(title)
#
# time.sleep(1)
# # 打印当前页面url current:当前的
# now_url = driver.current_url
# print(now_url)
#
# time.sleep(1)
# driver.find_element_by_id("toolbar-search-input").send_keys("selenium")
# driver.find_element_by_id("toolbar-search-button").click()
#
# print('======弹出搜索======')
#
# time.sleep(1)
# # 再次打印当前页面title
# title_1 = driver.title
# print(title_1)
#
# time.sleep(1)
# # 再次打印当前页面url
# now_url_1 = driver.current_url
# print(now_url_1)
#
# time.sleep(1)
# # 获取结果数目
# user = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]').text
# print(user)
#
# time.sleep(2)
# driver.quit()

# 百度结果个数直接获取，csdn提取不到哈哈，先放一放

"""     通过代码可知，title用于获取当前页面的标题，current_url用于获得当前页面的url，
text用于获取搜索条目的文本信息。
    5.1.8 设置元素等待
    
    现在大多数的web应用程序使用的是Ajax技术，当一个页面被加载到浏览器时，该页面内的元素可以
在不同的时间点被加载，这使得定位元素变得困难，如果元素不在页面之中，会抛出
Elenment Not Visible Exception 异常，使用waits，可以解决这个问题，waits提供了一些操作之间的时
间间隔，主要是定位元素或针对该元素的任何其他操作。
    selenium webdriver提供两种类型的waits——显式和隐式等待，显式等待，显式等待会让webdriver等待
满足一定的条件以后再进一步执行，而隐式等待会让webdriver等待一段时间后再查找某元素。

    1.显式等待
    显式等待在代码中定义等待一定条件发生后再进一步执行代码，例如，用户需要在等待此网页加载完成后再
执行代码，否则会在达到最大时长时抛出超时异常，示例代码如下："""

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
#
# element = WebDriverWait(driver,5,0.5).until(
#     EC.presence_of_element_located((By.ID,"kw"))
#     )
# element.send_keys('selenium')
# driver.quit()

"""     WebDriverWait类是由WebDriver提供的等待方法，在设置时间内，默认每隔一段时间检测一次当
前页面元素是否存在，如果超过设置时间检测不到则抛出异常，具体格式如下：
# WebDriverWait(driver,timeout, poll_frequency=0.5, ignored_exceptions=None)

    参数说明如下：
    （1）driver：浏览器驱动
    （2）timeout：最长超时时间，默认以秒为单位
    （3）poll_frequency：检测的间隔（步长）时间，默认为0.5秒
    （4）ignored_exceptions：超时后的异常信息，默认情况下，抛出NoSuchElementException异常
    WebDriverWait()一般由until()或until_not()方法配合使用（到什么时候为止...）,下面是until
和until_not()方法的相关说明。*until(method，message=)调用该方法提供的驱动程序作为一个参数，
只到返回值为True，*until_not(method，message=)调用该方法提供的驱动程序作为一个参数，
只到返回值为False,在本例中，通过as关键字将expected_conditions重命名为EC，并调用
presence_of_element_located()方法判断元素是否存在。

    2.隐式等待
    WebDriver提供了implicitly_wait()方法来实现隐式等待，默认设置为0，它的用法相对来说要简单得多，
implicitly_wait()默认参数的单位为秒，本例中设置等待时长为10秒，首先，这是秒并非一个固定的等待时间，
它并不影响脚本的执行速度，其次，它并不针对页面上的某一元素进行等待，当脚本执行到某个元素定位时，
如果元素可以定位，则继续执行，如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到，
假设在第6秒定位到了元素则继续执行，若直到超出设置时长（10秒）还没有定位到元素，则抛出异常，
实例代码如下："""

# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from time import ctime
#
# driver = webdriver.Chrome()
# # 设置隐式等待时长为10秒
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
#
# try:
#     print(ctime())
#     driver.find_element_by_id("kw22").send_keys('selenium')
# except NoSuchElementException as e:
#     print(e)
# finally:
#     print(ctime())
#     driver.quit()

""" 5.1.9 多表单切换
    在web应用中经常会遇到frame/iframe表单嵌套页面的应用，webdriver只能在一个页面上对元素识别与定位，
对于frame/iframe表单内嵌页面上的元素无法直接定位，这时就需要通过switch_to.frame()方法将当前
定位的主体切换到frame/iframe表单的内嵌页面中，书本图5-6所示为网易126邮箱登录框的大概结构，想要
操作登录框必须要先切换到iframe表单。
    这时在selenium webdriver中就可以使用switch_to.frame()方法去切换，示例代码如下："""

# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
# driver.get("http://www.126.com")
# driver.switch_to.frame('x-URS-iframe')
# driver.find_element_by_name("email").clear()
# time.sleep(1)
# driver.find_element_by_name("email").send_keys(15738108997)
# driver.find_element_by_name("password").clear()
# time.sleep(0.5)
# driver.find_element_by_name("password").send_keys("15738108997zhan")
# time.sleep(0.5)
#
# driver.find_element_by_id("dologin").click()
# driver.switch_to.default_content()
#
# time.sleep(2)
# driver.quit()

# switch_to.frame()默认可以直接取表单的id或name属性，如果iframe没有可用的id和name属性，
# 则可以直接通过下面的方式进行定位

# 先通过xpath定位到iframe
# xf = driver.find_element_by_xpath('//*[@id="x-URS-iframe1619006457365.8337"]')
#
# # 再将定位对象传给switch_to.frame()方法
# driver.switch_to.frame(xf)
# driver.switch_to.parent_frame()
# 此外，在进入多级表单的情况下，还可以通过switch_to.default_content()跳回到最外层的页面。

"""5.1.10 下拉框选择
    有时我们会遇到下拉框，webdriver提供了select类来处理下拉框，如百度搜索设置的下拉框，如课本图
5-7所示
    在selenium中实现此功能的实例代码如下："""

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
#
# # 鼠标指针悬停至“设置”链接,自动化打开窗口没有设置，哈哈，那就换个更多吧
# driver.find_element_by_link_text('新闻').click()
# sleep(2)
#
# # 打开科技
# driver.find_elements_by_link_text('').click()
# sleep(2)

# 显示搜索结果条数
# sel = driver.find_element_by_xpath()
# Select(set).select_by_value('50') # 显示50条
#
# driver.quit()

"""5.1.11 调用JavaScript代码

    虽然webdriver提供了操作浏览器的前进和后退方法，但对于浏览器滚动条并没有提供相应的操作
方法，在这种情况下，就可以借助JavaScript来控制浏览器的滚动条，webdriver提供了excute_script()
方法来执行JavaScript代码。
    用于调整浏览器滚动条的JavaScript代码如下："""

# window.scrollTO(0,450);
# window.scrollTO()方法用于设置浏览器滚动条的水平和垂直位置，方法的第一个参数表示水平的左间距，
# 第二个参数表示垂直的上边距，实例代码如下：

# from selenium import webdriver
# from time import sleep
#
# # 访问csdn
# driver = webdriver.Chrome()
# driver.get("https://www.csdn.net")
#
# # 设置浏览器窗口大小
# driver.set_window_size(500,500)
#
# # 搜索
# driver.find_element_by_id("toolbar-search-input").send_keys('selenium')
# sleep(1)
# driver.find_element_by_id("toolbar-search-button").click()
# sleep(1)
#
# # 通过javaScript设置浏览器的窗口大小
# js = "window.scrollTo(100,450);"
# driver.execute_script(js)
# sleep(3)

"""     通过浏览器打开csdn进行搜索，并且提前通过set_window_size()方法将浏览器窗口
设置成固定宽高显示，目的是让窗口出现水平和垂直滚动条，然后通过execute_script()方法执行
javascript代码来移动滚动条的位置。

    5.1.12 窗口截图
    自动化用例是由程序去执行的，因此有时打印的错误信息并不十分明确，如果在脚本执行出错时，
能对当前窗口截图保存，那么通过图片就可以非常直观的看出出错的原因，webdriver提供了截图函数
get_screenshot_as_file()方法来截取当前窗口，示例代码如下："""

# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys('selenium')
# driver.find_element_by_id("su").click()
# sleep(2)
#
# # 截取当前窗口，并指定截图图片的保存位置
# driver.get_screenshot_as_file("D:\python_learn\爬虫阶段\爬虫A课阶段\从入门到精通\第5章，动态渲染页面抓取.jpg")
# driver.quit()

""" 脚本运行完成，在所在文件路径下就可以看到截取的图片了。
    
    5.1.13 无头模式
    在Linux系统中，一般都是一个命令行窗口，没有界面，所以使用selenium时，他肯定不会像在Windows
系统中一样弹出一个浏览器窗口，那么在Linux系统中要如何进行selenium程序的运行呢？
    这就要用到谷歌或火狐的无头浏览模式了，无头浏览，顾名思义，其实就是一个纯命令行的浏览器，
他没有界面，但所包含的功能与有界面的相差无几。
    使用无头浏览，只需要将前面的示例代码稍加改动，将多个实例化参数传进去，相关示例代码如下："""

# 谷歌驱动示例：

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# # chrome_options = Options()
# options.add_argument('--headless')
# # 使用谷歌驱动
# driver = webdriver.Chrome(options=options)
# # 打开url
# driver.get("https://www.baidu.com")

# 按照书本代码复现，发现报错：DeprecationWarning: use options instead of chrome_options
# driver = webdriver.Chrome(chrome_options=chrome_options)
# 所以我们按照提示，注释掉chrome_options = Options()、使用options = Options()，把对应的
# chrome_options.add_argument('--headless')的chrome_去掉，即可运行成功。

#   可以看到，在实例化时，只是多加了一个无头参数“--headless”便可以实现无头浏览，这时运行代码，
# 就会发现不在弹出浏览器窗体，其他的都没变，一样的可以打开指定url定位指定元素等。

"""5.2.1 Splash 的基本使用
    前面学习了selenium，知道selenium可以抓取动态渲染页面、操作浏览器等，下面来介绍另外
一款工具Splash，splash是一个Javascript中的Twisted和QT库，利用它可以实现动态渲染页面的抓取。

    5.2.1 Splash的功能介绍
    利用Splash，用户可以实现如下功能：
    （1）异步方式处理多个网页渲染过程。
    （2）获取渲染后的页面的源代码或截图。
    （3）通过关闭图片渲染或使用Adblock规则来加快页面渲染速度。
    （4）执行特定的JavaScript脚本。
    （5）可通过Lua脚本来控制页面渲染过程。
    （6）获取渲染的详情过程并通过HAR（HTTP Archive）格式呈现。
    
    5.2.2 Docker 的安装
    Splash的安装分为两部分，一部分时Splash服务的安装，具体是通过Docker，安装之后，会启动一个
Splash服务，可以通过他的接口来实现JavaScript页面的加载，另一部分是scrapy-splash将会在后面的
第10章中讲到。
    在安装之前，需要先安装Docker，Docker的相关安装步骤如下：
    步骤1：从Docker官网上下载Windows下的docker进行安装，需要注意的是，系统要求是
Windows 10 64位pro及以上版本或教育版。
    官网下载地址为：https://store.docker.com/editions/community/docker-ce-desktop-windows,
如书本5-8所示。
    安装包下载完成后右击，以管理员身份运行。
    步骤2：进行安装，选项保持默认，安装成功后开始菜单会出现对应图标
    步骤3：单击Docker Quickstart Terminal 图标启动Docker Toolbox终端，如书本图5-11，如果系统显示
User Account Control 窗口来运行VirtualBox修改用户的计算机，选则Yes，在“$”符号处可以输入以下
命令来执行：
$ docker run hello-world
Unable to find image 'hello-world:latest'locally
Pulling repository hello-world
以下命令省略。。。

    对于win10来说，现在Docker有专门的Windows10专业版系统的安装包，但是需要开启Hyper-V的方法如下：
（1）右击开始菜单，选则应用和功能，单击程序和功能，单击启动或关闭Windows功能，选中复选框中的Hyper-V
，即可开启Hyper-V，最新版的Toolbox的下载地址为：https://www.docker.com/get-docker

    5.2.3 Splash的安装
    Docker安装完成后，启动Docker，并运行Docker启动splash命令，初次使用将安装Splash，例如，
这里使用一台云服务器Ubuntu，进入Docker输入以下命令：
sudo docker run -p 8050:8050 scrpinghub/splash
    输入命令后，此时需要等待一段时间，它会自动安装并启动，安装完成后会启动课本5-19所示内容，
表示容器已经启动并监听了8050端口。
    由于这里使用的是云服务器，因此需要打开防火墙端口允许8050端口远程访问，打开防火墙之后，
在浏览器输入ip:8050，将会出现Splash的启动页面，如书本图5-20所示，即可安装完成

    以上关于docker的使用我们暂时不采用
    5.3 新手实训 
    本章的基础知识讲解已经告一段落，接下来结合本章所学知识做一个实训练习，主要是为了使读者
加深对selenium基本使用的理解，达到举一反三的效果。

1.模拟登录csdn博客
    前面已经学习了关于selenium的一些基础知识，下面通过一个实训练习来加深巩固一下，使用
selenium模拟登录csdn博客。
    步骤详解不再赘述，我们直接利用知识进入登录："""

# import time
# from selenium import webdriver
#
# # 使用谷歌驱动
# driver = webdriver.Chrome()
# # 打开cdsn
# driver.get("https://www.csdn.net")
# # 由于有可能存在网络加载慢等原因，我们这里先暂停5秒，（可根据实际情况调整）再去获取表单元素
# time.sleep(1)
# # 下面开始定位以及点击、输入等登录准备操作
#
# # 定位点击登录/注册：
# driver.find_element_by_xpath('//*[@id="csdn-toolbar"]/div/div/div[3]/div/div[1]/a').click()
# # 这里我们通过xpath定位并成功点击到了登陆注册按钮，下面即是点击账号密码登录
# time.sleep(2)
# # 定位账号密码登录：
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[5]/ul/li[2]/a').click()
# # 这里我们再次通过xpath定位并成功点击到了账号密码登录，下面即是账号密码输入框的定位点击：
# time.sleep(2)
# # 定位账号输入框并输入账号：
# driver.find_element_by_id("all").click()
# driver.find_element_by_id("all").send_keys(15738108997)
#
# # 这里我们通过测试，使用id定位成功定位并点击输入了账号，下面操作密码：
# time.sleep(1)
# driver.find_element_by_id("password-number").click()
# time.sleep(1)
# driver.find_element_by_id("password-number").send_keys('15738108997zhan.')
# # 安全起见，我们输入了错误的密码
#
# # 我们上述操作已经完成了账号密码的输入，下面就是定位点击登陆按钮了：
# time.sleep(2)
# # 获取登录按钮，模拟表单提交：
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[5]/div/div[6]/div/button').click()
# # 通过定位测试，我们成功使用xpath定位点击到了登录按钮，至此，我们完成了此次模拟登录。

"""    2.selenium模拟百度搜索
    接下来再看一个实例，通过模拟在百度首页搜索框中输入“Python”然后单击按钮提交，获取搜索结果，太简单，直接省略吧
    
5.4 新手问答
    
1.学习完本章之后,读者可能会有以下疑问。
1. Selenium 的可以爬取所有的网站吗?

答: 使用Selenium模拟浏览器进行数据抓取无疑是当下最通用的数据采集方法,它“通吃各种数据加载方式,能够绕过客户JS加密,绕过爬虫检测,绕过签名机制。
它的应用,使得许多网站的反采集策略形同虚设。由于Selenium不会在HTTP请求数据中留下指纹,因此无法被网站直接识别和拦截。
这是不是就意味着Selenium真的就无法被网站屏蔽了呢?非也。Selenium在运行时会暴露出Python网结爬虫开发从入门到精通
一些预定义的JavaScript变量(特征字符串) ,如"window.navigator.webdriver" ,在非Seleniun环境下其值为undefined, 而在Selenim环境下,其值为True,
所以有些网站上的反爬会根据这个来进行判断屏蔽。

2.测试用例再执行单击元素时失败,导致整个测试用例失败。如何提高单击元素的成功率?

答: Selenim是在单击元素时是通过元素定位的方式找到元素的,要提高单击的成功率,必须保证找到元素的定位方式准确。
但是在自动化工程的实施过程中,高质量的自动化测试不是只有测试人员保证的。需要开发人员规范开发习惯,如给页面元素加上唯一的name、id等,
这样就能大大地提高元素定位的准确性。当然,如果开发人员开发不规范,那么在定位元素时尽量使用相对地址定位这样能减少元素定位受页面变化的影响。
只要元素定位准确,就能保证每一个操作符合预期。

3.脚本太多,执行效率太低,如何提高测试用例执行效率?

答: Selenim脚本的执行速度受多方面因素的影响,如网速、操作步骤的烦琐程度、页面的加载速度,以及在脚本中设置的等待时间、
运行脚本的线程数等。所以不能单方面追求运行速度,要确保稳定性,能稳定地实现回归测试才是关键。

可以从以下几个方面来提高速度:

(1)减少操作步骤。如果经过三四步才能打开要测试的页面,那么就可以直接通过网址来打开,减少不必要的操作。
(2)中断页面加载。如果页面加载的内容过多,可以查看一下加载慢的原因,如果加载的内容不影响测试,就设置超时时间,中断页面加载。
(3)在设置等待时间时,可以sleep固定的时间,也可以检测某个元素出现后中断等待,这两种方法都能提高速度。
(4)配置resING实现多线程。在编写测试用例时,一定要实现松耦合(减少耦合,增加可扩展性),然后在服务器允许的情况下,尽量设置多线程运行,提高执行速度。

    本章小结：
    本章主要讲解了Selenium自动化工具的基本使用方法,通过它在写爬虫时,可以实现模拟动览器的各种操作,如模拟单击、登录、拖动窗口等。
所涉及的“坑”比较多的就是环境的搭建,特别是Selenium的环境搭建,对版本要求特别严格,所以希望读者在实际练习过程中要多注意。关于Selenium的更多用法,
有兴趣的读者可以查阅Selenium-Python中文文档: htps//senimpython-zhreadthedocs.io/en/latest"""










