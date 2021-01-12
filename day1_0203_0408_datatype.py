import keyword
# -*- coding: UTF-8 -*-
#coding=utf-8

#以上两种编码方式会被执行


#print(keyword, keyword.kwlist)

'''
数据类型：数字
'''
# x=-7
# y=2
# z1=x/y
# z2=x//y  #向下取整
# print(z1,z2)
# print(type(z1),type(z2))
#del x,y



'''
数据类型：字符串
'''
# name="ruijun"
# print(name[0:3])
# print(name*2)
# print(name+"\tis good")
# print(name+'\n'+'I agree the above')
# if 'r' not in name:
#
#     print("%s is an excellent girl" %name)

'''
数据类型：列表
'''
# list0=["BJ","SH","TJ","CQ"]
# print(list0[0],list0[1:3])
# list1=["SZ"]
# list0.append("XA")
# list0[0]="CD"
# list2=list0+list1
# print(list0,list2)
#
# del list0[0]
# print(list0)
#
# list0.remove("TJ")
# print(list0)
#
# x=len(list0)
# y=max(list0)
# print(x,y)
# #list0.() 内置了各种针对列表操作的函数


'''
数据类型：元组
'''
# t1=("BJ","SZ","SH")
# t2=("XAN",)
# t3=t1+t2
# print(t3)
# x=len(t3)
# print(x)


'''
数据类型：字典
'''
# dic= {"name": "RJ", "age": "28", "sex": "female"}
# del dic["sex"]
# print(dic)
# dic["address"]="BJ"
# x=len(dic)
# print(dic)

'''
数据类型：集合，无序，不重复的元素序列
'''

myset={"bj","sh","tj"}
myset.add("cd")
print(myset)

myset.remove("cd")
print(myset)

myset.pop()
print(myset)

myset.update({"cd"})
print(myset)

print(len(myset))

print("bj" in myset)





