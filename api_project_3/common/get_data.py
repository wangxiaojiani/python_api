# -*- coding: utf-8 -*-
# Created by xj on 2019/3/18
from api_project_3.common.api_conf import MyConfig
import re
class GetData:
    """类的反射可以动态查看，增加，删除，修改类或者实例的属性"""
    # cookie =None
    LOAN_ID =None #加标
    AMOUNT_NUM =0
    ADD_MONEY=0 #充值后的金额
    MOBILE_PHONE=0
    MEMBER_ID_LOAN=None#借款人
    MEMBER_ID_INVEST =None #投资人
    m_mobile=MyConfig().get_str('ADDLOAN','m_mobile') #加标的手机号
    member_id=MyConfig().get_str("ADDLOAN","memberid") #借款人的memberid
    pwd=MyConfig().get_str("ADDLOAN","pwd")
    t_mobile=MyConfig().get_str("RECHARGE","t_mobile") #充值人的手机号
    t_pwd=MyConfig().get_str("RECHARGE","t_pwd")#充值人的密码

def re_replace(target):#target 表示字典里读取的字符串
    p="#(.+?)#" #指定匹配模式
    while re.search(p,target):
        m=re.search(p,target)  #返回匹配对象
        key=m.group(1) #返回匹配到的参数化的key  这个key和getdata里定义的属性应保持一致
        value=getattr(GetData,key) #通过获取到的key来获取getdata属性值
        target=re.sub(p,value,target,count=1)  #将target里匹配到的值用value来替换 并赋予target
    return target




if __name__ == '__main__':
    # print(getattr(GetData,"cookie")) #查看属性值
    print(setattr(GetData,"cookie","1234")) #没有返回值，设置属性值
    print(getattr(GetData, "cookie"))
    print(hasattr(GetData,"cookie")) #判断是否有这个属性值
    print(delattr(GetData,"cookie")) #删除属性值

    # target2 = '{"mobilephone":"m_mobile","pwd":"pwd"}'
    # s=re_replace(target2)
    # print(s)