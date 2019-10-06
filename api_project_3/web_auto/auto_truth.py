# -*- coding: utf-8 -*-
# Created by xj on 2019/4/26
"""selenium 原理
http协议搭建的webdriver接口
1.webdriver启动目标浏览器chrome.exe 之后chrome在对应的chromedriver在对应的端口打开一个webdriver服务 端口9515、
2.webdriver与浏览器服务端建立连接 chromRmoteConnection 然后客户端通过commandExecute发送http请求到服务器，服务器收到请求后执行相应的行为并返回结果
"""
from selenium import webdriver
import requests
driver=webdriver.Chrome(port=9515)
driver.get("http://www.baidu.com")
session_id=driver.session_id
url='http://localhost:9515/session/{}/url'.format(session_id)
bai_url='http://www.baidu.com'
data={"url":bai_url} #传递字典参数
requests.post(url,json=data) #发起访问百度请求
 #定位元素
driver.find_element_by_name()
url='http://localhost:9515/session/{}/element'.format(session_id)
p={'using': 'css selector','value':'#kw'}
#返回响应状态码
res=requests.post(url,json=p)
print(res)

