
def find_max(a, b, c):
    if a>b  and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

print("The greatest of the three number is : ",find_max(a,b,c))