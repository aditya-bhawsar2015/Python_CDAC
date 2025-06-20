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

    def __repr__(self):
        return "Empid :" +str(self.empid)+"  " + self.name + " "+str(self.basicSal)+" "



    def __eq__(self, other):
        return self.gross() == other.gross()

    def __le__(self, other):
        return self.gross() <= other.gross()

    def __ge__(self, other):
        return self.gross() >= other.gross()



e1 = Employee(1,"aa", 90000)
e2 = Employee(2, "bb", 99000)
e3 = Employee(3,"cc", 95000)
e4 = Employee(4, "dd", 96000)
e5 = Employee(5, "ee", 81000)

list = [e1,e2,e3,e4,e5]

print(list)

list.sort(key = lambda emp : emp.gross())
print(list)