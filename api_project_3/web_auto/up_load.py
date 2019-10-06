# # -*- coding: utf-8 -*-
# # Created by xj on 2019/4/28
#
#
# import win32gui
# import win32con
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import os
#
# def up_file(file_path):
#     '定义上传文件函数'
#     #找到对应的窗口
#     dialog=win32gui.FindWindow("#32770","打开")#一级窗口
#     #找到窗口
#     ComboBoxEx32=win32gui.FindWindowEx(dialog,0,'ComboBoxEx32',None) #二级窗口
#     comboBox=win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None) #三级窗口
#     edit=win32gui.FindWindowEx(comboBox,0,'Edit',None) #四级窗口
#     button=win32gui.FindWindowEx(dialog,0,'Button','打开(&O)') #二级窗口
#     #操作
#     win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,file_path) #发送文件路径
#     win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)  #点击打开按钮
#
#
# #初始化浏览器对象
# driver=webdriver.Chrome()
# # 访问课堂派登陆页面
# driver.get("https://www.ketangpai.com/")
# #添加隐士等待
# driver.implicitly_wait(30)
#
# #放大浏览器
# driver.maximize_window()
# #定义显示等待函数,返回定位到的元素对象
# def find_element_wait(locator) ->WebElement:
#     wait=WebDriverWait(driver,30,0.5)
#     e=wait.until(ec.presence_of_element_located(locator))
#     return e
# login=find_element_wait((By.XPATH,'//a[text()="登录"]'))
# #利用鼠标行为来点击登录按钮
# ActionChains(driver).click(login).perform()
#
# #定位账号文本框用来判断页面跳转成功
# WebDriverWait(driver,30,0.5).until(ec.visibility_of_element_located((By.XPATH,"//input[@name='account']")))
#
# #在账号输入框中输入手机号
# account=find_element_wait((By.XPATH,"//input[@name='account']"))
# account.clear()
# account.send_keys("13296662567")
# #定位到密码框
# user_pwd=find_element_wait((By.XPATH,"//span[text()='密码：']/following-sibling::input"))
# user_pwd.clear()
# user_pwd.send_keys("wangjian920913@@")
# #利用键盘操作点击登录按钮
# user_pwd.send_keys(Keys.ENTER)
#
# #通过定位到元素来判断页面是否跳转成功
# WebDriverWait(driver,30,0.5).until(ec.visibility_of_element_located((By.XPATH,"//a[@class='jumptoclass']")))
# #点击 python全栈第14期连接
# link_a=find_element_wait((By.XPATH,"//a[@class='jumptoclass']"))
# link_a.click()
#
# #通过 交互操作作业  元素来判定页面是否跳转成功
# WebDriverWait(driver,30,0.5).until(ec.visibility_of_element_located((By.XPATH,"//a[@title='交互操作作业']")))
#
# #通过js来执行滚动条滚动操作 拉到页面顶端 可以这样像x，y是以页面右上角为原点
# js="return window.scrollTo(0,document.body.scrollHeight);"
# driver.execute_script(js)
# time.sleep(4)
# #通过python来实现滚动条操作
# #首先定位到  交互操作作业元素
# ele=find_element_wait((By.XPATH,"//a[@title='交互操作作业']"))
# # ele.location_once_scrolled_into_view()#将元素移动可视范围(不好用)
# #通过js的另外一种方式实现 元素的底端与窗口底端对齐
# driver.execute_script("arguments[0].scrollIntoView(false);",ele)
# time.sleep(3)
# #鼠标点击操作
# ActionChains(driver).click(ele).perform()
#
# #通过定位上传按钮，判断页面是否跳转成功
# WebDriverWait(driver,30,0.5).until(ec.visibility_of_element_located((By.XPATH,"//div[text()='上传文件']/parent::a")))
# button_up=find_element_wait((By.XPATH,"//div[text()='上传文件']/parent::a"))
# #点击上传按钮
# button_up.click()
# #执行上传文件操作
# time.sleep(4)
# up_file(r"C:\Users\1\Desktop\武汉-小贱-14-2018-1-8\xiaer.jpg")
# #截图保存
# p=os.path.join(os.getcwd(),"picture.png")
# driver.get_screenshot_as_file(p)
# time.sleep(5)
#


#
def run(*args):
    print(*args)


run((1,2,3,4))

