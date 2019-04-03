# -*- coding: utf-8 -*-
# Created by xj on 2019/4/1
import requests
class Payment:
    def requestOutofSystem(self,car_num,amount):
        """定义一个第三方接口
        use_id:为用户id
        car_num:为用户卡号
        amount：为支付金额"""
        url='http://member/pay' #模拟请求的接口
        data={'car_num':car_num,'amount':amount}
        resp=requests.post(url,data=data)
        # if resp.status_code ==200:
        #     res ='success'
        # elif resp.status_code==500:
        #     res='fail'
        return resp.status_code

    def dopay(self,use_id,car_num,amount):
        try:

            resp=self.requestOutofSystem(car_num,amount)
            print("直接充值")
        except TimeoutError:
            print("重试一次")
            resp=self.requestOutofSystem(car_num,amount)
        if resp ==200:
            res='success'
            print("{}付款{}成功".format(use_id,amount))
        elif resp==500:
            res='fail'
            print("{}付款{}失败".format(use_id,amount))
        return res
