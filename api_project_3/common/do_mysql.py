# -*- coding: utf-8 -*-
# Created by xj on 2019/3/20
import pymysql #这里导入的是pymysql模块  也可以安装python-connnect-python包
from api_project_3.common.api_conf import MyConfig
#pymsql mysql-connector-python
#pip install pymysql
#pip install mysql-connector-python
class DoMysql:
    def do_mysql(self,query,flag):

        """首先将数据库IP，端口，用户名，密码，数据库名称保存在字典中(已经放在配置文件)
         query 代表要执行的sql 语句，flag=1获取一条数据，flag！=1 获取多条数据，这里返回的数据都是元组"""
        #获取数据库信息
        db_config = MyConfig().get_list('MYSQLDB','db_config')
        #建立数据库连接
        cnn=pymysql.connect(**db_config) #将数据库信息以字典的方式传进来
        #建立游标
        cursor =cnn.cursor()
        #执行sql语句
        cursor.execute(query)
        #***如果做的的增加，插入，删除操作 还要进行数据的提交***
        # cursor.execute('commit')
        if flag ==1:
        #返回结果
            res=cursor.fetchone()#查询匹配到的第一条数据 元组类型
        else:
            res = cursor.fetchall()#返回的结果是元组 里面嵌套的是元祖，每一个元组是一条查询数据 **这里需要注意的数利用mysql-connect-jar包安装的插件这种方式返回的是列表
        cnn.close() #关闭数据库连接
        return res

if __name__ == '__main__':
    query = 'select Id,MobilePhone from member where Id<=23528'
    res=DoMysql().do_mysql(query,2)
    print(res)