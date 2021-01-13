
# 如果这个类没有参数
class MyClass:

    #成员变量
    age=None
    name=None

    #成员函数
    def get_age(self):

        print(self.age)
        return self.age

    def set_age(self,age):
        self.age=age
        print(age)


#如果这个类有参数
class MyClass2:
    def __init__(self,age):
        self.age=age

    def get_age(self):
        print(self.age)

'''

公有成员变量/函数：公有成员：对所有人公开，可以在类的外部直接访问，默认
私有成员变量/函数（__xx）:双下划线开始，无双下划线结束；类的外部不能直接访问，需要调用类的公开成员方法访问；
保护成员变量/函数（_xxx）：不能通过“from module import”的方式导入；
特殊成员函数（__xxx__(self)）:双下划线开始+双下划线结束，系统定义的特殊函数，不能在类外部访问

'''

# 基类
class MyClass3:

    #初始化函数
    def __init__(self,age,name,job):
        self.age=age          #公有成员
        self._name=name       #保护成员
        self.__job=job        #私有成员
        print("BaseClass initial finished")



    #公有成员函数
    def get_age(self):
        print(self.age)
        return self.age

    #保护成员函数
    def _get_name(self):
        print(self._name)
        return self._name

    #私有成员函数
    def __get_job(self):
        return self.__job

# 派生类
class DriverdMyClass(MyClass3):

    def __init__(self,age,name,job,num):
        MyClass3.__init__(self,age,name,job)
        self.num=num
        print("DriverdClass initial finished")

    def get_age(self):
        print("DriverdClass get age: %d"%self.age)


'''
基类demo
'''
# def main():
#
#     mycls=MyClass3(28,"Ruijun","pts")
#
#     mycls.get_age()
#     print(mycls._name)   #访问保护成员变量
#     # print(mycls.__job)   #访问私有成员变量，会报错
#
#     mycls._get_name()    #访问保护成员函数
#
#     # mycls.__get_job()   #访问私有成员函数

'''
派生类demo
'''
def main():

    mycls=DriverdMyClass(28,"Ruijun","pts","1001")
    mycls.get_age() #重载

    print(mycls._name)
    mycls._get_name()



if __name__ == '__main__':
    main()