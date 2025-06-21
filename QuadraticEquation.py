a = int(input("Enter coefficient of x^2 :"))
b = int(input("Enter coefficient of x :  "))
c = int(input("Enter the constant value : "))

d = ((-b + (b**2 -(4*a*c)) **0.5 )/ 2*a)
e = ((-b - (b**2 -(4*a*c)) **0.5 )/ 2*a)

print("The roots are : " , d , "and" , e)