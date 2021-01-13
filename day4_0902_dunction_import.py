import day4_0901_function_define as fuc
import sys

fuc.main()

# 打印模块搜索路径
print(sys.path)

#添加模块搜索路径
sys.path.append("....")

#另外windows也可以在系统的环境变量，python path里添加这个路径