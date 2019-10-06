# -*- coding: utf-8 -*-
#@Time      :2019/10/1    9:42
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :get.py
#@Software  :PyCharm
"""
本脚本主要用来演示类的反射，主要可以查看，新增，修改，删除类的属性
"""
import re
class GetDate:
    cookie=None
def re_place(target):
    p='#(.*?)#'
    while re.search(p,target):
        m=re.search(p,target)
        key=m.group(1)
        value=getattr(GetDate,key)
        target=re.sub(p,value,target,count=1)
    return target




a=12
