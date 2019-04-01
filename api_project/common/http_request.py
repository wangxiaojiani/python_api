# -*- coding: utf-8 -*-
# Created by xj on 2019/3/10

import requests

class HttpRequest:
    def __init__(self,url,method,param):
        self.url=url
        self.method=method
        self.param=param   #get请求所需的参数


    def http_request(self):
        '''根据请求方法来决定发起get请求还是post请求
        method: get post http的请求方式
        url:发送请求的接口地址
        param:随接口发送的请求参数 以字典格式传递
        rtype:有返回值，返回结果是响应报文'''
        if self.method.lower()=='get':
            print('正在发起get请求')
            try:
                resp=requests.get(self.url,self.param)
            except Exception as e:
                print('错误是{}'.format(e))
        elif self.method=="post":
            print('正在发起post请求')
            try:
                resp=requests.post(self.url,data=self.param)
            except Exception as e:
                print('错误是{}'.format(e))
        else:
             print("你输入的请求方式不正确")
             resp = None

        return resp.text #返回结果


if __name__ == '__main__':

    url="http://47.107.168.87:8080/futureloan/mvc/api/member/register"
    param={"mobilephone":"13877881676","pwd":"123456"}
    resp =HttpRequest(url,"get",param).http_request()
    print(resp)


