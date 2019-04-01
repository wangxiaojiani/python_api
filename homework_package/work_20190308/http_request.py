# -*- coding: utf-8 -*-
# Created by xj on 2019/3/10

import requests

class HttpRequest:
    def __init__(self,url,method,param):
        self.url=url
        self.method=method
        self.param=param   #get请求所需的参数


    def http_request(self):
        '''url:请求的url地址
           method:请求的方式 get post可以选择'''
        if self.method.lower()=='get':
            print('正在发起get请求')
            try:
                resp=requests.get(self.url,self.param)
            except Exception as e:
                print('错误是{}'.format(e))
        else:
            print('正在发起post请求')
            try:
                resp=requests.post(self.url,data=self.param)
            except Exception as e:
                print('错误是{}'.format(e))

        return resp.text #返回结果


if __name__ == '__main__':

    url="http://47.107.168.87:8080/futureloan/mvc/api/member/login"
    param={"mobilephone":"13877881676","pwd":"123456"}
    resp =HttpRequest(url,"get",param).http_request()
    print(resp)


