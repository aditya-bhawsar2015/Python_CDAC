# num = int(input("Enter a number : "))
#
# li =[]
# for i in range(1, num+1):
#     if(num%i ==0):
#         li.append(i)
#
# print(num, "is divisible by : ",li)

num_list = [57,17,89,221,256]
new_list = []
print(num_list)

a = int(input("Enter a number to divide the above list by : "))
for i in num_list:
    if(i%a==0):
        new_list.append(i)

print("The number(s) divisible by", a ,"is/are " ,new_list)




