# -*- coding: utf-8 -*-
# Created by xj on 2019/3/10

import unittest
from homework_package.work_20190308.http_request import HttpRequest
from homework_package.work_20190308.do_excel import DoExcel
from ddt import ddt,unpack,data
import json
test_data_2 =DoExcel("API_TEST.xlsx", "Sheet1").read_excel(9,14) #对应登录的测试用例 也可以通过配置文件来修改
test_data_1 =DoExcel("API_TEST.xlsx", "Sheet1").read_excel(2,8)  #对应注册的测试用例

@ddt
class HttpTest(unittest.TestCase):

    def setUp(self):
        print("开始执行用例啦")
        self.t=DoExcel("API_TEST.xlsx","Sheet1")

    def tearDown(self):
        print("用例执行完毕啦")
    @data(*test_data_2)
    @unpack
    def test_2_get_login(self,case_id,module,title,method,para,expect_result):#通过get请求来登录
        print("开始执行第{}条用例".format(case_id))
        resp_t=HttpRequest("http://47.107.168.87:8080/futureloan/mvc/api/member/login","get",eval(para)).http_request()#若想用post方法 直接将eval(param)改成data=eval(param)
        try:
            self.assertEqual(expect_result,resp_t) #判断期望结果与实际结果是否相等
            test_result="Pass" #如果没报错 执行结果为pass
        except Exception as e:
            print("报错了，报错信息为{}".format(e))
            test_result="Failed"#如果报错执行结果为failed
            raise e
        finally:
            self.t.write_back(case_id+1,7,resp_t) #写回实际结果
            self.t.write_back(case_id+1,8,test_result) #写入测试结果
            print("第{}条用例结束".format(case_id))

    @data(*test_data_1)
    @unpack
    def test_1_get_register(self, case_id, module, title, method, param, expect_result): #通过get请求来注册
        print("开始执行第{}条用例".format(case_id))
        url="http://47.107.168.87:8080/futureloan/mvc/api/member/register"

        resp_t = HttpRequest(url,"get",eval(param)).http_request() #若想用post方法 直接将eval(param)改成data=eval(param)

        try:
            self.assertEqual(expect_result,resp_t)  # 判断期望结果与实际结果是否相等
            test_result = "Pass"  # 如果没报错 执行结果为pass
        except Exception as e:
            print("报错了，报错信息为{}".format(e))
            test_result = "Failed"  # 如果报错执行结果为failed
            raise e
        finally:
            self.t.write_back(case_id + 1, 7, resp_t)  # 写回实际结果
            self.t.write_back(case_id + 1, 8, test_result)  # 写入测试结果
            print("第{}条用例执行完毕".format(case_id))







