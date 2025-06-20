class Employee:
    def hello(self):
        print("hello Employee")


class Dev(Employee):
    def hello(self):
        print("Hello Dev")

class Test(Employee):
    def hello(self):
        print("hello test")

class DevTest(Dev, Test):
    def placeHolder(self):
        pass

    def hello(self):
        Test.hello(self)
e = Employee()
d = Dev()
t= Test()
dt = DevTest()

e.hello()
d.hello()
t.hello()
dt.hello()