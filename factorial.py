def factorial(num):
    fact = 1
    for i in range(num,1,-1):
        fact = fact * i
    return fact

print(factorial(int(input("Enter a number : "))))
