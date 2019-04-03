# -*- coding: utf-8 -*-
# Created by xj on 2019/4/1

import unittest
from unittest import mock
from api_project_2 import payment
class Testpay(unittest.TestCase):
    """1.用户信息完整，付款成功
       2.用户信息完整，付款失败
       3.请求超时，再次付款成功
       4.请求超时，再次付款失败"""
    # def test_pay_success(self):
    #     pay=payment.Payment() #创建对象
    #     pay.requestOutofSystem=mock.Mock(return_value=200) #模拟方法调用的时候不加（）。模拟第三方支付接口返回200
    #     resp=pay.dopay(use_id=1,car_num='12345678',amount=100)
    #     self.assertEqual('success',resp)
    def test_pay_fail(self):
        pay=payment.Payment()
        pay.requestOutofSystem=mock.Mock(return_value=500)
        resp=pay.dopay(use_id=2,car_num='12345678',amount=200)
        pay.requestOutofSystem.assert_called_once_with('12345678',200)  # 断言使用了参数被只被调用过一次

        self.assertEqual('fail',resp)

    def test_retry_fail(self):
        pay=payment.Payment()
        pay.requestOutofSystem=mock.Mock(side_effect=[TimeoutError,200])#side_effect的值必须时可地带的，这里必须注意必须要可迭代序列
        resp=pay.dopay(use_id=3,car_num='123',amount=200)
        pay.requestOutofSystem.called #断言是否被调用
        pay.requestOutofSystem.assert_called_with('123',200)#断言被调用并且传参正确 ,这里参数传递非常严格
        pay.requestOutofSystem.assert_called()#断言是否被至少被调用一次
        # pay.requestOutofSystem.assert_called_once()#断言是否只能被调用一次
        # pay.requestOutofSystem.assert_called_once_with()#断言使用了参数被只被调用过一次
        print(pay.requestOutofSystem.call_count)#判断曾经被调用的次数
        print(pay.requestOutofSystem.call_args)#获取最近调用时所使用的参数
        print(pay.requestOutofSystem.call_args_list)#生成曾经被调用时的参数列表
        print(pay.requestOutofSystem.method_calls)#测试当前对象调用了哪些方法--列表

        self.assertEqual('success',resp)


if __name__ == '__main__':
    unittest.main()