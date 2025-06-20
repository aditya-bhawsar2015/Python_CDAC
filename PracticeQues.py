from functools import reduce

li = [27,56,78,92,34,51]
a = 50
list2 = []
def func(li):
    for i in li:
        if(i>a):
            list2.append(i)

func(li)
print(list2)

o = list(filter(lambda a : a>50, li))

print(o)
def square(a):
    return a*a


x = list(map(square,li))

print(x)

listString = ["abc" , "bcd" , "cde", "def" , "efg"]

def upp(s):
    return str(s).upper()

y = list(map(upp , listString))

print(y)

x = list(map(lambda a:a*a,li))

print(x)

m = list(map(lambda  s: str(s).upper(),listString))

print(m)


# lambda taking 2 parameters
x = [12,25,64,71,34,82]
y = [62,21,74,27,34,91]
q = [72,88,91,29,19,11]

z = list(map(lambda a,b : a*b, x,y))

print(z)

r = list(map(lambda a,b,c:a+b+c , x,y,q))

print(r)

n = filter(lambda a : a>40, li)

print(list(n))

j = reduce(lambda a,b: a+b , q)

print(j)

def add(a,b):
    return a+b

k = reduce(add,y)
print(k)
