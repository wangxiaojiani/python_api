# -*- coding: utf-8 -*-
# @Time      :2019/10/1    13:28
# @Author    :xj
# @Email     :1027867874@qq.com
# @File      :login_test.py
# @Software  :PyCharm

import unittest
from ddt import ddt,unpack,data
from test_auto_interface.comon.my_path import test_data_path
from test_auto_interface.comon.do_excel import DoExcel
from test_auto_interface.comon.test_request import HttpRequest
test_data=DoExcel(test_data_path,'login').do_excel('BUTTON')
cookie=None

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        print('开始执行测试用例')
        self.t=DoExcel(test_data_path,'login')
    def tearDown(self):
        print('测试用例执行完毕')
    @data(*test_data)
    def test_case_1(self,data_item):
        global test_result
        global cookie
        print("正在执行第{0}条用例:{1}".format(data_item['Case_id'],data_item['Title']))
        #开始执行http请求
        res=HttpRequest(data_item['Url'],eval(data_item['Params'])).http_request(data_item['Method'])
        if res.cookies:
            cookie=res.cookies
        try:
            self.assertEqual(eval(data_item['ExpectResult']),res.json())
            test_result='Pass'
        except Exception as e:
            print('执行本接口时测试断言出错，错误是{}'.format(e))
            test_result='Failed'
            raise e
        finally:
            self.t.write_back(data_item['Case_id']+1,9,str(res.json()))
            self.t.write_back(data_item['Case_id']+1,10,test_result)


if __name__ =='__main__':
    unittest.main()
