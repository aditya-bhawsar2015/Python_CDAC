class Employee:
    def __init__(self,empid,name,basicSal):
        self.empid = empid
        self.name = name
        self.basicSal = basicSal
        self.hra= basicSal*0.5
        self.pt = 200
        self.pf = basicSal*0.12

    def gross(self):
        return self.basicSal + self.hra + self.pf + self.pt

    def netSal(self):
        return self.gross()-self.pf-self.pt

    def printEmployee(self):
        print("Empid : " ,self.empid, "Name : " ,self.name, "BasicSalary : ",self.basicSal, "Gross" ,self.gross())

    # def __repr__(self):
    #     return "[ Empid :" +str(self.empid) + ""


class Manager (Employee):
    def __init__(self, empid, name, basicSal):
        super().__init__(empid, name, basicSal)
        self.foodAllowance = self.basicSal*0.1
        self.managerAllowance = self.basicSal*0.05
        self.otherAllowance = self.basicSal*0.03

    def gross(self):
        return super().gross() + self.managerAllowance + self.foodAllowance+ self.otherAllowance

    # def printManager(self):
    #     super().printEmployee()
    #     print(self.managerAllowance , self.foodAllowance , self.otherAllowance, self.gross())


class marketingExecutive(Employee):
    def __init__(self ,empid, name, basicSal, distanceTravelled):
        super().__init__(empid,name,basicSal)
        self.phoneAllowance = 1500
        self.travelAllowance = 12*distanceTravelled

    def gross(self):
        return super().gross() + self.phoneAllowance + self.travelAllowance

    # def printMarketingExecutive(self):
    #     super().printEmployee()
    #     print(self.phoneAllowance , self.travelAllowance)

e= Employee(7,"mno",80000)
e1= Employee(7,"mno",80000)
e2= Employee(7,"mno",80000)
e.printEmployee()

me= marketingExecutive(5,"xyz",50000,18)
me1= marketingExecutive(5,"xyz",50000,18)
me2= marketingExecutive(5,"xyz",50000,18)
me.printEmployee()

m = Manager(1,"abc",100000)
m1 = Manager(1,"abc",100000)
m2  = Manager(1,"abc",100000)
m.printEmployee()

objectList  = [e,e1, me1,me2,m1,e2,m2,me,m]
managerList = []
empList = []
marketingExecutiveList = []
for i in objectList:
    if isinstance(i,Manager):
        empList.append(i.name)
    elif isinstance(i,marketingExecutive):
        managerList.append(i.name)
    else:
        marketingExecutiveList.append(i.name)



print("empList : ", empList)
print("managerList : ", managerList)
print("marketingExecutiveList : ", marketingExecutiveList)

