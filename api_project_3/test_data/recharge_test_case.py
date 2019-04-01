# -*- coding: utf-8 -*-
# Created by xj on 2019/3/10

import unittest
from api_project_3.common.http_request import HttpRequest
from api_project_3.common.do_excel import DoExcel
from ddt import ddt,unpack,data
from api_project_3.common import project_path
from api_project_3.common.my_log import MyLog
from api_project_3.common.get_data import GetData
from api_project_3.common.do_mysql import DoMysql

import re
from api_project_3.common.get_data import re_replace
test_data =DoExcel(project_path.test_data_path, "recharge").read_excel("RECHARGE")

mylog =MyLog()#日志实例化
# cookie =None
#>>>>>>思路：定义一个全局变量cookie 在函数内要去声明  在通过判断响应的cookie是否为空，如果不为空就把cookie重新赋值
#此外除了全局变量来设置cookie外还可以通过‘反射’来解决 --首先创建一个类 简历类属性cookie=None,然后利用setattr来修改属性值
@ddt
class HttpTest(unittest.TestCase):
    def setUp(self):
        print("开始执行用例啦")
        self.t=DoExcel(project_path.test_data_path,"recharge") #创建doexcel类的实例
    def tearDown(self):
        print("用例执行完毕啦")
    @data(*test_data)
    def test_2(self,case):
        global test_result_2
        # global cookie  #声明cookie为全局变量
        method = case["Method"]
        url = case["Url"]
        param =case["Params"]
        mylog.info("开始执行第{}条用例,用例的标题是{}".format(case["Case_id"],case["Title"]))
        mylog.info("测试数据为{}".format(case))
        if case['Sql'] !=None:
            first_money=DoMysql().do_mysql(eval(case['Sql'])['sql'],1)[0] #如果存在sql语句则在请求之前会进行查询
            setattr(GetData,"ADD_MONEY",first_money) #把查询到的结果反射
        param=re_replace(case["Params"])
        resp_t=HttpRequest(url,method,eval(param)).http_request(getattr(GetData,"cookie"))   #getattr(类名,"属性名") 来动态获取cookie
        if case['ExpectResult'].find('addmoney') !=-1:
            second_money=getattr(GetData,'ADD_MONEY') #获取数据库leaveamount的初始值
            final_money=second_money + int(eval(case['Params'])['amount']) #理论上的充值之后的结果
            expect_money=DoMysql().do_mysql(eval(case['Sql'])['sql'],1)[0] #在去数据库中查询到这个实际结果

        if resp_t.cookies: #判断响应的cookie是否为空，如果不为空，将cookie重新赋值
            # cookie =resp_t.cookies #将cookie重新赋值，下一次请求会应用到最新的cookie
            setattr(GetData,"cookie",resp_t.cookies) #利用setattr(类名，"属性名"，"修改后的值") 来动态修改cookie
        try:
            if case['Sql'] !=None and case['ExpectResult'].find('addmoney') !=-1:
                expect_result = case['ExpectResult'].replace('addmoney',str(expect_money))  # 将期望结果中的addmoney替换位数据库中的值
                case["ExpectResult"] =expect_result #将期望结果中的addmoney换成数据库中查询到的leaveamount
                self.assertEqual(final_money,expect_money) #计算出的结果与数据库结果比对    这里注意计算结果是期望结果，实际结果为数据库中查询到的结果
                self.assertEqual(eval(case['ExpectResult']),resp_t.json())  #这里用eval会报错，待解决
                self.t.updata_excel_amount(str(expect_money)) #将充值后的结果写入tel表
            else:
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










