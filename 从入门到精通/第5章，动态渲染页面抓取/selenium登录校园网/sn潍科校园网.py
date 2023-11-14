# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver

# 使用谷歌驱动
driver = webdriver.Chrome()
# 打开校园网url或者任意网页，使校园网登陆页面弹出

time.sleep(2)
driver.get("https://www.csdn.net/")
# 由于校园很垃圾，加载不稳定，我们默认等它5秒
time.sleep(5)
# 下面就开始定位点击登录了，
# 点击自助服务
driver.find_element_by_id("selfservicea").click()
# 输入账号
driver.find_element_by_id("first_name").send_keys(15738108997)
# 点击及输入密码
driver.find_element_by_id("first_password").click()
driver.find_element_by_id("first_password").send_keys('azytgy')
# 点击登录按钮
driver.find_element_by_id("first_button").click()

# 为观察网络状况，我们让它登陆成功之后关闭窗口并打开csdn进行测试

# 基于校园网的跳转倒计时，我们等待7秒，然乎打开新的csdn窗口
time.sleep(7)


time.sleep(3)
print('登陆任务完成，是否连网成功请自行查看！（待优化）')
# 关闭浏览器
driver.quit()
