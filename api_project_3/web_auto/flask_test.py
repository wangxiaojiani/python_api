# -*- coding: utf-8 -*-
# Created by xj on 2019/4/14

# from flask import Flask,jsonify,request
#
# app=Flask(__name__)
# @app.route("/login")
# def login():
#     # return "login sucess"
#     # return jsonify({"code":"20001","msg":"你已经成功登录"})
#     # return '<html><p style="color:red">login sucess</p></html>'
#     # return '<xml><msg>nihao1</msg></xml>'
#     res=dict(request.args) #获取请求参数
#     return jsonify(res)
#
# if __name__ == '__main__':
#     app.run(debug=True)
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
# driver.get("http://www/12306.com")
def wait_find_element(locator):
    wait=WebDriverWait(driver,30,0.5)
    ele=wait.until(ec.presence_of_element_located(locator))
    return ele
# driver.find_element_by_id('kw').send_keys("柠檬班")
# driver.find_element_by_id('su').click()
# handles=driver.window_handles
# print(handles)
# print(len(handles))
# print(driver.current_window_handle)
# time.sleep(5)
# ele=driver.find_element_by_xpath('//a[contains(text(),"百度贴吧")]')
# print(type(ele))
# ele.click()
# s=WebDriverWait(driver,10).until(ec.new_window_is_opened(handles))
# handles=driver.window_handles
# print(2)
# print(handles)
# print(driver.window_handles)
# print(type(s))
# print(s)
# # driver.switch_to.window(handles[-1])
# time.sleep(5)


# print(driver.get_cookies())
# driver.add_cookie({'name':'aadddfgg','value':'dadakfkakf'})
# print('新添加的cookie')
# print(driver.get_cookies())
# for i in driver.get_cookies():
#     print("{}->{}".format(i["name"],i['value']))
# print(driver.get_cookie('aadddfgg'))
ele=wait_find_element((By.XPATH,"//a[text()='设置' and contains(@href,'http')]"))
print(ele)
ActionChains(driver).move_to_element(ele).click(ele).perform()

ActionChains(driver).click(wait_find_element((By.XPATH,"//a[text()='高级搜索']"))).perform()
time.sleep(4)
select=WebDriverWait(driver,30,0.5).until(ec.presence_of_element_located((By.XPATH,"//select[@name='ft']")))

select.click()
select.find_element_by_xpath("//option[@value='ppt']").click()
# Select(select).select_by_value("ppt")
Select(select).select_by_index(3)


#一种是通过js来实行定位后在执行相应的操做
driver.execute_script('e=document.getElementById("kw");')
time.sleep(2)
driver.execute_script('e.readOnly=false;')
time.sleep(2)
driver.execute_script('e.value="1028-09-12;"')

#先利用python定位到元素本身，在利用js
ele=wait_find_element((By.ID,'kw'))
driver.execute_script("argument[0].readOnly=false;",ele)