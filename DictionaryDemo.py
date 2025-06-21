info = {
    "Name" : "Rahul",
    "RollNo" : 123,
    "Address" : "Delhi",
    "Pin" : 543210
}

more_info = {
    "College" : "CDAC",
    "Area" : "Pune"
}
info["Name"] = "Singh"

print(info)

data = "Virat Kohli scored 97 runs off 58 balls on 20"

new_data = data.lower()

print(new_data)

print(info["RollNo"])

info.update(more_info)

print(info)

new_ser = set()

print(type(new_ser))

set1 = {1,2,3,4,5}
set1.update()
print(set1)