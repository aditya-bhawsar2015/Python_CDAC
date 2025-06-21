#Using temp

x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))

# temp = x
# x = y
# y = temp
#
# print("After swap the values are : ", x , "and" , y)

# Without using 3rd variable

x = x-y
y = x+y
x = y-x

print("Now " , x , "and" , y)