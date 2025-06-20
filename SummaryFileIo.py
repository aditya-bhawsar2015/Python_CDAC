
def summary():
    file = open('abc.txt','r')
    data = file.readlines()
    print(data)
    upper_count = 0
    lower_count = 0
    special_count = 0

    for i in data:
        if i.upper():
            upper_count = upper_count+1
            return upper_count
        elif  i.lower():
            lower_count = lower_count+1
            return lower_count
    file.close()

summary()