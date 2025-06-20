# write a function to add n numbers
print("============Function to add n number============")


def summition(*number):
    sum1 = 0
    for i in number:
        sum1 = sum1 + i
    print(sum1)


summition(2, 3)
summition(2, 3, 4, 5)
summition(23, 45, 78)


# funtion to take two parameters list and integer and new list creation after nth element

def replaceList(mylist, n):
    x=0
    newlist=[]
    while x < int(len(mylist)/n):
        newlist.append( mylist[x*n:(x+1)*n:])
        x=x+1
    # else:
    #     newlist.append(mylist[x*n::])
    return newlist

mylist = [1, 2, 3, 4, 5, 6]
n = 2
print(replaceList(mylist, n))

#append two list

c=[]
a=["hero","maruti"]
b=["honda","suzuki"]
for i in range(len(a)):
    c.append(a[i]+" "+b[i])
print(c)
# for i , j in zip(a, b):
#     c.append("".join(i+j))
# print(c)

#function to seperate element
mylist=[i for i in range(1,100)]

def threelist (myList) :
    oddList = [i for i in myList if i % 2 != 0]
    evenList = [i for i in myList if i%2 ==0]
    if mylist.count(2) >= 1:
        primelist = [2]
        for i in oddList:
            if prime(i):
                primelist.append(i)

    else:
        primelist = [i for i in oddList if prime(i)]
    print(oddList)
    print(evenList)
    print(primelist)
def prime(i):
    for j in range(3,i):
        if i%j==0 :
            return False
    else:
        if i == 1:
            return False
        else:
            return True

threelist(mylist)
