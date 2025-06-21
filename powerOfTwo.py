def powerOfTwo(power):
    for i in range(0,power+1):
        powers = 2**i
        print("The value of 2^" ,i ,"is: ", powers)

print(powerOfTwo(10))