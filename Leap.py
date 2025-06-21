year = int(input("Enter an year: "))

if(year%4 ==0) and (year%100 !=0):
    print("Year is leap")
elif (year%400 == 0) and (year%100 == 0):
    print("Year is leap")
else:
    print("non leap year")