'''
顺序语句示例
'''

# print("顺序语句")
#
# def fun():
#     print("have fun today")
#
# def main():
#     fun()
#
# if __name__=='__main__':
#     main()

'''
条件语句示例
'''
# num=int(input("please input a number"))
#
# if num==2:
#     print("we found it !")
# else:
#     print("where is 2 ?")


'''
循环语句示例
'''

#在python中没有 do....while循环


# 1， while...else...一般情况下不推荐
# j=0
# count=10
# while j < 10:
#     print(j)
#     j+=1


# 2, for..else..
num=[1,2,3,4,5]
index=0
for index in range(len(num)):
    print(num[index])
    if index==3:
        break









