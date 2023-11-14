# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""本章主要涉及的知识点
1.Ajax的基本原理及方法
2.分析抓取目标网站的Ajax接口
3.使用python网络请求库请求分析到的Ajax接口获取数据"""


"""Ajax简介：
Ajax的全称为Asynchronous JavaScript and XML(异步的 JavaScript 和 XML),他不是新的编程语言，
而是一种使用现有标准的新方法，他可以在不重新加载整个页面的情况下与服务器交换数据并更新部分网页
的数据。
在W3School.com.cn/tiy/t.asp?f=ajax_get去体验一下"""

"""实例引入
   下面通过一个实例来了解Ajax请求，这里以飞常准大数据网页为例，在浏览器中打开链接
在界面右上方的条件筛选输入框中输入“PEK”,然后单击搜索按钮，得到查询结果后仔细观察前后的页面，
特别是url地址栏，可以发现url前后没有任何变化，但下面的列表中的数据却不一样了，这其实就是Ajax
的效果，在不刷新全部页面的情况下，通过Ajax异步加载数据，实现数据局部更新。"""

"""4.1.2 Ajax的基本原理
初步了解了Ajax之后，下面再来详细了解它的基本原理，发送Ajax请求到网页更新的过程可以简单的
分为以下3个步骤：
（1）发送请求
（2）解析返回数据
（3）渲染网页
在具体讲解这3个步骤之前，可以先看一下它的抽象过程图：图在书本上，懒得搬运了哈哈

1.发送请求
我们知道，JavaScript可以实现页面的各种交互功能，Ajax也不例外，它的底层也是由JavaScript实现的，
要使用Ajax技术，需要创建一个XMLHttpRequest对象，缺少它就不能实现异步传输，所以执行Ajax时，实际上
需要执行以下代码："""

# var xmlhttp;
# if (window.XMLHttpReauest){
# //IE7+,Firefox,Chrome,Opera,Safari # 浏览器执行代码
# xmlhttp=new XMLHttpRequest();
# }else{
# //IE6,IE5 # 浏览器执行代码
# xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
# }
# xmlhttp.open("GET","/try/ajax/demo_get2.php?fname=Henry&lname=Ford",true);
# xmlhttp.send();
#
# xmlhttp.open("POST","/try/ajax/demo_post2.php",true);
# xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlen coded");
# xmlhttp.send("fname=Henry&lname=Ford");

"""在网页中为某些事件的响应绑定异步操作：通过上面创建的xmlhttp对象传输请求、携带数据。
在发出请求前要先定义请求对象的method（方法）、要提交给服务器中哪个文件进行请求的处理、要携带
哪些数据，以及判断是否异步
    其中，与普通的Request提交数据一样，这里也分两种方式：GET和POST，在实际使用时可根据需求自主选择
，GET和POST都是向服务器提交数据据，并且都会从服务器获取数据，他们之间的区别如下：
    （1）传送方式：GET通过地址栏传输，POST通过报文传输
    （2）传送长度：GET有长度限制（受限于url长度），而POST无限制
    对于GET方式的请求，浏览器会把HTTP header和data一并发送出去，服务器响应200（返回数据）；
而对于POOST，浏览器先发送header，服务器响应100 continue，浏览器再发送data，服务器响应200 OK
（返回数据），也就是说，GET只跑一趟就把货送到了，而POST得跑两趟，第一趟，先去和服务器打个招呼
“嗨，我等下要送一批货来，你们打开门迎接我”，然后再回头把货送过去，因为POST需要两步，时间上消耗
的要多一点，看起来GET比POST更有效，因此推荐用GET替换POST来优化网站性能。

2.解析请求
    服务器在收到请求后，就会把附带的参数数据作为输入传给处理请求的文件，例如，前面代码中所示：
把fname=Henry&lname=Ford作为输入，传给“/try/ajax/demo_get.php”文件，然后该文件根据传
入的数据做出处理，最终返回结果，并通过response对象发回去，客户端根据xmlhttp对象来获取response
的内容，返回的response内容可能是html也可能是json，接下来只需要在方法中用JavaScript做进一步
的处理即可，例如，当为json时可以进行解析和转化。
    例如，这里使用谷歌浏览器打开网址https://data.variflight.com/analytics/CodeQuery,按F12
打开调试模式，然后在页面的搜索框中输入“PEK”并单击搜索按钮，之后在调试面板中切换到network，找到名为
aiportCode的请求并单击即可以查看Ajax发起请求之后返回的json数据

3.渲染网页
    JavaScript有改变网页内容的能力，所以通过Ajax请求获取到返回数据后，通过解析就可以调用JavaScript
获取指定的网页DOM对象进行更新、修改等数据处理了，例如，通过document.getElementById().innerHTML
操作，便可以对某个元素内的元素进行修改，这样网页显示的内容就改变了，这样的操作也被称为DOM操作，
即对Document网页文档进行操作，如修改、删除等。
    例如，通过document。getElementById("intro")可以将ID为intro的节点内容的HTML代码改为服务器返回的内容，
这样intro元素内部便会呈现出服务器返回的新数据，网页的部分内容看上去就更新了，假使服务器返回了“11”
这个数据，如课本p88所示，通过观察可以发现，上述3个步骤其实都是JavaScript完成的，即JavaScript完成了
整个请求、解析和渲染过程，现在再回过头去想一下，前面的例子中的飞常准大数据网页，其实就是JavaScript
向服务器发送了一个Ajax请求，然后获取新的数据解析，并将其渲染在网页中。
"""

"""4.1.3 Ajax方法分析"""

"""
    这里仍以飞常准大数据（https://data.variflight.com/analytics/CodeQuery）网页为例，我们都知道
在条件筛选框中输入机场三字码时刷新内容由Ajax加载，而且页面的url没有变化，那么应该到哪里去查看这些Ajax
请求呢？
    这里还需要借助浏览器的开发者工具，下面以chrome浏览器为例来介绍。
    步骤1：用chrome浏览器打开网址https://data.variflight.com/analytics/CodeQuery。
    步骤2：在页面中右击，在弹出的快捷菜单中选择检查选项或按F12键，此时会弹出开发者工具，
在elements选项卡中会显示网页的源代码，其下方是节点的样式，不过这不是我们想要寻找的内容。
    步骤3：切换到network选项卡，重新刷新当前页面，可以发现这里出现了非常多的条目，其实这些条目
就是页面在加载过程中浏览器与服务器之间发送请求和接收响应的所有记录。
Ajax有其特殊的请求类型，它叫做xhr，小黄人哈哈，在这些条目中我们可以找到名为“airportCode”的请求
，其Type为xhr，这就是一个名副其实的Ajax请求，单击这个请求就可以看到它的详细信息。
    步骤4：单击airportCode请求，会看到右侧有他的一些详细信息，，选择preview或response选项卡就会看到
当前Ajax请求向服务器端发起请求后服务端响应的内容了，得到这些内容后，JS就可以解析处理，将它更新到网页中，
至于其他的4个选项卡介绍请参考第2章中HTTP部分所讲的内容，这里不再作单独的讲解。

温馨提示：
    在进行请求分析时，若发现条目太多，不方便直接找出xhr方法时，这里教大家一个小技巧，单击
Type选项就可以快速地对请求进行筛选分类，这时再按分类去查找xhr就快速多了。"""

"""4.2 使用Python模拟Ajax请求数据"""

"""
    通过前面的学习，认识和了解了Ajax的基本原理，下面用Python来模拟这些Ajax请求，这里仍以前面的飞常准
大数据网页为例，通过传入条件查询的参数北京首都机场三字码PEK来请求获取它的数据，把北京首都机场
的信息提取出来。

    4.2.1 分析请求
    下面分析一下请求，使用浏览器打开网址https://data.variflight.com/analytics/CodeQuery之后，
相关的步骤如下：
    步骤1：按F12进入开发者工具，选择network选项卡，在条件搜索框中输入“PEK”并单击搜索按钮，
可以看到network选项卡中出现了很多条目。
    步骤2：然后单击Type进行筛选，找到名称为airportCode的请求并单击。
    步骤3：单击之后，可以看到response下面很多关于请求的详细信息，通过观察发现，请求链接
request url为“https://data.variflight.com/analytics/Codeapi/aiportCode”，请求方法
request method为“POST”，继续拖动滚动条到最下方From Data处，可以看到这里有两个参数：
key和page，key就是输入PEK要查询的三字码，page是页数。

    4.2.2 分析响应结果
    前面已经分析了请求的详细信息，如请求的链接、方法、需要传递的参数等，下面再来看看
它的响应结果是什么样的，选则Preview选项卡，将会出现书本p92页4-12的内容，这些内容时json格式，
浏览器开发工具自动做了解析方便查看，可以看到有3个信息，一是code，代表响应状态码是成功还是失败，
二是data，data就是我们想要的内容，里面包含了北京机场的相关信息，三是message，提示消息。

    4.2.3 编写代码模拟抓取
    下面使用Python的request库编写代码来模拟抓取，首先定义一个方法获取每次请求的结果，在请求时，
key和page是一个可变的参数，所以我们将它们作为方法的参数传递过来，相关示例代码如下："""

# 导包
# import requests
# import json
#
# # 获取请求参数
# def get_data(key,page):
#     # 准备起始的url地址：
#     url = "https://data.variflight.com/analytics/Codeapi/aiportCode"
#     # 传参:
#     data = {
#         "key":key,
#         "page":page
#     }
#     # 接收响应
#     res = requests.request("post", url, data=data)
#     return res.text
# # 获取解析结果
# def get_parse(data): # 定义解析函数
#     return json.loads(data) # 返回的是json数据，使用json.loads转化为字典
# # 接收获取的内容
# data = get_data("PEK",0)
# # 获取解析的data内容
# apt_info = get_parse()
# # 输出获取的data
# print(apt_info["data"])

""" 这里定义了一个get_data的方法来表示获取请求数据，通过传入的key三字码和页数page作为参数，
从前面使用浏览器开发工具分析请求详细信息得知，要抓取的请求链接request url为“https://data.
variflight.com/analytics/Codeapi/aiportCode”，方法为POST，需要传递的参数时key和page，
然后返回请求响应结果，接着又定义了get_parse方法，这个方法是用来解析结果的，通过传入请求获
取到的数据，解析并返回，由前面的分析可知，它返回的是json字符串格式的数据，因此需要使用
json.loads方法去解析并返回，最终得到的结果如书本p93的4-13所示，此时网站升级中...enm....

    通过上述方法成功得到了关于北京首都机场的相关信息，另外，还可以增加一个方法，用于将
数据保存到数据库中或excel中等，关于保存数据的方法，将会在后面的章节中讲到，这里不做讲解。
"""

"""4.3 新手实训
    关于Ajax的内容基本介绍完毕，学习它的基本原理和分析方法后，下面结合所学知识做几个实战练习。

1.分析猎聘网的xhr请求并编写代码模拟抓取数据
    下面以在猎聘网上抓取与python相关的招聘信息为例，相关步骤如下：
    步骤：用浏览器打开猎聘网首页“http://www.liepin.com”,然后抓包，找到名为“soejob4landingpage.json”
的请求并点击，观察headers，编写代码，示例如下："""


# import requests
#
# url = "https://dataopen.liepin.com/basic/p/v2/getAllDq.json?traceId=65054209984"
# headers = {
#     'Cookie': '__uuid=1618650116414.39; __tlog=1618650116426.16%7C00000000%7C00000000%7C00000000%7C00000000; __s_bid=bef44e74d0bd5b328aece6a7b7217b024155; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1618650117; acw_tc=276082a616186501358706966ee8cd771e7bb2154680a64186c28617008748; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1618650517; __session_seq=6; __uv_seq=6',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
# }
# data = {
#     "key":"python",
#     "traceld":"65054209984"
# }
# res = requests.post(url, json=data)
# print(res.json())

"""2. 分析南方航空官网的机票查询xhr请求抓取数据

    有了实训1的练习经验以后，接着再来看一个网页，通过对他的分析和观察，进一步加深对Ajax请求接口
的理解，由于分析步骤与实训1类似，这里不再重复讲解，下面给出相关示例代码：
相关示例代码如下：
"""

# import requests
#
# url = "https://b2c.csair.com/portal/minPrice/queryMinPriceInAirLines?jsoncallback=getMinPrice&inter=N&callback=getMinPrice&_=1618743110976"
# data = {"depCity": "SZX", "arrCity": "PVG", "date": "20210424", "adultFuelTax": "0", "childFuelTax": "0",
#         "adultFuelTax": "0",
#         "arrCity": "PVG",
#         "childFuelTax": "0",
#         "date": "20210424"
#         }
# res = requests.post(url, json=data)
# print(res)

"""新手问答：
    1.太简单，省略吧哈哈
    2.Ajax接收到的数据类型是什么？
    答：后台返回的数据主要有三种类型:string、json串和json对象，接收到了这三种数据，
可以通过json对象直接循环使用、json串转json使用和string直接使用，具体方法可根据实际得到的数据来选择

    本章小结：
    本章主要介绍了Ajax的基本工作原理，并通过实例，使用python模拟Ajax请求，并成功抓取到了数据，
    本章中的内容需要熟练掌握，在后面的实战中会用到很多次这样的分析和抓取。
    """












