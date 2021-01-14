
# 一个解释比较清晰的文档 https://www.jb51.net/article/166309.htm

import re


'''
示例：身份证号匹配
'''

str1="110102199809098762"     #18位身份证号
str2="1101021998090987"       #16位身份证号

#模式字符串
p1='^[1-9]\d{13,16}[0-9x]$'
p2='^[1-9]\d{14}(\d{2}[0-9x])?$'
p3='^([1-9]\d{16}[0-9x]|[1-9]\d{14})$'

m=re.match(p1,str1) #匹配对象

print(m,m.group(0))



'''
正则对象示例

'''
url="https://www.jb51.net/article/166309.htm"
pattern1=re.compile('http')
pattern2=re.compile('com')

#pattern.match():从起始位置开始匹配
print(pattern1.match(url))
print(pattern2.match(url))

#pattern.search():从任意位置开始匹配
print(pattern1.search(url))
print(pattern2.search(url))

