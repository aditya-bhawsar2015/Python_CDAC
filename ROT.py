lower_encrypt = {}
upper_encrypt = {}
lower_encrypt[' '] = '0'
upper_encrypt[' ']='0'
lower_encrypt['0'] = ' '
upper_encrypt['0']=' '
i = 'a'


while(i<='z'):
    if i <= 'm':
        lower_encrypt[i] = chr(ord(i)+13)
        i = chr(ord(i)+1)
    else:
        lower_encrypt[i] = chr(ord(i)-13)
        i = chr(ord(i)+1)

i = 'A'
while(i<='Z'):
    if i <= 'M':
        upper_encrypt[i] = chr(ord(i)+13)
        i = chr(ord(i)+1)
    else:
        upper_encrypt[i] = chr(ord(i)-13)
        i = chr(ord(i)+1)

print(lower_encrypt)
print(upper_encrypt)

encrypted = []
def encrypt(string):
    for i in string:
        if i.isupper():
            encrypted.append(upper_encrypt[i])
        else:
            encrypted.append(lower_encrypt[i])

decrypted = []
def decrypt(string):
    for i in string:
        if i.isupper():
            decrypted.append(upper_encrypt[i])
        else:
            decrypted.append(lower_encrypt[i])


encrypt("Hi This is Aksahy and Aditya")

print("".join(encrypted))

decrypt("".join(encrypted))

print("".join(decrypted))


print(-012)