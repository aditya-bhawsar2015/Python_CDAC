from abcd import oddEven

x = [i for i in range(1,101) if oddEven(i)]

print(x)

l = [10,12,68,3,2,7,9,11,56,43,67]

y = [i for i in l if i%2==0]

print(y)

z = [i for i in l if i%2!=0]

print(z)

my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "kiwi", "lemon", "mango", "orange", "pear", "quince", "raspberry", "strawberry", "watermelon", "xigua"]

a_list = [i for i in my_list if i.startswith("a")]

print(a_list)

def checkVowelCount(s):
    s = str(s)
    s = s.lower()
    vowelList = ["a", "e", "i", "o", "u"]
    count = 0
    for i in s:
        if i in vowelList:
            count+=1
            if count>1:
                return True
    return False

twoVowelsList = [i for i in my_list if checkVowelCount(i)]

print(twoVowelsList)