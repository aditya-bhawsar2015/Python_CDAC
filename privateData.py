

class Demo :
    def __init__(self, first,second):
        self.first = first
        self.__second = second

    def __getmethod(self, name, id):
        self.name = name
        self.id = id



d = Demo(10,20)
print(d.first)
print(d._Demo__second)
print(d._Demo__getmethod("abc", 11))