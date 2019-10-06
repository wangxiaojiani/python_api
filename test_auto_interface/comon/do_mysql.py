# -*- coding: utf-8 -*-
#@Time      :2019/10/1    2:34
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :do_mysql.py
#@Software  :PyCharm
import pymysql
from test_auto_interface.comon.api_conf import MyConfig
class DoMysql:
    def do_mysql(self,query,flag=1):
        db_config=MyConfig().get_list('APP','db_config')
        cnn=pymysql.connect(**db_config)
        cur=cnn.cursor()
        cur.execute(query)
        if flag==1:
            res=cur.fetchone()
        else:
            res=cur.fetchall()
        cnn.close()
        return res
if __name__=='__main__':
    query = 'select Id,MobilePhone from Future.member where Id<=23528'
    s=DoMysql().do_mysql(query,2)
    print(s)

