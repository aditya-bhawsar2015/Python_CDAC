import numpy as np

a = np.array([6,2,12,4])
b = np.array([5,6,7,8])

l1 = [1,5,9,7]
l2 = [7,5,3,9]

print(a+b)   # adds elements in a and b
print(l1+l2)   # concatenate 2 lists

x = np.concatenate((a,b))    # concatenate 2 arrays
y = np.concatenate((l1,l2))
print(x)
print(y)


print(int(np.mean(a)))
print(np.median(a))
print(np.std(a))

from numpy import random

num = random.randint(100,size=7)  # generates random list of 3 elements
print(num)

num1 = random.choice([1,2,3,4,5,6])  # gives any one num as op
print(num1)


random.shuffle(a)       #shuffles the input array in any random order
print(a)