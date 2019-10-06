# -*- coding: utf-8 -*-
#@Time      :2019/9/30    19:56
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :test_request.py
#@Software  :PyCharm

import requests

class HttpRequest:
    #创建初始化化函数，每次请求都需要提供url及param参数
    def __init__(self,url,param):
        self.url=url
        self.param=param
    def http_request(self,method,cookies=None):
        if method.lower() =='get':
            try:
                res=requests.get(self.url,params=self.param,cookies=cookies)
            except Exception as e:
                print('执行get请求报错：错误是{}'.format(e))
                res='Error:get请求报错{}'.format(e)
        elif method.lower() =='post':
            try:
                res =requests.post(self.url,data=self.param,cookies=cookies)
            except Exception as e:
                print('执行post请求报错：错误是{}'.format(e))
                res='Error:post请求报错：错误是{}'.format(e)
        else:
            print('你输入的请求方式不对')
            res ='Error:你请求的方式不正确报错{}'.format(method)
        return res
if __name__ =='__main__':
    url='http://test.lemonban.com/futureloan/mvc/api/member/login'
    param={"mobilephone":"137786","pwd":"123456"}
    method='gET'
    res=HttpRequest(url,param).http_request(method)
    print(res.json())
    s=res.json()
    print(type(s))
    import json
    p=json.dumps(s,ensure_ascii=False)
    print(type(p))
    print(p)
    U=json.loads(p)
    print(type(U))
    print(U)