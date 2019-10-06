# -*- coding: utf-8 -*-
#@Time      :2019/10/2    0:24
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :runner.py
#@Software  :PyCharm

import unittest
from test_auto_interface.comon.my_path import test_report_path
import time
from HTMLTestRunnerNew import HTMLTestRunner
from test_auto_interface.test_data.login_test import TestHttpRequest
suit=unittest.TestSuite()
loader=unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
now=time.strftime('%y-%m-%d')
path=test_report_path+'_'+now +'.html'
with open(path,'wb+') as f:
    runner=HTMLTestRunner(stream=f,description='afa',verbosity=2,title='dad',tester='xx')
    runner.run(suit)