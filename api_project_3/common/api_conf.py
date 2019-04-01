# -*- coding: utf-8 -*-
# Created by xj on 2019/3/11
from configparser import ConfigParser
from api_project_3.common import project_path
class MyConfig:
    def __init__(self):
        self.mc =ConfigParser()
        self.mc.read(project_path.api_config_path,encoding="utf-8")

    def get_str(self,option,section):
        return self.mc.get(option,section)
    def get_int(self,option,section):
        return self.mc.getint(option,section)
    def get_float(self,option,section):
        return self.mc.getfloat(option,section)
    def get_list(self,option,section):#字典，列表，元组 用这个转换
        s=self.get_str(option,section)
        return eval(s)
if __name__ == '__main__':
    button = MyConfig().get_list("RECHARGE","m_mobile")
    print(type(button))
    member_ID = MyConfig().get_list('ADDLOAN', 'member_ID')
    print(type(member_ID))
    pwd=MyConfig().get_list("ADDLOAN","pwd")
    print(type(pwd))
