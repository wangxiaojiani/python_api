# -*- coding: utf-8 -*-
# Created by xj on 2019/3/9
import logging

class MyLog:
    def read_conf(self,LEVEL,MSG):
        my_log=logging.getLogger('py14')
        my_log.setLevel('DEBUG')

        if not my_log.handlers:

            ch = logging.StreamHandler()
            ch.setLevel('DEBUG')

            fh=logging.FileHandler('mm.log',encoding='utf-8')
            fh.setLevel('DEBUG')

            my_log.addHandler(ch)
            my_log.addHandler(fh)

        if LEVEL =='DEBUG':
            my_log.debug(MSG)
        elif LEVEL =='INFO':
            my_log.info(MSG)
        elif LEVEL =='WARNING':
            my_log.warning(MSG)
        elif LEVEL=='ERROR':
            my_log.error(MSG)
        else:
            my_log.critical(MSG)

    def debug(self,msg):
        self.read_conf('DEBUG',msg)
    def info(self,msg):
        self.read_conf('INFO',msg)
    def warning(self,msg):
        self.read_conf('WARNING',msg)
