
def vowels_count(string):
    count = 0
    vowels = 'aeiou'
    for char in string.lower():
        if char in vowels:
            count+=1
    return count

print(vowels_count("abba"))
