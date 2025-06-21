def binary_number(decimal_number):
    if decimal_number == 0:
        return "0"
    binary =""
    while decimal_number>0:
        remainder = decimal_number%2
        binary = str(remainder) + binary
        decimal_number//=2
    return binary


def octal_number(decimal_number):
    if decimal_number == 0:
        return "0"
    octal = ""
    while decimal_number>0:
        remainder = decimal_number % 8
        octal = str(remainder) + octal
        decimal_number//=8
    return octal

def hexadecimal_number(decimal_number):
    if decimal_number == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal_number>0:
        remainder = decimal_number%16
        hexadecimal = hex_chars[remainder] +  hexadecimal
        decimal_number//=16
    return hexadecimal

number = int(input("Enter the Decimal Number: "))
print("Binary number is: ",binary_number(number))
print("Octal Number is : ",octal_number(number))
print("Hexadecimal NUmber is : ",hexadecimal_number(number))
