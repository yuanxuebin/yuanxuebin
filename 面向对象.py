# class Employee:
#     pay_raist_amount = 1.2                                                     #声明一个类的变量
#     def __init__(self,first,last,pay,domain="funcat.com"):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first+last+"@"+domain
#     def fullname(self):                                                          #创建一个方法
#         print(self.first+self.last+self.email)
#
#     def jiaxin1(self):
#         return self.pay * self.pay_raist_amount
#     def jiaxin2(self):
#         return self.pay * Employee.pay_raist_amount
#
# emp1 = Employee("xiaoming","wang",10000,"xinlang.com")
# emp2 = Employee("xiaohong","zhang",20000,"baidu.com")
# Employee.pay_raist_amount=1.3
# emp1.pay_raist_amount=1.5
# print(emp1.jiaxin1())
# print(emp1.jiaxin2())
# emp1.fullname()
# emp2.fullname()
class Employee:
    name="xiaoming"
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay = pay

    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def setName(self,name):
        self.first,self.last = name.split(' ')

    @staticmethod
    def printemail():
        print("email",Employee.name+"@domain.com")

    def __repr__(self):
        return "fullname:{},pay:{}".format(self.fullname,self.pay)

class Manager(Employee):
    employess = []

    def __init__(self,first,last,pay,emp):
        Employee.__init__(self,first,last,pay)
        self.employess = emp

    def delete(self,fullname):
        empss = self.employess
        # 根据姓名 删除 其中的一个成员
e1 = Employee('xiao','wang',7000)
e2 = Employee('xiao','hong',8000)
e3 = Employee('xiao','ming',9000)

print(repr(e1))





