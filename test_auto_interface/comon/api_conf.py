# -*- coding: utf-8 -*-
#@Time      :2019/10/1    1:43
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :api_conf.py
#@Software  :PyCharm

from configparser import  ConfigParser
from test_auto_interface.comon.my_path import current_conf_path

class MyConfig:
    def __init__(self):
        self.mc=ConfigParser()
        self.mc.read(current_conf_path,encoding='utf-8')
    def get_str(self,section,option):
        return self.mc.get(section,option)
    def get_int(self,section,option):
        return self.mc.getint(section,option)
    def get_float(self,section,option):
        return self.mc.getfloat(option,section)
    def get_boolen(self,option,section):
        return self.mc.getboolean(option,section)
    def get_list(self,option,section):
        s=self.get_str(option,section)
        return eval(s)
if __name__ =='__main__':
    s1=MyConfig().get_int('APP','login_1')
    print(s1)
    print(type(s1))
    s2 = MyConfig ().get_str ('APP', 'login_2')
    print (s2)
    print (type (s2))
    s3 = MyConfig ().get_list('APP', 'login_3')
    print (s3)
    print (type (s3))
    s4 = MyConfig ().get_list('APP', 'login_4')
    print (s4)
    print (type (s4))
    s5 = MyConfig ().get_list('APP', 'login_5')
    print (s5)
    print (type (s5))
    s6 = MyConfig ().get_boolen ('APP', 'login_6')
    print (s6)
    print (type (s6))
