# day = 6
# match day:
#     case 1|2|3|4|5: 
#         print("Weekday")
#     case 6|7:
#         print("Weekend")
#     case _:
#         print("Invalid")

#else statement is not executed if break statement is used

# for i in range(6):
#     if i == 3: break
#     print(i)
# else:
#     print("Loop completed without break")                    

# def name(firstname):
#     print(firstname + " sherry")
#     print(firstname + " cherry")    
#     print(firstname , " ohh no")

# name("yoo")


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)