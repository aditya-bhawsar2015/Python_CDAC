from day6.Oop import Employee

e = Employee()

file = open('file.txt','w')
file.write(str(e))
file.close()