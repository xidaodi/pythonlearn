'''

Python的文件操作

'''

import os,sys

fd=os.open("foo.txt",os.O_RDWR|os.O_CREAT)

d_fd=os.dup(fd)

os.write(d_fd,"jiyufuzhi".encode())

# result=os.read(fd,12)
#
# print(result)

os.closerange(fd,d_fd)

print("guanb")