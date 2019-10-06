# -*- coding: utf-8 -*-
# Created by xj on 2019/3/21
import unittest
from api_project_3.common.http_request import HttpRequest
from api_project_3.common.do_excel import DoExcel
from ddt import ddt,unpack,data
from api_project_3.common import project_path
from api_project_3.common.my_log import MyLog
from api_project_3.common.get_data import GetData
from api_project_3.common import get_data
from api_project_3.common.do_mysql import DoMysql
from api_project_3.common.api_conf import MyConfig
import re
member_ID=MyConfig().get_list('ADDLOAN','member_ID')
test_data =DoExcel(project_path.test_data_path,"addloan").read_excel("ADDLOAN") #第一个addloan是sheet名，第二个是配置文件中的section
mylog =MyLog()#日志实例化
# cookie =None
#>>>>>>思路：定义一个全局变量cookie 在函数内要去声明  在通过判断响应的cookie是否为空，如果不为空就把cookie重新赋值
#此外除了全局变量来设置cookie外还可以通过‘反射’来解决 --首先创建一个类 简历类属性cookie=None,然后利用setattr来修改属性值
@ddt
class HttpTest(unittest.TestCase):
    def setUp(self):
        print("开始执行用例啦")
        self.t=DoExcel(project_path.test_data_path,"addloan") #创建doexcel类的实例
    def tearDown(self):
        print("用例执行完毕啦")
    @data(*test_data)
    def test_2(self,case):
        global test_result_2
        # global cookie  #声明cookie为全局变量
        method = case["Method"]
        url = case["Url"]
        mylog.info("开始执行第{}条用例,用例的标题是{}".format(case["Case_id"],case["Title"]))
        mylog.info("测试数据为{}".format(case))
        # if  case['Sql'] !=None:
        #     member_id =DoMysql().do_mysql(eval(case['Sql'])['sql_1'],1)[0] #从数据中获取member
        #     setattr(GetData,'MEMBER_ID_LOAN',member_id) #将memberid反射
        # if case['Params'].find('loanid') !=-1:#如果在参数中找到了loanid，则进行替换
        #     param=case['Params'].replace('loanid',str(getattr(GetData,'LOAN_ID')))
        # elif re.search('&(.+?)&',case['Params']):#通过正则来匹配参数化的memberid 后面投资模块也可用此方法
        #     param=re.sub('&(.+?)&',member_ID,case['Params'],count=1)

        # elif case['Params'].find('member_id') !=-1: #这个是利用参数化+反射方法来获取member_id
        #     param =case['Params'].replace('member_id',str(getattr(GetData,'MEMBER_ID_LOAN')))
        if case["Sql"] !=None:
            loan_id =DoMysql().do_mysql(eval(case['Sql'])['sql'],1) #返回的数据是元组 存储数据的时候最好根据索引去拿值
            setattr(GetData,'loanid',str(loan_id[0]))  #这里是通过索引来取loadid元组中的第一个loadid

        param=get_data.re_replace(case['Params'])   #参数化+正则+反射  一行代码解决问题
        # else:
        #     param =case["Params"]
        resp_t=HttpRequest(url,method,eval(param)).http_request(getattr(GetData,"cookie"))   #getattr(类名,"属性名") 来动态获取cookie
        # if case['Sql'] !=None: #如果sql语句不为空，则执行查询sql操作
        #     loan_id =DoMysql().do_mysql(eval(case['Sql'])['sql'],1) #返回的数据是元组 存储数据的时候最好根据索引去拿值
        #     setattr(GetData,'LOAN_ID',loan_id[0])  #这里是通过索引来取loadid元组中的第一个loadid
        if resp_t.cookies: #判断响应的cookie是否为空，如果不为空，将cookie重新赋值
            # cookie =resp_t.cookies #将cookie重新赋值，下一次请求会应用到最新的cookie
            setattr(GetData,"cookie",resp_t.cookies) #利用setattr(类名，"属性名"，"修改后的值") 来动态修改cookie
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












