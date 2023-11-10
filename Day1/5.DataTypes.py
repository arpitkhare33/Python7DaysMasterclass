# Int
num = 23
# print(type(num))
# Float: Decimal
fl = 45.43
# print(type(fl))

# Str
str_1 = "Hello World"
# print(type(str_1))

# List
# - Creating Lists
my_pets = ['Tommy', 'Jammy', 'Bulldog']  # list of strings

# - Accessing elements
# print(my_pets[2])

# - Appending items
my_pets.append("Jerry")
my_pets.append(7)
# print(my_pets)

# Tom
# Harry
# Entertainment

# Extending the list
# my_pets.extend(["Tom", "Harry", "Entertainment"])
my_pets.append(["Tom", "Harry", "Entertainment"])
# print(my_pets)
my_pets[0] = "Raman"
# - Removing items
my_pets.remove(7)
print(my_pets)


# Tuple
# - Meaning and Need of Immutability

# - Creating Tuples
tup1 = (12, 23, 56)
# print(type(tup1))
# - Accessing elements in Tuples
# print(tup1[2])

# tup1[2] = 65

# Dictionary: {key: value, key: val}
person = {
    "Name": "Arpit",
    "Contact": 123,
    "Profession": "Teacher"
}
print(person["Name"])
print(type(person))


# Set
# - Unordered, Unique
my_set = {1,1,2,2,3}
print(my_set)
print(type(my_set))


# Bool: Boolean
x = 1 == 4
print(x)
print(type(x))

# List, Str, Tuple, Dictionary
