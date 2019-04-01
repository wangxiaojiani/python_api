# -*- coding: utf-8 -*-
# Created by xj on 2019/3/18

import unittest
from api_project_3.common.http_request import HttpRequest
from api_project_3.common.do_excel import DoExcel
from ddt import ddt,unpack,data
from api_project_3.common import project_path
from api_project_3.common.api_conf import MyConfig
from api_project_3.common.my_log import MyLog

# button=MyConfig().get_list("SELECT","button")#从配置文件中读取指定用例
test_data =DoExcel(project_path.test_data_path, "register").read_excel("REGISTER")


mylog =MyLog()#日志实例化
cookie =None #思路：定义一个全局变量cookie 在函数内要去声明  在通过判断响应的cookie是否为空，如果不为空就把cookie重新赋值
@ddt
class HttpTest(unittest.TestCase):
    def setUp(self):
        print("开始执行用例啦")
        self.t=DoExcel(project_path.test_data_path,"register")
    def tearDown(self):
        print("用例执行完毕啦")
    @data(*test_data)
    def test_2(self,case):
        global test_result_2
        global cookie  #声明cookie为全局变量
        method = case["Method"]
        url = case["Url"]
        param =case["Params"]
        mylog.info("开始执行第{}条用例,用例的标题是{}".format(case["Case_id"],case["Title"]))
        mylog.info("测试数据为{}".format(case))
        resp_t=HttpRequest(url,method,eval(param)).http_request(cookie)
        if resp_t.cookies: #判断响应的cookie是否为空，如果不为空，将cookie重新赋值
            cookie =resp_t.cookies #将cookie重新赋值，下一次请求会应用到最新的cookie
        try:
            self.assertEqual(eval(case["ExpectResult"]),resp_t.json()) #判断期望结果与实际结果是否相等  为了安全起见这里用json字典格式做对比
            test_result_2="Pass" #如果没报错 执行结果为pass
        except Exception as e:
            mylog.error("报错了，报错信息为{}".format(e))
            test_result_2="Failed"#如果报错执行结果为failed
            raise e #注意要抛出异常否则用例会被执行
        finally:
            self.t.write_back(case["Case_id"]+1,9,str(resp_t.json())) #写回实际结果 是要以字符串的方式进行写回的
            self.t.write_back(case["Case_id"]+1,10,test_result_2) #写入测试结果
            mylog.info("=====第{}条用例结束======".format(case["Case_id"]))











