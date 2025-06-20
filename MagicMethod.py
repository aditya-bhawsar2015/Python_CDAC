class Employee:
    def __init__(self,empid,name,salary):
        self.empid = empid
        self.name = name
        self.salary = salary

    def __repr__(self):
        return "[Empid : "+ str(self.empid) + " Name : " + str(self.name) + " Salary : " +str(self.salary) + "]"


    def __eq__(self, other):
        if self.empid>other.empid:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.empid>other.empid:
            return True
        else:
            return False


    def __lt__(self, other):
        if self.empid<other.empid:
            return True
        else:
            return False

    def __add__(self, other):
        return self.salary+other.salary

e1 = Employee(5,"abc", 69000)
e2 = Employee(1, "mno" , 90000)



l = [e1,e2]
#l.reverse()
l.sort()
#l.sort() gives error bcoz it is unable to understand on what basis comparison is done?
print(e1+e2)

