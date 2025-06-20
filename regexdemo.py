import re

#findall , search ,sub->substitute ,split

s = "hello 9world how are9 you hel7lo again baab 1111111111, 2323232323"

x = re.findall("[0-9]+.",s)

print(x)

x = re.findall("[0-9]{10}",s)

print(x)

