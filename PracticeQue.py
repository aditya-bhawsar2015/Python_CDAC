a = [1,5,7,9,11]
b = [7,9,1,2,8]

commonList = list(filter(lambda x: x in b,a))

print(commonList)



s = "Hello world how are you"

s = s.split(" ")

print(s)

def stringOperation(s):
    return [str(s).upper(), str(s).lower(), len(s)]

x = list(map(stringOperation, s))

y = list(map(lambda x : [str(x).upper(),str(x).lower(),len(x)], s))

print(y)

print(x)

