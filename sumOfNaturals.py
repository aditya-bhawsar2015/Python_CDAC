def naturalNumbersSum(start,end):
    sum = 0
    for i in range(start,end+1):
        sum+=i
    return sum

start = int(input("Enter start range : "))
end = int(input("Enter ending range : "))

totalSum = naturalNumbersSum(start,end)
print("The sum is : ", totalSum)


# def arsmstrong(nums):
#     # while num<0:
#     #     x = num%10
#     #     sum +=x
#     #     num= num/10
#     sum2 = 0
#     num = nums
#     while num>0:
#         x = num % 10
#         print("x:",x)
#         sum2 = sum2 +  x*x*x
#         print("sum2:",sum2)
#         num = num // 10
#         print("num:",num)
#
#     if nums == sum2:
#         return True
#     else:
#         return False
#
# print(arsmstrong(153))