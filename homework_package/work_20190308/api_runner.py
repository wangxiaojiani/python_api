# -*- coding: utf-8 -*-
# Created by xj on 2019/3/10
import unittest
import HTMLTestRunnerNew
from homework_package.work_20190308.test_case import HttpTest

suite =unittest.TestSuite() #创建测试套件
loader= unittest.TestLoader() #创建loader对象
suite.addTest(loader.loadTestsFromTestCase(HttpTest)) #加载用例

with open("api_report.html","wb") as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f,verbosity=2,title="API测试报告",description="登录与注册的get请求用例",tester="xj")
    runner.run(suite)