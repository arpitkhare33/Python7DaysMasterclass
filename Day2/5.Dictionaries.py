# Creating dictionaries: key-value
my_student ={
    "roll": "1",
    "name": "Rahul",
    "age": 45,
    "contact": 123
}
# Accessing elements from dictionaries
# print(my_student["name"])
# print(my_student['age'])
# # Updating existing entries from dictionaries
# my_student["age"] = 46
# print(my_student)
# # Append new entries into dictionaries
# my_student['city'] = "Mumbai"
# print(my_student)
# # Pop the entry from dictionaries
# my_student.pop("contact")
# print(my_student)

# Missing key error
# print(my_student)
# print(my_student["city"])

# Nested Dictionaries
my_student ={
    "roll": "1",
    "name": "Rahul",
    "age": 45,
    "contact": 123,
    "addr": {
        "house_no": 45,
        "building": "XYZ Apartment",
        "city": "Delhi"
    }
}

print(my_student['addr']['house_no'])
