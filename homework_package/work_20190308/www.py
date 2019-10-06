# # # # -*- coding: utf-8 -*-
# # # # Created by xj on 2019/3/10
# # # #这是doexcel类
# # # from openpyxl import workbook,load_workbook
# # # # #定义一个读去excel类#
# # # class Doexcel:
# # #     def __init__(self,filepath,sheetname):
# # #         self.filepath=filepath
# # #         self.sheetname =sheetname
# # #
# # #     def read_excel(self,button):
# # #         wb =load_workbook(self.filepath)
# # #         sheet=wb[self.sheetname]
# # #         test_data=[]
# # #         for i in range(2,sheet.max_row+1):
# # #             row_dict={}
# # #             row_dict["Case_id"] = sheet.cell(row=i,column=1).value
# # #             row_dict["Moudle"] =sheet.cell(row=i,column=2).value
# # #             row_dict["Params"] =sheet.cell(row=i,column=3).value
# # #             new_tel =self.read_excel_tel()
# # #             if sheet.cell(row=i,column=3).value.find('Tel') != -1:
# # #                 new_params=sheet.cell(row=i,column=3).value.replace('Tel',str(new_tel))
# # #                 self.update_excel_tel(new_tel+1)
# # #             else:
# # #                 new_params=sheet.cell(row=i,column=3).value
# # #             row_dict["Params"] =new_params
# # #             test_data.append(row_dict)
# # #         wb.close()
# # #         final_data=[]
# # #         if button =='all':
# # #             final_data = test_data
# # #         else:
# # #             for i in button:
# # #                 final_data.append(test_data[i-1])
# # #         return final_data
# # #     def write_back(self,row,column,value):
# # #         wb=load_workbook(self.filepath)
# # #         sheet=wb[self.sheetname]
# # #         sheet.cell(row,column).value=value
# # #         wb.save(self.filepath)
# # #         wb.close()
# # #     def creat_sheet(self):
# # #         wb=load_workbook(self.filepath)
# # #         wb.create_sheet(self.sheetname)
# # #         wb.save(self.filepath)
# # #
# # #     def read_excel_tel(self):
# # #         wb =load_workbook(self.filepath)
# # #         sheet=wb['Tel']
# # #         tel_num=sheet.cell(row=1,column=2).value
# # #         return tel_num
# # #     def update_excel_tel(self,value):
# # #         wb =load_workbook(self.filepath)
# # #         sheet=wb['tel']
# # #         sheet.cell(row=1,column=2).value=value
# # #         wb.save(self.filepath)
# # #
# # # #==这是配置类
# # # from configparser import ConfigParser
# # # class Myconfig:
# # #     def __init__(self,filepath):
# # #         self.wb =ConfigParser()
# # #         self.wb.read(filepath,encoding='utf-8')
# # #     def read_int(self,section,option):
# # #         return self.wb.getint(section,option)
# # #     def read_float(self,section,option):
# # #         return self.wb.getfloat(section,option)
# # #     def read_str(self,section,option):
# # #         return self.wb.get(section,option)
# # #     def read_list(self,section,option):
# # #         return eval(self.read_str(section,option))
# # #
# # #
# # # #设置一个读取MySQL的类
# # # import pymysql
# # #
# # # class Domysql:
# # #     def domysql(self,db_config,querty,flag=1):
# # #         db_config = {'host':"192.168.09.99",'port':3306,'username':'xiaoixia','password':123456,'database':'uftut'}
# # #         cn =pymysql.connect(**db_config)
# # #         cur=cn.cursor()
# # #         cur.execute(querty)
# # #         if flag ==1:
# # #             res=cur.fetchone() #返回的是元组
# # #         else:
# # #             res=cur.fetchall() #返回的是嵌套的元组
# # #         cur.execute('commit')
# # #         cur.close()
# # #         return res
# # #
# # # #设置一个日志类
# # # import logging
# # # class Mylog:
# # #     def mylog(self,level,msg):
# # #         logger = logging.getLogger("py14")
# # #         logger.setLevel("DEBUG")
# # #         if not logger.handlers:
# # #             formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-[日志信息]:%(message)s')
# # #             ch =logging.StreamHandler()
# # #             ch.setLevel("ERROR")
# # #             ch.setFormatter(formatter)
# # #             fh =logging.FileHandler('filename',encoding='utf-8')
# # #             fh.setLevel("ERROR")
# # #             fh.setFormatter(formatter)
# # #
# # #             logger.addHandler(ch)
# # #             logger.addHandler(fh)
# # #         if level =="DEBUG":
# # #             logger.debug(msg)
# # #         elif level =="ERROR":
# # #             logger.error(msg)
# # #         elif level=='INFO':
# # #             logger.info(msg)
# # #         elif level =='CRITICAL':
# # #             logger.critical(msg)
# # #         else:
# # #             print("你输入的级别错误")
# # #     def debug(self,msg):
# # #         self.mylog("DEBUG",msg)
# # #     def info(self,msg):
# # #         self.mylog('INFO',msg)
# # #
# # # #project path
# # #
# # # import os
# # # print(os.path.basename(__file__)) #返回当前文件名称
# # # print(os.path.abspath(os.path.basename(__file__))) #返回当前文件的绝对路径
# # # print(os.path.dirname(__file__)) #返回当前目录的绝对路径
# # # print(os.path.realpath(__file__)) #返回当前文件的决定路径
# # # print(os.path.split(os.path.realpath(__file__))) #返回元组
# # #
# # #
# # # #正则
# # import re
# #
# # target ='{"mobilephone":"#13888888886#","pwd":"#123456#"}'
# # p='#(.*?)#'
# # # v=re.search(p,target)
# # # v=re.match(p,target)
# # # print(v)
# # # print(v.group())
# # # print(v.group(1))
# #
# #
# # # w=re.findall(p,target) #返回的是列表，每个列表中的元素代表所匹配的的组数据
# # # print(w)
# # target1 ='{"mobilephone":"#username#","pwd":"#password#"}'
# # b=re.sub(p,'133322',target1,count=1)
# # print(b)
# #
# # while re.search(p,target1):
# #     m = re.search(p,target1)
# #     key=m.group(1)
# #     v=re.sub(p,getattr(GETDATA,key),target1,count=1)
# #
# # #测试的请求类
# # import requests
# #
# # class HttpRequest:
# #     def __init__(self,url,method,param):
# #         self.url=url
# #         self.method=method
# #         self.param=param
# #     def http_request(self,cookie):
# #         if self.method.upper()=='GET':
# #             try:
# #                 resp=requests.get(self.url,params=self.param,cookies=cookie)
# #             except Exception as e:
# #                 print("错误是{}".format(e))
# #         elif self.method.upper()=='post':
# #             try:
# #                 resp=requests.post(self.url,data=self.param,cookies=cookie)
# #             except Exception as e:
# #                 print("错误是{}".format(e))
# #         else:
# #             print("你输入的请求方式不挣")
# #             resp=None
# #         return resp
# #
# # #runner 脚本
# #
# # import unittest
# # from HTMLTestRunnerNew import HTMLTestRunner
# #
# # suit = unittest.TestSuite()
# # loader =unittest.TestLoader()
# # suit.addTest(loader.loadTestsFromModule(moudle))
# # with open(filepath,'wb') as f:
# #     runer=HTMLTestRunner(title="zhuti",description="描述",tester="xiiajia",verbosity=2,stream=f)
# #     runer.run(suit)
# # #测试类
# # import unittest
# # from ddt import ddt,unpack,data
# # # -*- coding: utf-8 -*-
# # # Created by xj on 2019/3/18
# #
# # import unittest
# # from api_project_3.common.http_request import HttpRequest
# # from api_project_3.common.do_excel import DoExcel
# # from ddt import ddt,unpack,data
# # from api_project_3.common import project_path
# # from api_project_3.common.api_conf import MyConfig
# # from api_project_3.common.my_log import MyLog
# #
# # # button=MyConfig().get_list("SELECT","button")#从配置文件中读取指定用例
# # test_data =DoExcel(project_path.test_data_path, "register").read_excel("REGISTER")
# #
# #
# # mylog =MyLog()#日志实例化
# # cookie =None #思路：定义一个全局变量cookie 在函数内要去声明  在通过判断响应的cookie是否为空，如果不为空就把cookie重新赋值
# # @ddt
# # class HttpTest(unittest.TestCase):
# #     def setUp(self):
# #         print("开始执行用例啦")
# #         self.t=DoExcel(project_path.test_data_path,"register")
# #     def tearDown(self):
# #         print("用例执行完毕啦")
# #     @data(*test_data)
# #     def test_2(self,case):
# #         global test_result_2
# #         global cookie  #声明cookie为全局变量
# #         method = case["Method"]
# #         url = case["Url"]
# #         param =case["Params"]
# #         mylog.info("开始执行第{}条用例,用例的标题是{}".format(case["Case_id"],case["Title"]))
# #         mylog.info("测试数据为{}".format(case))
# #         resp_t=HttpRequest(url,method,eval(param)).http_request(cookie)
# #         if resp_t.cookies: #判断响应的cookie是否为空，如果不为空，将cookie重新赋值
# #             cookie =resp_t.cookies #将cookie重新赋值，下一次请求会应用到最新的cookie
# #         try:
# #             self.assertEqual(eval(case["ExpectResult"]),resp_t.json()) #判断期望结果与实际结果是否相等  为了安全起见这里用json字典格式做对比
# #             test_result_2="Pass" #如果没报错 执行结果为pass
# #         except Exception as e:
# #             mylog.error("报错了，报错信息为{}".format(e))
# #             test_result_2="Failed"#如果报错执行结果为failed
# #             raise e #注意要抛出异常否则用例会被执行
# #         finally:
# #             self.t.write_back(case["Case_id"]+1,9,str(resp_t.json())) #写回实际结果 是要以字符串的方式进行写回的
# #             self.t.write_back(case["Case_id"]+1,10,test_result_2) #写入测试结果
# #             mylog.info("=====第{}条用例结束======".format(case["Case_id"]))
#
# #
# # test_data=DoExcel(filename，sheetname)
# # @ddt
# # class httptest(unittest.Testcase):
# #     def setUp(self):
# #         print("---开始执行用例了----")
# #     def tearDown(self):
# #         print("=---用例执行完毕啦---")
# #     @data()
# #     def test_register(self):
#
from suds.client import Client
user_url_1="http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
print(user_url_1)
# user_url_2 = "http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
client_1 = Client(user_url_1)
t_1={'client_ip':'110.10.113.119','tmpl_id':'1','mobile':'13211228889'}
try:
    result_1=client_1.service.sendMCode(t_1)
    print(result_1)
except Exception as e:
    print(111)
    # print(e.fault.faultstring)
    print(e.fault)
    print(222)

# client_2=Client(user_url_2)
# t_2={'channel_id':'2','ip':'129.45.6.8','mobile':'13311228889','pwd':'123456','user_id':'k99018','verify_code':'537519'}
# result_2=client_2.service.userRegister(t_2)
# print(result_2)
# user_url_3='http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl'
# client_3=Client(user_url_3)
# print(client_3)
# t_3={'uid':'100007063','true_name':'反射','cre_id':'eexxxxxxxxxxxxx'}
# result_3=client_3.service.verifyUserAuth(t_3)
# print(result_3)
"""
# 1.在线安装pip install suds.jurko
# 2.引入suds库，from suds.client import Client
# 3.创建webservice对象  client=Client(URL)
# 4.打印这个client中所有接口信息 print(client)
# 5.用soapui来查看某个接口的组成和参数
# 6.将参数当作字典存储t
# 7.在python中调用这个接口 result=client.service.userRegister(t)
# 8打印响应结果
# """


# import time
# s=time.strptime("2018-09-02 09:09:43",'%Y-%m-%d %H:%M:%S')
# print(s) #转换成时间数组
# v=time.mktime(s)
# print(v)
# import datetime
# print(datetime.datetime.now())