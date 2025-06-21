def calculate_hcf(num1,num2):
    smaller = min(num1,num2)

    for i in range(1, smaller+1):
        if (num1%i==0) and (num2%i==0):
            hcf = i
    return hcf

def calculate_gcd(num1,num2):
    while num2:
        num1,num2 = num2, num1%num2
    return num1

def calculate_lcm(num1,num2):
    if num1==0 and num2 ==0:
        return 0
    gcd = calculate_gcd(num1,num2)
    lcm = (num2*gcd)
    return lcm


num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
hcf_result = calculate_hcf(num1, num2)
lcm_result = calculate_lcm(num1,num2)
print("The HCF is : ", hcf_result)
print("The LCm is : ", lcm_result)