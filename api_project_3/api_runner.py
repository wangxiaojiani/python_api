# -*- coding: utf-8 -*-
# Created by xj on 2019/3/10
import sys
import os
curpath=os.path.abspath(os.path.dirname(__file__)) #获取当前目录名称
rootpath=os.path.split(curpath)[0]  #获取当前目录的绝对路径后取到根路径
sys.path.append(rootpath) #python编译的系统路径中加入根路径
# os.path.append("./")  #这两种方法都行 老师用的

import unittest
import HTMLTestRunnerNew
from api_project_3.test_data import recharge_test_case, register_test_case,addloan_test_case,invest_test_case
from api_project_3.common import project_path


suite =unittest.TestSuite() #创建测试套件
loader= unittest.TestLoader() #创建loader对象
# suite.addTest(loader.loadTestsFromTestCase(HttpTest)) #加载用例
suite.addTest(loader.loadTestsFromModule(register_test_case)) #加载注册用例 因为注册类与充值类的类名相同，所以这里选择按照模块名的形式来加载用例
suite.addTest(loader.loadTestsFromModule(recharge_test_case)) #加载充值用例
suite.addTest(loader.loadTestsFromModule(addloan_test_case)) #加载加标用例
suite.addTest(loader.loadTestsFromModule(invest_test_case)) #加载投资用例

with open(project_path.test_report_path,"wb") as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f,verbosity=2,title="API测试报告",description="登录与注册的get请求用例",tester="xj")
    runner.run(suite)

