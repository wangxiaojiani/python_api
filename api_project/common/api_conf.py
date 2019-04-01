# -*- coding: utf-8 -*-
# Created by xj on 2019/3/11
from configparser import ConfigParser
from common import project_path
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
    def get_list(self,option,section):
        s=self.get_str(option,section)
        if s=="ALL":
            return s
        else:
            return eval(s)
if __name__ == '__main__':
    button = MyConfig().get_list("SELECT", "button")
    print(button)