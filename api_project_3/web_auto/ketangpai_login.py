# -*- coding: utf-8 -*-
# Created by xj on 2019/4/26

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
#打开登录页面
driver.get("https://www.ketangpai.com/User/login.html")
def wait_find_element(locator) -> WebElement:
    wait=WebDriverWait(driver,50,0.5)
    ele=wait.until(ec.presence_of_element_located(locator))
    return ele
#添加隐士等待
driver.implicitly_wait(30)
#点击微信登录
ele=wait_find_element((By.XPATH,"//div[@id='login']/div/a[text()='微信登录']"))
ActionChains(driver).click(ele).perform()
#切换到iframe中获取二维码元素

wei_xin_frame=driver.find_element_by_xpath("//div[@id='login_container']/iframe")
WebDriverWait(driver,30,0.5).until(ec.frame_to_be_available_and_switch_to_it(wei_xin_frame))
#定位二维码
img=WebDriverWait(driver,30,0.5).until(ec.presence_of_element_located((By.XPATH,"//div[@class='wrp_code']/img")))
print(img.get_attribute('src'))



