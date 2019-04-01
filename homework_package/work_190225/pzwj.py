# -*- coding: utf-8 -*-
# Created by xj on 2019/2/25
import configparser

class MyConfig:
    "按照获取的数据类型来定义配置类"

    def __init__(self,filename):
        "初始化配置类"
        self.cf = configparser.ConfigParser()   #创建配置类对象
        self.cf.read(filename,encoding="utf-8") #打开配置文件

    def get_str(self,section,option):
        "读取字符串的方法"
        res=self.cf.get(section,option)
        return res

    def get_int(self,section,option):
        "读取整数的方法"
        res=self.cf.getint(section,option)
        return res

    def get_float(self,section,option):
        "读取浮点数的方法"
        res=self.cf.getfloat(section,option)
        return res

    def get_boolean(self,section,option):
        res=self.cf.getboolean(section,option)
        return res

    def get_else(self,section,option):
        "读取列表，字典，元组的方法"
        res=eval(self.get_str(section,option))
        return res
if __name__ == '__main__':
    cf=MyConfig("work_config.conf")
    print(cf.get_str("STUDENT_INFO","favourite"))#获取配置文件中的字符串
    print(cf.get_int("STUDENT_INFO","age")) #获取配置文件中的整型
    print(cf.get_float("STUDENT_INFO","score"))#获取配置文件中的浮点型
    print(cf.get_boolean("STUDENT_INFO","salary"))#获取配置文件中的布尔型
    print(cf.get_else("STUDENT_INFO","subject"))#获取配置文件中的列表
    print(cf.get_else("STUDENT_INFO","subject_scores"))#获取配置文件中的字典
    print(cf.get_else("STUDENT_INFO","boy_friend"))#获取配置文件中的元组



