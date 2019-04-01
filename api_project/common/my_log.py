# -*- coding: utf-8 -*-
# Created by xj on 2019/3/12

import logging
from common import project_path
class MyLog:
    def my_log(self,level,msg):
        logger =logging.getLogger("") #指定收集器名字
        logger.setLevel("DEBUG")#设置日志收集器级别
        if not logger.handlers:
            #设置日志输出格式
            formatter =logging.Formatter('[%(asctime)s]-[%(levelname)s]-[日志信息]:%(message)s')

            ch = logging.StreamHandler() #输出渠道默认为控制台
            ch.setLevel("DEBUG") #设置级别
            ch.setFormatter(formatter)

            fh =logging.FileHandler(project_path.test_log_path,encoding="utf-8")
            fh.setLevel("DEBUG") #设置文件渠道级别
            fh.setFormatter(formatter)

            logger.addHandler(ch) #渠道对接
            logger.addHandler(fh)
        if level =="DEBUG":
            logger.debug(msg)
        elif level=="INFO":
            logger.info(msg)
        elif level=="WARNING":
            logger.warning(msg)
        elif level =="ERROR":
            logger.error(msg)
        elif level=="CRITICAL":
            logger.critical(msg)
        else:
            print("你输入的级别有误")

    def debug(self,msg):
        self.my_log("DEBUG",msg)
    def info(self,msg):
        self.my_log("INFO",msg)
    def warning(self,msg):
        self.my_log("WARNING",msg)
    def error(self,msg):
        self.my_log("ERROR",msg)
    def critical(self,msg):
        self.my_log("CRITICAL",msg)

