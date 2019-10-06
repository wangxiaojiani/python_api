# -*- coding: utf-8 -*-
# Created by xj on 2019/4/22
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
driver=webdriver.Chrome() #创建浏览器对象

#打开课堂派登录页面
driver.get('https://www.ketangpai.com/Home/User/login.html')

#浏览器器页面最大化
driver.maximize_window()

#获取浏览器url及当前窗口句柄及标题
print(driver.current_url)
print(driver.current_window_handle)
print(driver.title)

#点击首页
driver.find_element_by_xpath("//div[@id='indextop']/child::div[@class='nav fl']//a").click()

#设置等待时间(隐式等待)
driver.implicitly_wait(10)

#设置显示等待，并定位到解决方案对象
solution_obj=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@id='solutiontop']/a")))

#鼠标悬浮在解决方案上并点击本地申请机构版
ActionChains(driver).move_to_element(solution_obj).perform()
#双击本地化部署
local_private=driver.find_element_by_xpath("//div[@id='solutiontop']/ul/li/a[text()='本地化部署']")
ActionChains(driver).double_click(local_private).perform()

#滑动下拉框到指定位置
js='window.scrollTo(0,300);'
driver.execute_script(js)
time.sleep(4)
#滑动到页面顶端，点击登录按钮
top_js ='window.scrollTo(0,0)'
driver.execute_script(top_js)
driver.find_element_by_xpath("//div[@id='indextop']/div[@class='log-reg fr']/a[text()='登录']").click()


#跳转到登录页面，输入帐号及密码点击登录
time.sleep(3)
user_obj=driver.find_element_by_xpath("//span[text()='账号：']/following-sibling::input")
user_obj.clear()
user_obj.send_keys("13296662567")
time.sleep(4)
user_pwd=driver.find_element_by_xpath("//span[text()='密码：']/following-sibling::input")
user_pwd.clear()
user_pwd.send_keys("123456")

#勾选下次自动登陆
driver.find_element_by_xpath("//a[text()='下次自动登录']").click()

#打印登录按钮的text文本（这里就不演示登录啦）
print(driver.find_element_by_xpath("//a[@class='btn-btn']").text)
time.sleep(4)
#返回上一页面
driver.forward()


#截图
p=os.getcwd()
p_t=os.path.join(p,'截图.png')
driver.get_screenshot_as_file(p_t)

#关闭浏览器
driver.close()




