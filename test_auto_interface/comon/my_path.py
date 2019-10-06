# -*- coding: utf-8 -*-
#@Time      :2019/9/30    20:58
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :my_path.py
#@Software  :PyCharm

import os

#当前文件所在目录
current_dir_path=os.path.dirname(__file__)

#项目工程目录
current_pro_path=os.path.split(current_dir_path)[0]

#日志输出路径文件夹路径
current_log_dir_path=os.path.join(current_pro_path,r'result',r'test_log')

#配置文件所在目录
current_conf_path=os.path.join(current_pro_path,r'test_conf',r'api.conf')

#测试用例所在路径
test_data_path=os.path.join(os.path.split(current_pro_path)[0],r'api_project_3\test_data\API_TEST.xlsx')

#测试报告路径
test_report_path=os.path.join(current_pro_path,r'result',r'test_result')
