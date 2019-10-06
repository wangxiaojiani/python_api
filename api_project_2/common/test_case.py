# -*- coding: utf-8 -*-
# Created by xj on 2019/3/10

import unittest
from api_project_2.common.http_request import HttpRequest
from api_project_2.common.do_excel import DoExcel
from ddt import ddt,unpack,data
from api_project_2.common import project_path
from api_project_2.common.api_conf import MyConfig
from api_project_2.common.my_log import MyLog

button=MyConfig().get_list("SELECT","button")#从配置文件中读取指定用例
# test_data_2 =DoExcel(project_path.test_data_path, "Sheet1").read_excel(9,14) #对应登录的测试用例 也可以通过配置文件来修改
# test_data_1 =DoExcel(project_path.test_data_path, "Sheet1").read_excel(2,8)  #对应注册的测试用例
test_data =DoExcel(project_path.test_data_path, "Sheet1").read_excel(button)
test_data_tel=DoExcel(project_path.test_data_path,"Sheet2").read_excel_tel()

mylog =MyLog()#日志实例化
@ddt
class HttpTest(unittest.TestCase):
    def setUp(self):
        print("开始执行用例啦")
        self.t=DoExcel(project_path.test_data_path,"Sheet1")
        self.t_tel=DoExcel(project_path.test_data_path,"Sheet2")
    def tearDown(self):
        print("用例执行完毕啦")
    @data(*test_data)
    def test_2(self,case):
        global test_result_2
        params = eval(case["Params"])#将参数转换成字典格式
        if params["mobilephone"] in test_data_tel.keys():#判断excel中sheet1手机号多对应的电话号码是否是Sheet2表中tel
            old_tel = params["mobilephone"] #读取sheet1 注册的电话号码
            new_tel=str(test_data_tel[old_tel]) #将从sheet2表中读取的电话号码转化成字符串格式
            case["Params"]=case["Params"].replace(old_tel,new_tel) #手机号码替换
            new_tel_add =int(new_tel)+1 #手机号码+1
            self.t_tel.write_back(1,2,str(new_tel_add)) #返回的手机号码以字符串形式写入sheet2表中
            params = eval(case["Params"])#将params 重新赋值，以更新手机号
        else:
            mylog.info("手机号码未进行替换")
        mylog.info("开始执行第{}条用例,用例的标题是{}".format(case["Case_id"],case["Title"]))
        mylog.info("测试数据为{}".format(case))
        resp_t_2=HttpRequest(case["Url"],case["Method"],params).http_request()
        try:
            self.assertEqual(eval(case["ExpectResult"]),resp_t_2.json()) #判断期望结果与实际结果是否相等  为了安全起见这里用json字典格式做对比
            test_result_2="Pass" #如果没报错 执行结果为pass
        except Exception as e:
            mylog.error("报错了，报错信息为{}".format(e))
            test_result_2="Failed"#如果报错执行结果为failed
            raise e #注意要抛出异常否则用例会被执行
        finally:
            self.t.write_back(case["Case_id"]+1,8,resp_t_2.text) #写回实际结果 是要以字符串的方式进行写回的
            self.t.write_back(case["Case_id"],9,test_result_2) #写入测试结果
            mylog.info("=====第{}条用例结束======".format(case["Case_id"]))

    # @data(*test_data)
    # def test_1_get_register(self,case): #通过get请求来注册
    #     mylog.info("开始执行第{}条用例,用例的标题是{}".format(case["Case_id"], case["Title"]))
    #     resp_t = HttpRequest(case["Url"], case["Method"],eval(case["Params"])).http_request()  # 若想用post方法 直接将eval(param)改成data=eval(param)
    #     try:
    #         self.assertEqual(eval(case["ExpectResult"]),resp_t.json())  # 判断期望结果与实际结果是否相等  为了安全起见这里用json字典格式做对比
    #         result = "Pass"  # 如果没报错 执行结果为pass
    #     except Exception as e:
    #         mylog.error("报错了，报错信息为{}".format(e))
    #         result = "Failed"  # 如果报错执行结果为failed
    #         raise e  # 注意要抛出异常否则用例会被执行
    #     finally:
    #         self.t.write_back(case["Case_id"]+1,8,resp_t.text)  # 写回实际结果 是要以字符串的方式进行写回的
    #         self.t.write_back(case["Case_id"],9, result)  # 写入测试结果
    #         mylog.info("=====第{}条用例结束======".format(case["Case_id"]))










