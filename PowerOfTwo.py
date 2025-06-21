n = int(input("Enter a value till which power of two is required : "))

val = list(map( lambda x : 2**x , range(n+1) ))

print("The power of 2 in range 0 to",n, "is")
for i in range(n):
    print("2 to the power " ,i, "is : ", val[i])