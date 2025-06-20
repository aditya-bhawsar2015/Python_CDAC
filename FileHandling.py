

def fileFunction():
    file = open('abc.txt', 'w')
    file.write('Heyy! How are you?')
    file.close()

    file = open('abc.txt','r')
    data = file.read()
    file.close()
    return data


data = fileFunction()

print(data)