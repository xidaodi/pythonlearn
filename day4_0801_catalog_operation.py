import os,sys


'''
判断某个文件是否存在，有 读 写 执行 权限
'''
# ret=os.access("foo.txt",os.F_OK)
#
# print("%s"%ret)
#
# ret=os.access("foo.txt",os.R_OK)
#
# print("%s"%ret)
#
# ret=os.access("foo.txt",os.W_OK)
#
# print("%s"%ret)
#
# ret=os.access("foo.txt",os.X_OK)
#
# print("%s"%ret)

'''
修改工作目录

'''

ret1=os.getcwd()

print("当前工作目录为： %s" %ret1)

path="/temp"

#修改工作目录

os.chdir(path)

ret2=os.getcwd()

print("当前工作目录为： %s" %ret2)


# os.chroot(path) 设置根目录








