a = int(input("Enter 1st num : "))
b = int(input("Enter 2nd num : "))
c = int(input("Enter 3rd num : "))

if(a>b) and (a>c):
    print(a, "is greatest")
elif (b>c):
    print(b, "is greatest")
else:
    print(c,"is greatest")