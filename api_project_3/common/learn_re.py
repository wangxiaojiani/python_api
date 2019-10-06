# # -*- coding: utf-8 -*-
# # Created by xj on 2019/3/25
import re
#
target ='{"mobilephone":"#13888888886#","pwd":"#123456#"}'

"""match  search  findall finditer sub
   正则匹配分为原义字符，元字符，限定字符

"""
p = "#(.+?)#" #如果这里不加？会按照最大限度进行匹配
v = re.search(p,target) #这里返回的是匹配到的表达式-》对象   没能匹配到就返回None  match 与seartch用法相同  只是match表示从头开始进行匹配 匹配到第一个就进行返回
print(v)
print(v.group()) #这里不传入参数表示匹配到的表达式
print(v.group(1)) #这里传入参数输入匹配到表达式里的第一个组  1，代表第一个
t=v.group(1)
w =re.findall(p,target) #用这种方式返回的是列表  每个列表中的元素代表所匹配到的组
print(w)
target1 ='{"mobilephone":"#username#","pwd":"#password#"}'

f=re.sub(p,'188899932',target1,count=1) #1888表示替换后的字符串，target表示要被替换的字符串 count表示被替换的次数
print(f)

s="{'memberId':#member_id#,'title':'借钱修别墅啦','amount':100000,'loanRate':18.0,'loanTerm':3,'loanDateType':0,'repaymemtWay':5,'biddingDays':5}"
v=re.search('#(.+?)#',s)
print(v.group(1))

# p='#(.+?)#'
# target2 ='{"mobilephone":"#username#","pwd":"#password#"}'
# while re.search(p,target2):
#     m=re.search(p,target2)
#     key=m.group(1)
#     getattr(Getdata,key)
#     target2=re.sub(p,value,target2,count=1)


#
s="123485678"
print(s[-2:-1])
