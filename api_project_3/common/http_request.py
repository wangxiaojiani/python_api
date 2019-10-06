# -*- coding: utf-8 -*-
# Created by xj on 2019/3/10

import requests
class HttpRequest:
    def __init__(self,url,method,param):
        self.url=url
        self.method=method
        self.param=param   #get请求所需的参数

    def http_request(self,cookie):
        '''根据请求方法来决定发起get请求还是post请求
        method: get post http的请求方式
        url:发送请求的接口地址
        param:随接口发送的请求参数 以字典格式传递
        resp:有返回值，返回结果是响应对象实体
        '''
        if self.method.upper()=='GET':
            print('正在发起get请求')
            try:
                resp=requests.get(self.url,params=self.param,cookies=cookie)
            except Exception as e:
                print('错误是{}'.format(e))
        elif self.method.upper()=="POST":
            print('正在发起post请求')
            try:
                resp=requests.post(self.url,data=self.param,cookies=cookie)
            except Exception as e:
                print('错误是{}'.format(e))
        else:
             print("你输入的请求方式不正确")
             resp = None
        return resp #返回结果


if __name__ == '__main__':
    url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'  # 接口地址
    param = {"mobilephone":"137786","pwd":"123456"}  # 字典的形式存储参数数据
    method = 'GET'

    resp = HttpRequest( url,method, param).http_request('None')
    print(resp.text)
    print(resp.headers)


