def armstrongInRange(start,end):
    armstrongList = []
    for num in range(start,end+1):
        sum = 0
        temp = num
        while temp>0:
            digit = temp%10
            sum += digit**3
            temp//=10


        if num ==sum:
            armstrongList.append(num)

    return armstrongList

print(armstrongInRange(150,410))