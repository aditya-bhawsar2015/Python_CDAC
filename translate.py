sentence = "this is fun"

def translate(s):
    s = str(s)
    newS = []
    for i in s:
        if i not in 'aeiou' and i not in "AEIOU" and i != " ":
            newS.append(i+"o"+i)
        else:
            newS.append(i)

    print(newS)

    return "".join(newS)

print(translate(sentence))


my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "kiwi", "lemon", "mango", "orange", "pear", "quince", "raspberry", "strawberry", "watermelon", "xigua"]

new_list = [i for i in my_list if len(i)>=6]

print(new_list)
