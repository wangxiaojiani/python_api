# -*- coding: utf-8 -*-
# Created by xj on 2019/3/10
import json

s= '{"status":1,"code":"10001",' \
   '"data":' \
   ' {"id":1126527,' \
   '"leaveamount":"26300.00",' \
   '"mobilephone":"13999099933",' \
   '"pwd":"E10ADC3949BA59ABBE56E057F20F883E",' \
   '"regname":"小蜜蜂", ' \
   '"regtime":"2019-03-22 00:07:37.0",' \
   '"type":"1"}, ' \
   '"msg":"充值成功"}'

p=eval(s)

print(p)
