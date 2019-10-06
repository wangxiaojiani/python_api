# -*- coding: utf-8 -*-
# Created by xj on 2019/4/25
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://ke.qq.com/")
driver.maximize_window()
driver.implicitly_wait(30)
def wait_find_element(locator) -> WebElement:
    wait=WebDriverWait(driver,50,0.5)
    ele=wait.until(ec.presence_of_element_located(locator))
    return ele
ActionChains(driver).click(wait_find_element((By.XPATH,'//a[@id="js_login"]'))).perform()
WebDriverWait(driver,30,0.5).until(ec.visibility_of_element_located((By.XPATH,"//i[@class='icon-font i-qq']/parent::a")))
#QQ登录
button=wait_find_element((By.XPATH,"//i[@class='icon-font i-qq']/parent::a"))
driver.execute_script("return $(arguments[0]).click();",button)
WebDriverWait(driver,30,0.5).until(ec.frame_to_be_available_and_switch_to_it('login_frame_qq'))
ActionChains(driver).click(wait_find_element((By.XPATH,"//a[@id='switcher_plogin']"))).perform()
time.sleep(2)
qq=wait_find_element((By.CSS_SELECTOR,"#u"))
qq.send_keys("1027867874@qq.com")
pwd=wait_find_element((By.XPATH,"//input[@id='p']"))
pwd.send_keys("wangjian920913@@")
pwd.submit()






