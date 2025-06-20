def oddEven(num):
    if num%2 ==0:
        return True
    else:
        return False

def fact(num):
    if num<=1:
        return 1
    else:
        return num * fact(num-1)

def prime(num):
    if num ==2:
        return True
    for i in range(2,(num//2)+1,1):
        if num%i ==0:
            return False
        else:
            return True

print(prime(2))


primelist = [i for i in range(2,101) if prime(i)]

print(primelist)

factlist = [fact(i) for i in range(1,6) ]

print(factlist)


# for i in range(2,101,1):
#     if prime(i):
#         primelist.append(i)
# else:
#     print(primelist)

oddEvenList = []

for i in range(1,101):
    if oddEven(i):
        oddEvenList.append(i)

print(oddEvenList)
