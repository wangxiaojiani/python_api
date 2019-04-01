# -*- coding: utf-8 -*-
# Created by xj on 2019/3/10

import unittest
from common.http_request import HttpRequest
from common.do_excel import DoExcel
from ddt import ddt,unpack,data
from common import project_path
from common.api_conf import MyConfig
from common.my_log import MyLog

button=MyConfig().get_list("SELECT","button")#从配置文件中读取指定用例


# test_data_2 =DoExcel(project_path.test_data_path, "Sheet1").read_excel(9,14) #对应登录的测试用例 也可以通过配置文件来修改
# test_data_1 =DoExcel(project_path.test_data_path, "Sheet1").read_excel(2,8)  #对应注册的测试用例
test_data =DoExcel(project_path.test_data_path, "Sheet1").read_excel(button)


mylog =MyLog()#日志实例化
@ddt
class HttpTest(unittest.TestCase):

    def setUp(self):
        print("开始执行用例啦")
        self.t=DoExcel(project_path.test_data_path,"Sheet1")

    def tearDown(self):
        print("用例执行完毕啦")
    @data(*test_data)
    @unpack
    def test_2_get_login(self,case_id,module,title,method,url,para,expect_result):#通过get请求来登录
        mylog.info("开始执行第{}条用例,用例的标题是{}".format(case_id,title))
        resp_t=HttpRequest(url,"get",eval(para)).http_request()#若想用post方法 直接将eval(param)改成data=eval(param)
        try:
            self.assertEqual(expect_result,resp_t) #判断期望结果与实际结果是否相等
            test_result="Pass" #如果没报错 执行结果为pass
        except Exception as e:
            mylog.error("报错了，报错信息为{}".format(e))
            test_result="Failed"#如果报错执行结果为failed
            raise e
        finally:
            self.t.write_back(case_id+1,8,resp_t) #写回实际结果
            self.t.write_back(case_id+1,9,test_result) #写入测试结果
            mylog.info("=====第{}条用例结束======".format(case_id))

    @data(*test_data)
    @unpack
    def test_1_get_register(self, case_id, module, title, method,url,param, expect_result): #通过get请求来注册
        mylog.info("开始执行第{}条用例,用例的标题是{}".format(case_id,title))

        resp_t = HttpRequest(url,"get",eval(param)).http_request() #若想用post方法 直接将eval(param)改成data=eval(param)

        try:
            self.assertEqual(expect_result,resp_t)  # 判断期望结果与实际结果是否相等
            test_result = "Pass"  # 如果没报错 执行结果为pass
        except Exception as e:
            mylog.error("报错了，报错信息为{}".format(e))
            test_result = "Failed"  # 如果报错执行结果为failed
            raise e
        finally:
            self.t.write_back(case_id + 1, 8, resp_t)  # 写回实际结果
            self.t.write_back(case_id + 1, 9, test_result)  # 写入测试结果
            mylog.info("******第{}条用例执行完毕*******".format(case_id))







