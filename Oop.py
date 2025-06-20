
#OBJECTS

class Employee:

    def __init__(self,empid = 1, name = "abc" , salary = 10000):    #default parameters
        self.empid = empid
        self.name = name
        self.salary = salary

    def printEmp(self):
        print("Empid : ",self.empid)
        print("Name : " , self.name)
        print("Salary : ", self.salary)


e = Employee()
e.printEmp()

e1 = Employee(2,"abc",11000)
e1.printEmp()

class Developer (Employee):

    def __init__(self,empid,name,salary):
        super().__init__(empid,name,salary)
        self.allowamce = salary*0.05

    def codewriting(self):
        print("Coder is Coding")

    def printEmp(self):
        super().printEmp()
        print("Allowance : ", self.allowamce)



d = Developer(1,"xyz",10000)
d.printEmp()

