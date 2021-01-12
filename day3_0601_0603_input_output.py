

#格式化输出1

# age=28
#
# pi=3.223455
#
# print("ruijun's age is : %.2f" %pi)

#格式化输出2：  "".format() 函数
# age=28
# height=166.889
# print("ruijun's age is {0} years old, height is {1:.2f} cm".format(age,height))

'''
当文件作为输入对象
'''

#文件打开，用open(filaname,mode)函数,默认以只读模式打开
# file=open("hello.txt","r")
# file.close()

#文件写入 write()
# file=open("hello.txt","a+")
# file.write("hello\npython")
# file.close()

#文件写入 writelines()
# data=["this is","a test"]
# file=open("hello.txt","a+")
# # for line in data:
# #     file.writelines([line+"\n"])
# file.writelines([line+"\n" for line in data])
# file.close()

#文件读取：read()
# file=open("hello.txt","r")
# context=file.read()
# print(context)
# file.close()

#文件读取：readline()
# file=open("hello.txt","r")
# context=file.readline()
# print(context)
# file.close()


#文件读取：readlines()
file=open("hello.txt","r")
context=file.readlines()
print(context)
file.close()








