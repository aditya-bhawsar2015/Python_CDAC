def celciusToFar(celcius):
    far = (celcius*(9/5))+32
    return far

def farToCelcius(farh):
    cel = (farh-32)*(5/9)
    return cel

print(farToCelcius(89.6))
print(celciusToFar(32))
