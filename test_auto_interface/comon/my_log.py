# -*- coding: utf-8 -*-
#@Time      :2019/9/30    20:48
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :my_log.py
#@Software  :PyCharm
import logging
from test_auto_interface.comon.my_path import current_log_dir_path
import time
class MyLog:
    #日志类
    def __init__(self,name):
        """
        :param name: 日志收集器名称
        """
        self.name=name
    def my_log(self,level,msg):
        logger =logging.getLogger(self.name)
        logger.setLevel('DEBUG')
        Formater=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-[日志信息]:%(message)s')
        if not logger.handlers:
            ch =logging.StreamHandler()
            ch.setLevel('DEBUG')
            ch.setFormatter(Formater)
            now_time = time.strftime ('%Y-%m-%d')  # 获取当前时间 年月日
            file=current_log_dir_path +r'\test_api_'+ now_time + '.txt'
            fh=logging.FileHandler(file,encoding='utf-8')
            fh.setLevel('DEBUG')
            fh.setFormatter(Formater)
            logger.addHandler(ch)
            logger.addHandler(fh)
            if level == 'DEBUG':
                logger.debug(msg)
            elif level =='INFO':
                logger.info(msg)
            elif level == 'WARNING':
                logger.warning(msg)
            elif level =='ERROR':
                logger.error(msg)
            elif level =='CRITICAL':
                logger.critical(msg)
    def debug(self,msg):
        self.my_log('DEBUG',msg)
    def info(self,msg):
        self.my_log('INFO',msg)
    def warning(self,msg):
        self.my_log('WARNING',msg)
    def error(self,msg):
        self.my_log('ERROR',msg)
    def critical(self,msg):
        self.my_log('CRITICAL',msg)

if __name__=='__main__':
    MyLog('MM').debug('你是真的都')

