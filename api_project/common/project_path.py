# -*- coding: utf-8 -*-
# Created by xj on 2019/3/11

import os

#主项目路径
data_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]


#测试数据的路径
test_data_path=os.path.join(data_path,"test_data","API_TEST.xlsx")


#测试报告的路径
test_report_path=os.path.join(data_path,"Result","test_report","api_report.html")


#测试日志的路径
test_log_path =os.path.join(data_path,"Result","test_log","api.log")

#配置文件的目录
api_config_path=os.path.join(data_path,"test_data","api.conf")