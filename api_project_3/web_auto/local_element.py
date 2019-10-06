
# -*- coding: utf-8 -*-
# Created by xj on 2019/4/18
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://github.com/topics')
driver.maximize_window()#浏览器最大


ele=WebDriverWait(driver,30,0.5).until(ec.presence_of_element_located((By.ID,'name')))


#通过xpath定位元素---层级定位----定位3D缩略图元素  通过先找到3D元素再去找祖先
# ele=driver.find_element_by_xpath("//div[@class='flex-auto']/p/ancestor::a/div")

#通过xpath text定位-------定位3D缩略图元素  通过先找到3D元素再去找祖先
# ele=driver.find_element_by_xpath("//p[text()='3D']/ancestor::a/div")

#通过xpath 标签标签属性进行模糊定位----------定位3D缩略图元素  通过先找到3D元素再去找祖先
# ele=driver.find_element_by_xpath("//p[contains(text(),'3')]/ancestor::a/div")

#通过xpath 标签属性定位-----------定位3D缩略图元素  通过先找到3D元素再去找祖先
# ele=driver.find_element_by_xpath("//p[@class='f3 lh-condensed mb-0 mt-1 link-gray-dark']/ancestor::a/div")

#稍微麻烦一点的
ele=driver.find_element_by_xpath("//div[@class='flex-auto']/p/preceding::li[@class='py-4 border-bottom']/descendant::div")

#定位3Dstar元素
sle=driver.find_element_by_xpath("//form[@class='unstarred']/button")


#定位AMP的缩略图
amp=driver.find_element_by_xpath("//p[text()='Amp']/preceding::img[@class='rounded-1 mr-3']")
#定位星星
amp_star=driver.find_element_by_xpath("//ul[@class='list-style-none']/li[4]/descendant::form[2]/button")

#定位Atom缩略图
atom=driver.find_element_by_xpath("//p[text()='Atom']/preceding::img[@class='rounded-1 mr-3']")
#定位星星
atom_star=driver.find_element_by_xpath("//ul[@class='list-style-none']/li[11]/descendant::button")




