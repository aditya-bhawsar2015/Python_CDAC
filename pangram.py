import string
def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    print(set(s.lower()))
    return set(s.lower()) == alphabet

print(is_pangram("Thequickbrownfoxjumpsoverthelazydog"))