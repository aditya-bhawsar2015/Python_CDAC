Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = int(input("Enter a number : "))
Enter a number : 8
for i in range(1,1<8,-1)
SyntaxError: expected ':'
for i in range(1,a+1,1):




     
KeyboardInterrupt
a = [1,2,3,4,5]
print(a)
[1, 2, 3, 4, 5]
a[1]
2
a[-5]
1
for i in range(0,len(a))
SyntaxError: expected ':'
for i in range(0,len(a)):
    print(a[-1])

    
5
5
5
5
5
for i in range(-1,-len(a),-1):
    print(a[i])

    
5
4
3
2
for i in range(-1,-len(a)-1,-1):
    print(a[i])

    
5
4
3
2
1
for i in range(-1,-len(a)-1,-1):
    print(a[-1:-5])

    
[]
[]
[]
[]
[]
for i in range(1,len(a)+1,1):
    print(a[-i])

    
5
4
3
2
1
for i in range(len(a)-1,1,-1):
    print(a[i])

    
5
4
3
for i in range(len(a)-1,-1,-1):
    print(a[i])

    
5
4
3
2
1
print(a[1:5])
[2, 3, 4, 5]
print(a[-1:-4])
[]
print(a[-4:-1])
[2, 3, 4]
a.append(6)
list(a)
[1, 2, 3, 4, 5, 6]
a[0:5:2]
[1, 3, 5]
a[::]
[1, 2, 3, 4, 5, 6]
a[0,6,3]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a[0,6,3]
TypeError: list indices must be integers or slices, not tuple
a[0:6:3]
[1, 4]
a.append(7,8,9)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.append(7,8,9)
TypeError: list.append() takes exactly one argument (3 given)
a[-5:0]
[]
a[::-1]
[6, 5, 4, 3, 2, 1]
a[0::-1]
[1]
a[:-4:-1]
[6, 5, 4]
a[0:-4:-1]
[]
a[0:-4]
[1, 2]
a[0:-4:1]
[1, 2]
a[-4:0:-1]
[3, 2]
a= [10,20,30,40]
b= [50,60,70]
print(a+b)
[10, 20, 30, 40, 50, 60, 70]
for i in range(0,len(a+b),1):
    if(i%2==1):
        print(a[i])

        
20
40
Traceback (most recent call last):
  File "<pyshell#54>", line 3, in <module>
    print(a[i])
IndexError: list index out of range
c=[10, 20, 30, 40, 50, 60, 70]
for i in range(0,len(c),1):
    if(i%2==1):
        print(c[i])

        
20
40
60
for i in c:
    fact = 1
    for j in range(1,i):
        fact *= j
    print(fact)

    
362880
121645100408832000
8841761993739701954543616000000
20397882081197443358640281739902897356800000000
608281864034267560872252163321295376887552831379210240000000000
138683118545689835737939019720389406345902876772687432540821294940160000000000000
171122452428141311372468338881272839092270544893520369393648040923257279754140647424000000000000000
for i in c:
    fact = 1
    for j in range(0,i):
        fact *= j
    print(fact)

    
0
0
0
0
0
0
0
for i in c:
    fact = 1
    for j in range(1,i+1):
        fact *= j
    print(fact)

    
3628800
2432902008176640000
265252859812191058636308480000000
815915283247897734345611269596115894272000000000
30414093201713378043612608166064768844377641568960512000000000000
8320987112741390144276341183223364380754172606361245952449277696409600000000000000
11978571669969891796072783721689098736458938142546425857555362864628009582789845319680000000000000000
a=[37,90,88,79,71]
for i in range(0,len(a)):
    for j in range(2,i+1):
        if(a[i]%j ==0):
            print(a[i] , "is a prime no")

            
88 is a prime no
b=[79, 71, 30, 22 , 88]
b=[79, 71, 37, 90 , 88]
for i in range(0,len(a),1):
    for j in range(0,len(b),1):
        if (a[i] == b[j]):
            print("Lists are equal")
         else:
             
SyntaxError: unindent does not match any outer indentation level
b=[79, 71, 37, 90 , 88]for i in range(0,len(a),1):
    for j in range(0,len(b),1):
        if (a[i] == b[j]):
            print("Lists are equal")
         else
         
SyntaxError: invalid syntax
b=[79, 71, 37, 90 , 88]
for i in range(0,len(a),1):
    for j in range(0,len(b),1):
        if (a[i] == b[j]):
            print("Lists are equal")
         else
         
SyntaxError: multiple statements found while compiling a single statement
a=[37,90,88,79,71]
b=[79,71,37,90,88]
for i in range(0,len(a),1):
    for j in range(0,len(b),1):
        if (a[i] == b[j]):
            print("Lists are equal")
         else :
             
SyntaxError: unindent does not match any outer indentation level
a=[37,90,88,79,71]
b=[79,71,37,90,88]
for i in range(0,len(a),1):
    for j in range(0,len(b),1):
        if (a[i] == b[j]):
            print("Lists are equal")
        else :
            
SyntaxError: multiple statements found while compiling a single statement
a=[37,90,88,79,71]
b=[79,71,37,90,88]
for i in range(0,len(a),1):
    for j in range(0,len(b),1):
        if (a[i] == b[j]):
            print("Lists are equal")
        else :
            
SyntaxError: multiple statements found while compiling a single statement
a=[10,20,30]
b=[30,10,20]
for i in range(0,len(a),1):
    for j in range(0,len(b),1):
        if(a[i]==b[j]):
            print("Equal Lists")
        else:
            print("Unequal Lists")

            
Unequal Lists
Equal Lists
Unequal Lists
Unequal Lists
Unequal Lists
Equal Lists
Equal Lists
Unequal Lists
Unequal Lists
a=[10,20,30]
b=[30,10,20]
for i in range(0,len(a),1):
    for j in range(0,len(b),1):
        if(a[i]==b[j]):
            print(a[i])
            
SyntaxError: multiple statements found while compiling a single statement
a=[10,20,30]
b=[30,10,20]
for i in range(0,len(a),1):
    for j in range(0,len(b),1):
        if(a[i]==b[j]):
            print(a[i])
a=[10,20,30]
b=[20,30,10]
b.sort()
b
[10, 20, 30]
if(a[i]==b[i]):
    print(a)

    
[10, 20, 30]
x=[10,30,54,77]
y=[77,20,60,54]
if(a==b):
    print(a)
    
SyntaxError: multiple statements found while compiling a single statement
x=[30,40,50,60]
y=[22,32,42,52]
if(len(x)!=len(y)):
    print ("Lists not equal")
else:
    for i in a
    
SyntaxError: expected ':'
x=[30,40,50,60]
y=[22,32,42,52]
z=[]
if(len(x)!=len(y)):
    print ("Lists not equal")
else:
    for i in a 
KeyboardInterrupt
a = [66,49,73,97,82,29]
a.append(12)
a
[66, 49, 73, 97, 82, 29, 12]
a.insert(2,34)
a
[66, 49, 34, 73, 97, 82, 29, 12]
a.pop()
12
a.pop()
29
a.remove(34)
a
[66, 49, 73, 97, 82]
a.remove(73)
a
[66, 49, 97, 82]
a.remove(121)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    a.remove(121)
ValueError: list.remove(x): x not in list
a = [66,49,73,97,82,29]
b=a.copy
b
<built-in method copy of list object at 0x0000023D2B31B740>
b=a.copy()
b
[66, 49, 73, 97, 82, 29]
c=a
c
[66, 49, 73, 97, 82, 29]
a.append(57)
c
[66, 49, 73, 97, 82, 29, 57]
c.clear()
a
[]
b.clear()
b
[]
a
[]
b
[]
c
[]
a = [66,49,73,97,82,29,73,29]
a.count(73)
2
a.index(29)
5
a.count(333)
0
x+y
[30, 40, 50, 60, 22, 32, 42, 52]
x.extend([10])
x
[30, 40, 50, 60, 10]
p=list()
p
[]
p=list(0)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    p=list(0)
TypeError: 'int' object is not iterable
p=int(list(0))
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    p=int(list(0))
TypeError: 'int' object is not iterable
a.reverse()
a
[29, 73, 29, 82, 97, 73, 49, 66]
a.sort()
a
[29, 29, 49, 66, 73, 73, 82, 97]
a.sort(reverse=True)
a
[97, 82, 73, 73, 66, 49, 29, 29]
a
[97, 82, 73, 73, 66, 49, 29, 29]
a.sort()
a
[29, 29, 49, 66, 73, 73, 82, 97]
for i in a:
    if a.count(i)>1:
        a.remove(i)

        
a
[29, 49, 66, 73, 82, 97]

a = ["10", 20, 30]
a
['10', 20, 30]
b = [20, "10", 30]
b
[20, '10', 30]

"10" in a
True

for i in a:
    if i not in b:
        flag = False
        break
    flag = True

    
flag
True

a= [29, 29, 49, 66, 73, 73, 82, 97]
for i in a:
    print(a.index(i), i)
    if a.count(i)>1:
        a.remove(i)
print(a)
SyntaxError: invalid syntax
a= [29, 29, 49, 66, 73, 73, 82, 97]for i in a:
    print(a.index(i), i)
    if a.count(i)>1:
        a.remove(i)

SyntaxError: invalid syntax
a= [29, 29, 49, 66, 73, 73, 82, 97]
for i in a:
    print(a.index(i), i)
    if a.count(i)>1:
        a.remove(i)
        
SyntaxError: multiple statements found while compiling a single statement
a= [29, 29, 49, 66, 73, 73, 82, 97]
for i in a:
    print(a.index(i), i)
    if a.count(i)>1:
        a.remove(i)
        
SyntaxError: multiple statements found while compiling a single statement
a= [29, 29, 49, 66, 73, 73, 82, 97]

for i in a:
    print(a.index(i), i)
    if a.count(i)>1:
        a.remove(i)

        
0 29
1 49
2 66
3 73
4 82
5 97
a=[]
for i in range(1,101,1):
    if(a%i==1):
        a.append()

        
Traceback (most recent call last):
  File "<pyshell#197>", line 2, in <module>
    if(a%i==1):
TypeError: unsupported operand type(s) for %: 'list' and 'int'
a=[]
for i in range(1,101,1):
    if(i%2):
        a.append()
        
SyntaxError: multiple statements found while compiling a single statement
KeyboardInterrupt
a = []

for i in range(1,101,2):
    a.append(i)

    
a
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
a = []

for i in range(2,101):
    math.sqr
KeyboardInterrupt
a = math.sqrt(36)
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    a = math.sqrt(36)
NameError: name 'math' is not defined. Did you forget to import 'math'?
import math
a = math.sqrt(36)
a
6.0

a = [1,2,43,54]
len = len(a)
len
4
a[0] = a[0]+a[len-1]
a[len-1] = a[len-1] - a[0]
a[0] = a[0] - a[len-1]
a
[56, 2, 43, -1]
a = [1,2,43,54]
a[0] = a[0]+a[len-1]
a[len-1] = a[0]-a[len-1]
a[0] = a[0] - a[len-1]
a
[54, 2, 43, 1]
a = []
for i in range(1,101,1):
    
KeyboardInterrupt
odd = []
even =  []
prime = []
for i in range
SyntaxError: expected ':'
for i in range(1,101):
    if(a%i):
        odd.append()
        for i in range(2,    
KeyboardInterrupt

import math
for i in range(1,101):
    if(a%i):
        odd.append()
        for i in range(2,math.floor(math.sqrt(i)):
                       
SyntaxError: invalid syntax
for i in range(1,101):
    if(a%i):
        odd.append()
        for j in range(2,math.floor(math.sqrt(i))+1):
                       if i % j == 0:
                       break
                    
SyntaxError: expected an indented block after 'if' statement on line 5
for i in range(1,101):
    if(a%i):
        odd.append()
        for j in range(2,math.floor(math.sqrt(i))+1):
                       if i % j == 0:
                           break
                        
KeyboardInterrupt
import math
for i in range(1,101):
    if(a%i):
        odd.append()
        flag = False
        for j in range(2,math.floor(math.sqrt(i))+1):
                       if i % j == 0:
                           flag = False
                           break
                        flag = True
                        
SyntaxError: unindent does not match any outer indentation level
import mathfor i in range(1,101):
    if(a%i):
        odd.append()
        flag = False
        for j in range(2,math.floor(math.sqrt(i))+1):
                       if i % j == 0:
                           flag = False
                           breakflag = True
                           
SyntaxError: invalid syntax
import math
for i in range(1,101):
    if(a%i):
        odd.append()
        flag = False
        for j in range(2,math.floor(math.sqrt(i))+1):
                       if i % j == 0:
                           flag = False
                           breakflag = True
                           
SyntaxError: multiple statements found while compiling a single statement
KeyboardInterrupt
import math
import math
for i in range(1,101):
    if(a%i):
        odd.append()
        flag = False
        for j in range(2,math.floor(math.sqrt(i))+1):
                       if i % j == 0:
                           flag = False
                           breakflag = True
                           
SyntaxError: multiple statements found while compiling a single statement
import math
for i in range(1,101):
    if a%i:
        odd.append(i)
        flag = False
        for j in range(2,math.floor(math.sqrt(i))+1):
            if not(i%j)
            
SyntaxError: expected ':'
import math
for i in range(1,101):
    if a%i:
        odd.append(i)
        flag = False
        for j in range(2,math.floor(math.sqrt(i))+1):
            if not(i%j):
                flag = False
                break
            flag = True
        if flag:
            prime.append(i)

            
Traceback (most recent call last):
  File "<pyshell#264>", line 2, in <module>
    if a%i:
TypeError: unsupported operand type(s) for %: 'list' and 'int'
import math
for i in range(1,101):
    if i%2:
        odd.append(i)
        flag = False
        for j in range(2,math.floor(math.sqrt(i))+1):
            if not(i%j):
                flag = False
                break
            flag = True
        if flag:
            prime.append(i)
    else:
        even.append(i)

        
odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
prime
[5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
import math
for i in range(1,101):
    if i%2:
        odd.append(i)
        flag = False
        for j in range(2,math.ceil(math.sqrt(i))+1):
            if not(i%j):
                flag = False
                break
            flag = True
        if flag:
            prime.append(i)
    else:
        if i == 2:
            prime.append(i)
        even.append(i)

        
odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
odd = []
prime = []
even=[]
import math
for i in range(1,101):
    if i%2:
        odd.append(i)
        flag = False
        for j in range(2,math.ceil(math.sqrt(i))+1):
            if not(i%j):
                flag = False
                break
            flag = True
        if flag:
            prime.append(i)
    else:
        if i == 2:
            prime.append(i)
        even.append(i)

        
odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
prime
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
s= "hello world"
for i in range(0,len(s)):
    print(s[i])

    
Traceback (most recent call last):
  File "<pyshell#289>", line 1, in <module>
    for i in range(0,len(s)):
TypeError: 'int' object is not callable
s = "hello world"
for i in range(0, len(s),1):
    print(s[i])

    
Traceback (most recent call last):
  File "<pyshell#293>", line 1, in <module>
    for i in range(0, len(s),1):
TypeError: 'int' object is not callable
type(s)
<class 'str'>
s = "hello world"
print(s)
hello world
triple = """Hii
how are you
all good?"""
print(triple)
Hii
how are you
all good?
triple
'Hii\nhow are you\nall good?'
string = "Racecar"
for i in range(0,len(string),1):
    print(string)

    
Traceback (most recent call last):
  File "<pyshell#305>", line 1, in <module>
    for i in range(0,len(string),1):
TypeError: 'int' object is not callable
>>> string = "Racecar"
... for i in range(0,len(string),1):
...     print(string[i])
...                        
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> string = "racecar"
...                        
>>> for i in range(0,len(string),1):
...                        print(string[i])
... 
...                        
Traceback (most recent call last):
  File "<pyshell#311>", line 1, in <module>
    for i in range(0,len(string),1):
TypeError: 'int' object is not callable
>>> type(i)
...                        
<class 'int'>
>>> s.
...                        
SyntaxError: invalid syntax
>>> s = "hello world"
...                        
>>> s.
...                        
SyntaxError: invalid syntax
>>> s.capitalize
...                        
<built-in method capitalize of str object at 0x0000023D2DE0EE70>
>>> s
...                        
'hello world'
>>> s.capitalize()
...                        
'Hello world'
>>> s.upper()
...                        
'HELLO WORLD'
>>> s.lower()
...                        
'hello world'
>>> s.find(z)
...                        
Traceback (most recent call last):
  File "<pyshell#321>", line 1, in <module>
    s.find(z)
NameError: name 'z' is not defined
>>> s.find('z')
...                        
-1
>>> s.index('s')
...                        
Traceback (most recent call last):
  File "<pyshell#323>", line 1, in <module>
    s.index('s')
ValueError: substring not found
>>> s.count('l')
...                        
3
