

def divide():
    dividend = int(input("Enter Dividend : "))
    divisor = int(input("Enter Divisor : "))
    if(divisor==0):
        print("Cannot divide by Zero")
        divide()
    else:
        print(int(dividend/divisor))

# divide()

def numberFormat():
    number = input("enter number : ")
    if number.isnumeric():
        print("Correct")
    else:
        print("Not Correct, Try again")
        numberFormat()

numberFormat()

arr = [1,2,3,4,5]

def getIndex(arr):
    index = int(input("Enter desired position : "))
    if index < len(arr) and index >= -1*(len(arr)):
        print(arr[index])
    else:
        print("No element found")
        getIndex(arr)

# getIndex(arr)