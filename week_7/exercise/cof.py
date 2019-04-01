# -*- coding: utf-8 -*-
# Created by xj on 2019/3/9

from configparser import ConfigParser

class MyConfig:
    def __init__(self,filename):
        self.mc =ConfigParser()
        self.mc.read(filename,encoding='utf-8')
    def read_str(self,option,section):
        return self.mc.get(option,section)
    def read_int(self,option,section):
        return self.mc.getint(option,section)
    def read_float(self,option,section):
        return self.mc.getfloat(option,section)
    def read_bool(self,option,section):
        return self.mc.getboolean(option,section)
    def read_list(self,option,section):
        s=self.read_str(option,section)
        if s =='ALL':
            return s
        else:
            s=eval(s)
            return s
if __name__ == '__main__':
    mc=MyConfig('conf.config')
    S = mc.read_list('TESTCASE','button')
    print(S)