# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 20:44
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 配置文件学习.py
#什么是配置文件 .conf .ini .config .properties .xml
#A:怎么写配置文件---[section] option value
#B：怎么读取配置文件---configparser 模块里面的ConfigParser类 可以定位
from configparser import ConfigParser

#创建对象：
cf=ConfigParser()
#第一步：打开文件 read()
cf.read('lemon.conf',encoding='utf-8')

#第二步读取内容 section option
# res=cf.get('StudentName','stu_3')
# res=cf['StudentName']['stu_6']
# res=cf.getfloat('StudentName','stu_3')#
# res=cf.getint('StudentName','stu_4')
res=cf.getboolean('StudentName','stu_5')
print(res)
print(type(res))

#配置文件里面读取出来的所有数据 都是字符串
#eval()---把括号里面的数据变成原本的数据类型

#作业
#写一个配置类  有以下几个函数：
#1：读取整数
#2：读取浮点数
#3：读取布尔值
#4：读取其他类型的数据 list tuple dict eval（）
#5：读取字符串

