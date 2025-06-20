

l = [i for i in range(0,11)]

x = iter(l)

print(l)            # loads whole list at once in the memory directly
print(next(x))      # loads in the memory one by one
print(next(x))
print(next(x))
print(len(l))