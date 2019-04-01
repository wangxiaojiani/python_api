# -*- coding: utf-8 -*-
# Created by xj on 2019/3/10

import requests
import json
url="http://47.107.168.87:8080/futureloan/mvc/api/member/login"
param={"mobilephone":"13877881676","pwd":"123456"}
resp=requests.get(url,param)
s=resp.text
print(s)
value=json.loads(s)
print(value)