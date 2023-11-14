# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
第6章，代理的设置与使用

    在做爬虫的过程中经常会遇到这种情况:本来写的爬虫脚本一直在好好地运行,正常地抓取数据,
但就在一盏茶的工夫错误“从天而降” ,重启脚本也不行,如出错403 Forbidden。这时网页上可能会出现
“你的IP访问频率过高”这样的提示,或者是跳出一个验证码输入框让输入验证码验证之后才能继续访问该网页,
但一会又反复出现这种情况。
出现这种现象的原因是网站采取了一些反爬策略,如限制IP访问频率,如果在单位时间内某个IP请求以较快
的速度请求,并超过了预先设置的阈值,那么服务器就会拒绝服务,返回一些错误信息或验证措施。这种情况
可以称为封IP,这样一来爬虫就自然而然会报错抓取不到信息了。
试想一下,既然服务器检测的是某个IP单位时间的请求次数,那么借助某种方法伪装IP,让服务器无法识别请求
的真实IP,这样不就可以实现突破封IP的限制继续抓取数据了吗?
所以,这时代理IP就派上用场了。本章将会详细介绍代理的基本知识,包括设置代理、代理池构建、付费代理
的使用、ADSL拨号代理的搭建等,以帮助爬虫脱离封IP的“苦海”。
"""
"""
本章主要涉及的知识点
·代理的设置
.在爬虫中应用代理
·代理池的维护
"""

"""
    6.1 代理设置
    前面的章节中介绍了很多的请求库，如urllib、requests、selenium等，接下来将通过一些实际案例
来了解如何设置他们的代理，为后面了解代理池、ADSL拨号代理的使用打下基础。

    6.1.1 urllib 代理设置
    下面以最基础的urllib为例，来看一下代理的设置方法，假使通过某种途径获取到两个代理IP，
通过请求http://myip.kkcha.com这个网站来测试，实例代码如下：
"""

# import urllib.request
#
# url = "http://myip.kkcha.com"
# # ip地址：端口号
# proxies = {
#     'http':'http://114.104.185.82',
#     'https':'https://163.125.223.14:8118'
# }
#
# proxy_support = urllib.request.ProxyHandler(proxies)
# opener = urllib.request.build_opener(proxy_support)
# urllib.request.build_opener(opener)
# response = urllib.request.urlopen(url)

"""
    这里可以看到,需要借助ProxyHandler方法设置代理,参数是字典类型,键名是协议类型,键值是代理,
此处代理前面需要加上协议,即http或https,当请求的链接是http协议时, ProxHandler会调用http代理,
当请求的链接是https协议时, ProxyHandler会调用https,此处生效的代理是171.214.214.185:8118。

    创建完ProxyHandler对象之后,继续利用build opener0方法传入该对象来创建Opener,这样就相当于
此Opener已经设置好代理了。接下来直接调用urllib.requesturlope()方法,即可访问需要的链接。
通过运行如图6-1所示的代码,可以看到,在返回的HTML中, IP已经发生了改变,变成了所设置的代理IP。


    6.1.2 requests 代理设置
    与urllib代理设置方法相比，在requests中设置代理就更简单了，实例代码如下："""

# import requests
#
# url = "http://myip.kkcha.com"
# # IP地址：端口号
# proxies = {'http':'171.214.214.185:8118'}
# response = requests.get(url=url,proxies=proxies)
# print(response.text)

"""     直接在requests.get()方法中添加一个proxies参数就完成了设置，运行代码得到的结果与urllib
方法相同，如书本p135_6-1所示。


    6.1.3 selenium 代理设置
    对于如何在selenium中设置代理，这里以谷歌webdriver为例，相关示例代码如下："""

# from selenium import webdriver
#
# chromeOptions = webdriver.ChromeOptions()
#
# # 设置代理
# chromeOptions.add_argument("--proxy-server=http://http://114.104.185.82")
# browser = webdriver.Chrome(chrome_options=chromeOptions)
# # 查看本机IP，查看代理是否起作用
# browser.get("http://myip.kkcha.com")
# print(browser.page_source)
# # 退出，清除浏览器缓存
# browser.quit()

""" 如代码中所示，通过webdriver.ChromeOptions()创建一个参数对象，再通过add_argument()
方法添加参数--proxy-server,这里需要注意的是，”==“两边不能有空格，如设置为 ”--proxy-server=
 http://114.104.185.82“则会报错，运行结果如图p135，6-1所示。
 
    如果能多个IP随机切换，那么爬虫的强壮程度会更高，下面将简单介绍随机切换IP，它是通用的，
不限于urllib、requests或selenium，示例代码如下："""

# import random
# # 我们从IP代理网站上得到的IP，用IP地址：端口号存入iplist数组
# iplist = ['xxx.xxx.xxx.xxx:xxxx','xxx.xxx.xxx.xxx:xxxx']
# proxies = {'http':random.choice(iplist)}

# 将n个代理放在一个list列表中，然后每次请求时，随即从list中取出一个代理使用，使爬虫更加健壮。

""" 6.2 代理池构建
    所谓代理池，就是由n个代理IP组成的一个集合，做网络爬虫时，一般对代理IP的需求量比较大，
这是因为在爬取网站信息的过程中，很多网站做了反爬策略，可能会对每个IP做频次控制，因此在爬
取网站时就需要很多代理IP，形成一个可用代理池，形成一个可用的IP代理池,每次在请求时,从代理
池中取出一个代理使用。
    那么构建这个代理池的IP从哪来呢?用户可以选择直接从网上购买一些代理IP,它们稳定且价格也不贵,
也可以选择从网上获取免费的代理IP,例如,这里在百度上搜索后,以其中一个网站http://wwwxicidalico/
为例,如图6-3所示。

    可以看到,此网站提供了丰富的免费代理P,可以从这个网站上抓取一些代理P来使用,它的网址结构
是http://wwwxicidaili.com/nn'+PageNumber,每页有50个代理IP，可以很方便地用for循环来爬取
所有代理P。查看网页源码,发现所有的IP和端口都在<-tr class->下第二个和第三个td类下,
结合BeautifulSoup可以很方便地抓取信息,
下而来看看如何抓取IP构建代理池。

    6.2.1 获取IP：
    在分析了http://www.xicidaili.com/nn代理网站的网页结构后，下面将通过Python的requests
来抓取它，并提取出来，实例代码如下："""

# import requests
# from bs4 import BeautifulSoup
#
# def get_ips(num):
#     url = "http://www.xicidaili.com/nn{}".format(str(num))
#     header = {
#         "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
#
#     }
#     res = requests.get(url,headers=header)
#     bs = BeautifulSoup(res.text,'html.parser')
#     res_list = bs.find_all("tr")
#     ip_list = []
#     for x in res_list:
#         tds = x.find_all("td")
#         if tds:
#             ip_list.append({"ip":tds[1].text,"port":tds[2].text})
#     return ip_list
# # 获取第一页的IP，这个可以自己随便填
# ip_list = get_ips(1)
# # 循环打印看一下所获取的IP
# for item in ip_list:
#     print(item)

# 抓取到第一页的IP和端口，下一步就是验证代理是否可用。

"""     6.2.2验证代理是否可用
    前面已经通过代码得到第一页的免费代理,当然了,免费也有免费的弊端,那就是并不是所有的代理IP
都可以用,所以就需要检查一下哪些 是可以使用的。要分辨该IP是否可用,主要通过检查连上代理后能不能
在2秒内打开页面,如果可以,则认为IP可用,将其添加到一个list中供后面使用,反之如果出现异常,则认为
IP不可用,实现代码如下"""

# import requests
#
# from bs4 import BeautifulSoup
# import socket
#
# # 获取代理
# def get_ips(num):
#     url = "http://www.xicidaili.com/nn{}".format(str(num))
#     header = {
#         "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
#
#     }
#     res = requests.get(url, headers=header)
#     bs = BeautifulSoup(res.text, 'html.parser')
#     res_list = bs.find_all("tr")
#     ip_list = []
#     for x in res_list:
#         tds = x.find_all("td")
#         if tds:
#             ip_list.append({"ip": tds[1].text, "port": tds[2].text})
#     return ip_list
#
# # 验证代理是否可用
# def ip_pool():
#     socket.setdefaulttimeout(2)
#     ip_list = get_ips(1)
#     ip_pool_list = []
#     for x in ip_list:
#         proxy = x['ip']+":"+x["port"]
#         proxies = {'http:proxy'}
#         try:
#             res = requests.get("http://www.baidu.com",proxies=proxies)
#             ip_pool_list.append(proxy)
#         except Exception as ex:
#             continue
#         return ip_pool_list
#     ip_pool()

# 这样就取得了一系列可用的代理IP，配合之前的爬虫使用，就可以解决IP被封的问题了，但由于验证IP
# 所需要的时间很长，所以可以采用多线程或多进程的方法进一步提高效率。

"""     6.2.3 使用代理池
    当通过爬取和验证得到一批可用的IP组成了一个代理池后，就可以在爬虫中使用它了，操作方法很简单
，每次只需要从代理池中随机取一个代理IP使用就可以了，示例代码如下："""

# import random
# # 把从IP代理网站上拿到的可用IP列表，随机取出一个给爬虫使用
# iplist = ip_pool()
# proxies = {'http':random.choice(iplist)}
# url = "http://myip.kkcha.com"
# response = requests.get(url=url,proxies=proxies)
# print(response.text)

"""     温馨提示：
    在实际项目中可能会获得到大量的代理IP，建议将通过验证可用的IP代理存储到数据库中，如Redis
或其他数据库，这样每次在使用时，就可以到数据库中去取，这样做的好处是易于维护和方便代理池的IP供
其他的爬虫取用。

    6.3 付费代理的使用
    相对于免费代理来说，付费代理稳定性会更高一些，付费代理分为两类：一是提供接口获取海量代理，
按天或按量收费，如讯代理，另一类搭建了代理隧道，直接设置固定域名代理，如阿布云代理。
    本节分别以两家具有代表性的代理网站为例，讲解这两类代理的使用方法。

    6.3.1 讯代理的使用
    讯代理的代理效率在各个平台中相对较高，其官网为：http://www.xdaili.cn,如书本p140，6-5所示。
    
    
    在讯代理官网上可供选购的代理有多种类别,包括如下几种:(参考官网介绍)。
(1)优质代理:适合对代理IP需求量非常大,但能接受较短代理有效时长(10-30分钟)的小部分不稳定的客户。
(2)独享代理:适合对代理IP稳定性要求非常高且可以自主控制的客户,支持地区筛选。
(3)混拨代理:适合对代理IP需求量大,代理IP使用时效短(3分钟)、切换快的客户。
(4)长效代理:适合对代理IP需求量大,代理IP使用时效长(大于12小时)的客户。
一般来说,用户选择优质代理即可满足需求。但这种代理的量比较大,稳定性不高,一些代理不可用。
所以这种代理的使用就需要借助6.2.3小节所介绍的代理池,自己再做一次筛选,以确保代理可用。
    读者可以购买一天时长来试试效果。购买之后,讯代理会提供一个API来提取代理,如图6-6所示

    例如，这里提取API为http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderIp=
ace5b9824e1f.......省略，（可能已经过期，再次仅仅做演示）
    在这里指定了提取数量为0，提取格式为JSON，直接访问链接即可提取代理，如书本p141图6-7所示；,
    接下来要做的就是解析JSON，然后将其放入代理池中，跟据API获取代理的代码如下：
运行结果如下，如书本6-8所示："""

# import requests
#
# res = requests.get("http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?"
#                    "spiderIp=..以下部分省略")
# ip_list = res.json()["RESULT"]
# print(ip_list)

"""  温馨提示：如果信赖讯代理，可以不做代理池筛选，直接使用代理，但一般来说，推荐使用代理池
筛选，可以提高代理利用率。

    6.3.2 阿布云代理的使用
    阿布云代理提供了代理隧道，代理速度快且非常稳定，其官网为：https://www.abuyun.com,
如书本6-9所示，
    阿布云代理主要分为两种：专业版和动态版，另外，还有经典版：（参考官网介绍）
    
(1)动态版:每个请求锁定一个随机IP、海量I资源池需求、近300个区域全覆盖、IP切装迅、使用灵活,适用于爬虫类业务。
(2)专业版:多个请求锁定一个IP、海量IP资源池需求、近300个区域全覆盖、IP可连续使用1分钟,适用于请求IP连续型业务。
(3)丝真版:多个请求锁定一个IP、海量IP资源池需求、近300个区域全覆盖、IP可连续使用15分钟,适用于请求IP连续型业务。
    关于专业版和动态版的更多介绍可以查看官网https:/www.abyun.com/http-proxy/dyn-intro.html
对于爬虫来说,推荐使用动态版,购买之后可以在后台看到代理隧道的用户名和密码,如书本p143，图6-10所示

    整个代理的连接域名为proxy.abuyun.com,端口为9020,它们均是固定的,但是每次使用之后IP都会更改,该过程其实就是利用代理隧道实现的(参考官网介绍)。
(1)云代理通过代理隧道的形式提供高匿名代理服务,支持HTTP/HTTPS
(2)云代理在云端维护一个全局P池供代理隧道使用,池中的IP会不间断更新,以保证同一时刻IP池中有几十到几百个可用代理IP。
(3)代理IP池中部分I可能会在当天重复出现多次。
(4)动态版HTTP代理隧道会为每个请求从IP池中挑选一个随机代理IP。
(5)无须切换代理IP,每一个请求分配一个随机代理IP。
(6) HT理路道有并发请求限制,默认每秒只允许5个请求。如果需要更多请求数，需额外购买。
使用教据的官网地址为https:/www.abyun.com/http-proxy/dyn-manual-python.html。
"""

# 这里以request为例，接入代码如下：

# import requests
#
# url = 'http://httpbin.org/get'
#
# # 代理服务器
# proxy_host = 'proxy.abuyun.com'
# proxy_port = '9020'
#
# # 代理隧道验证信息
#
# proxy_user = 'H306219X51T4OW8D'
# proxy_pass = 'DA48BAABD708EF10'
# proxy_meta = 'http://%(user)s:%(pass)s@%(host)s:%(port)s'%{
#     'host':proxy_host,
#     'port':proxy_port,
#     'user':proxy_user,
#     'pass':proxy_pass
# }
#
# proxies = {
#     'http':proxy_meta,
#     'https':proxy_meta,
# }
# response = requests.get(url,proxies=proxies)
# print(response.text)

"""
    输出结果的origin即为代理IP的实际地址。这段代码如果多次运行测试,就能发现每次请求origin都会
产生变化,这就是动态版代理的效果。
这种效果其实与之前的代理池的随机代理效果类似,都是随机取出一个当前可用代理。但是,与维护代理池
相比,此服务的配置简单,使用更加方便,更省时省力。在价格可以接受的情况下,用户也可选择此种代理。
以上便是付费代理的相关使用方法,付费代理的稳定性比免费代理更高,用户可以自行选购合适的代理。
"""

"""
    6.4 ADSL代理的搭建
化理池可以挑选出许多可用代理,但是稳定性不高、响应速度慢,而且这些代理通常是公共代黑,可能许多
人在同时使用,其I被封的概率很大。另外,这些代理可能有效时间比较短,虽然代理池一直在筛选,但如果
没有及时更新状态,也有可能获取到不可用的代理。
如果要追求更加稳定的代理,就需要购买专有代理或自己搭建代理服务器。但是服务器一般都是固定的IP,
搭建100个代理就需要100台服务器,这对于一般用户来说是难以实现的。
所以, ADSL动态拨号主机就派上用场了。下面来了解一下ADSL拨号代理服务器的相关设置。

    6.4.1 ADSL简介
    ADSL的全称为Asymmetric Digital Subscriber Line,中文意思为非对称数字用户环路,即它的上行
和下行带宽不对称。它采用颜分复用技术把普通的电话线分成了电话、上行和下行3个相对独文的信道,从而
避免了相互之间的干扰。
这种主机称为动态拨号VPS主机,也就是ADSL.号,在连接上网时是需要拨号的,只有拨号成功后才可以上网,
每拨一次号,主机就会获取一个新的IP,也就是说,它的IP并不是固定的,而且IP量特别大,几乎不会拨到相同
的IP,如果用它来搭建代理,既能保证高度可用,又可以自由控制号切换。经测试发现,这也是最稳定最有效
的代理方式。

    6.4.2购买动态拨号VPS云主机
在开始之前,需要先购买一台动态拨号VPS主机,在百度搜索能发现不少提供动态拨号VPS主机的眼务商,如
选择云立方(https://www.yunlifang.cn/), 提据实际需求自行选择,只要带宽满足需求即可。下面来
看看如何购买和安装。
步骤1:打开云立方官网https://www.yunlifang.cn/. 如书本p145,6-12所示。

    可以看到，这里提供了很多区域的选项，如选择四川电信线路，（推荐购买电信线路），这里为演示
选则6元一天的，然后单击立即购买，

步骤2：购买完成之后就需要安装操作系统了，进入拨号主机的后台，需要先预装一个操作系统，这里
选择Ctentos7.1版本，选择好版本之后，单击马上预装操作系统，这时网站会把相关的ssh连接账号
和密码信息发送给用户，记录下账号密码，然后等待5~6分钟，就可以使用xshell工具去连接了。

    如这里分配的IP和端口分别为110.187.88.59和20057,用户名为root，（仅供演示使用，可能已经过期）
    
    6.4.3 测试拨号
    
    在成功购买一台主机和安装好操作系统之后，接下来需要使用远程工具xshell去连接，测试一下它的
拨号效果，操作步骤如下：

步骤1：打开xshell连接工具，新建一个会话，输入已获取到的账号信息，xshell工具可自行下载。
步骤2：输入完成之后，单击确定按钮，然后输入管理密码，就可以连接上远程服务器了。
步骤3：进入之后，发现已经默认把ADSL账号和密码初始化设置好了（账号和密码为购买时告知的账号和密码）
    在拨号之前测试ping任何网站都是不通的，因为当前网络还没连通，如这里ping一下www.baidu.com,
不能连通。
步骤4：这时可以输入命令“adsl-start”,发现拨号明令成功运行，没有任何报错信息，证明拨号成功了，
耗时约几秒钟，重新ping网站www.baidu.com,成功ping百度并返回了信息。

步骤5：如果要停止接号可以输入"adsl-stop"命令,停止之后,会发现又连不通网络了。所以只有拨号之后
才可以建立网络连接。
断线重播的命令就是以上二者的组合,先执行adsl-stop,再执行adsl-start,每拨一次号,用ifocnfg命令
观察一下主机的IP,发现主机的IP一直是在变化的,网卡名称为ppp0,如图6-20所示。

    由此看来,如果将这台主机作为代理服务器,一直拨号换IP,就不用担心IP被封了,即使某个IP被封了,
重新拨一次号就好了。
    接下来就需要将主机设置为代理服务器,以及实时获取拨号主机的IP。
    6.4.4设置代理服务器
    经常听说代理服务器,那么如何将自己的主机设置为代理服务器呢?接下来就来介绍搭建HTTP代理服务器
的方法。
    在Limu系统下搭建HTTP代理服务器,推荐TinyProxy和Squid,配置都非常简单,这里以TinyProxy为例
来介绍搭建代理服务器的方法。
步骤1:安装TiyProxy。依次执行以下命令: yum intall-y epel-release、 yum update-y、
yum install-y tinyproxy。,运行完成之后就完成TinyProxy的安装了。
步骤2:配置TinyProxy。安装完成之后还需要配置TinyProxy才可以将其用作代理服务器,需要编辑配置文
件,它一般的路径是/etc/tinyproxy/tinyproxy.conf.这里使用vim命令进入编辑界面(需要注意的是,
如果提示vim命令不可用,则需要使用yum intall vim 命令进行安装),如图6-21所示。
    可以看到有一行"Port8888",在这里可以设置代理的端口,默认是8888,然后继续向下找,有一行
"Allow 127.0.0.1" ,这是被允许连接的主机的IP,如果想任何主机都可以连接,那么就直接将它注释即可,
这里选择直接注释,将其修改为"#Allow 127.0.0.1",然后退出保存。
    步骤3:重启TinyProxy。设置完成之后,输入"service tinyproxy start"命令。
    步骤4:验证TinyProxy。这样就成功搭建好代理服务器了,用ifconfig查看下当前主机的IP,例如,
当前主机拨号IP为182.132.225.4,在其他的主机运行测试一下。例如,用curl命令设量代理请求httpbin,
检测代理是否生效。在Windows命令行中执行curl-x 182.132.225.4:8888httpbin.org/get命令,
如图6-22所示。
    
    如果有正常的结果输出并且origin的值为代理IP的地址,就证明TinyProxy配置成功了,说明这个代理
是可以用的。
    6.4.5动态获取IP
    说到动态获取主机IP,很多人可能首先会想到DNS,也就是动态域名解析服务,它需要使用一个城名来
解析,也就是虽然IP是变的,但域名解析的地址可以随着IP的变化而变化。它的原理其实是拔号主机向固定
的服务器发出请求,服务器获取客户端的IP,然后再将域名解析到这个IP上。
    关于域名,网上有很多平台都提供注册,如阿里云、腾讯云等。用户只需要注册好域名将它解折到搭建
的代理服务器就可以了,操作步骤如下。
步骤1:这里以在腾讯云上注册的一个域名为例(具体注册和解析步骤请参考域名提供商官网),将注册的域名
"ads.liuyanlin.cn"解析到服务器。
步骤2:解析完成后通过ping命令测试,就能看出是否成功解析,如图6-23所示。
    
    接下来需要安装nginx,并使用nginx做反向代理。安装nginx可以直接使用yum安装,命令为
yum install nginx,默认安装在/etc路径下。修改nginx.conf 配置文件,如图6-24所示。
    在location下加上一句"proxy_pass 127.0.1:8888”,表示反向到本机8888端口,然后保存并重新
启动nginx(执行nginx-s reload命令)。设置完成就能够通过域名动态获取IP了。
    此外，这个域名解析也可使用花生壳(花生壳是一个动态域名解析软件) ,它提供了免费版的动态城名
解析。当用户安装并注册花生壳动态域名解析软件后,无论用户在任何地点、任何时间、使用任何线路,均
可利用这一服务建立拥有固定域名和最大自主权的互联网主机。

    6.4.6使用Python实现拨号
    搭建好自己的代理服务器后,需要使用时,每次都手动使用xshell登量录服务器去拨号是不现实的,所
以就需要使用程序去自动拨号返回需要的IP。下面以Python为例,去实现模拟登录xshell断行ADSL拨号,
然后获取新的代理IP返回来供用户使用。首先使用pip命令安装好paramiko库,相关示例代码如下。
"""

import paramiko, re, time

# 定义一个类，表示一台远程Linux主机
class Linux(object):
    # 通过用户名、密码、超时时间初始化一个远程Linux主机
    def __init__(self,ip,username,password,timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = timeout
        # transport和chanel
        self.t = ''
        self.chan = ''
        # 连接失败的重试次数
        self.try_time = 3

        # 调用该方法连接远程主机
    def connect(self):
     while True:
            # 连接过程中可能会抛出异常，如网络不通、连接超时
      try:
        self.t = paramiko.Transport(sock=(self.ip,22))
        self.connect(username = self.username,password = self.password)
        self.chan = self.open_session()
        self.chan.settimeout(self.timeout)
        self.chan.get_pty()
        self.chan.invoke_shell()
        # 如果没有抛出异常，说明连接成功，直接返回
        print(self.chan.recv(65535).decode('utf-8'))
        return
      # 这里不对可能的异常如socket.error、socket.timeout细化，直接一网打尽
      except Exception as ex:
          if self.try_time !=0:
              print('连接%s失败，进行重试'%self.ip)
              self.try_time -= 1
          else:
              print('重试3次失败，结束程序')
              exit(1)
    # 断开连接
    def close(self):
        self.close()

    # 发送要执行的命令
    def send(self,cmd):
     cmd +='\r'
     result = ''
     # 发送要执行的命令
     self.chan.send(cmd)
     # 回显很长的命令可能执行较久，通过循环分批次取回回显，执行成功返回True，失败返回False
     while  True:
         time.sleep(0.5)
         ret = self.chan.recv(65535)
         ret = ret.decode('utf-8')
         result += ret
         return result
     # 连接正常的情况
if __name__ == '__main__':
    host = Linux('110.187.88.59','root','P5AzifzHc5') # 传入IP、用户名、密码
    host.connect()
    adsl = host.send('adsl-start') # 发送一个拨号命令
    result = host.send('ifconfig') # 发送一个查看IP的命令
    ip = re.findall(".*?inet.*?(\d+\.\d+\.\d+.)*?netmask",result)
    print("拨号后的IP是："+ip[0])
    host.close()

    """这里使用Python实现了一个模拟xshell的功能，用他就可以远程自动连接而代理服务器，然后使用
send方法发送执行命令，最后从返回的结果中用正则匹配出需要的IP，得到这个IP后就可以应用到爬虫中了
    至此，ADSL拨号代理服务器搭建完成了。
    
    
    
    6.5新手问答
    学习完本章之后,读者可能会有以下疑问：
    
1,如果代理没有使用成功,那么问题出在哪里?

答:如果在实际过程中,代理使用不成功,可以先排除代理是否可用,如通过ping命令去pig一下代理,看能否
ping通,或者也可以换几个网站访问试试,也不排除所使用的代理是别人用过的。所以有问题要多分析、多观察。

2,爬虫如何在工作中解决代理IP不足的问题?

答:在爬虫工作过程中,经常会被目标网站禁止访问,但又找不到原因,这是令人非常头疼的事情。一般来说,
目标网站的反爬虫策略都是依靠IP来标识爬虫的,很多时候,我们访问网站的IP地址会被记录,当服务器认为这
个P是爬虫,那么就会限制或禁止此IP访问。被限制P最常见的一个原因是抓取频率过快,超过了目标网站所设置
的阔值,将会被服务器禁止访问。所以,很多爬虫工作者会选择使用代理IP来辅助爬虫工作的正常运行。
但有时不得不面对这样一个问题,代理IP不够用,即使去买,这里也有两个问题,一是成本问题,二是高效代理IP
并不是到处都有。
    通常,爬虫工程师会采取两个办法来解决问题：
(1)放慢抓取速度,减少IP或其他资源的消耗,但是这样会减少单位时间的抓取量,可能会影响到任务是否能按
时完成。
(2)优化爬虫程序,减少一些不必要的程序,提高程序的工作效率,减少对IP或其他资源的消耗，这就需要资深
爬虫工程师了。

    如果说这两个办法都已经做到极致了,还是解决不了问题,那么只有加大投入继续购买高效的代理IP来保障
爬虫工作高效、持续、稳定地进行

3.设置了代理,如proxy_ip=(HTTP:49.85.13.8:359097,但是没生效,到网上找了很多代理但是始终显示的是
自己的IP,这是什么问题?

答:这个是代理格式的问题造成的,正确的格式为1thtp:htp//roy-iporto。外,也可能是该代理不可用。
    小结：
    本章开始讲解了Python主要的网络请求库的代理设置,然后讲了代理池的构建、如何获取免费的代理和收
费的代理,最后详细地讲解了如何去搭建自己的ADSL拨号服务器,并使用Python去远程拨号获取最新的IP。
"""










