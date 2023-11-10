# Printing Strings
name = "Ramesh"
print("Hello", name)


# Concatenating Strings
first_name = "Arpit"
last_name = "Khare"
print(first_name + " | | " + last_name)

# Visualisation of Strings
first_name = ['A', 'r', 'p', 'i', 't']
# Selecting any character in Strings
print(first_name[0])
print(first_name[1])
print(first_name[2])

# Size of a string
print(len(first_name))
print(first_name[len(first_name)-1])

# Replace substring from a string
welcome_str = "Hi, welcome to Codekaro, this is Arpit."
welcome_str = welcome_str.replace("Arpit", "Khare")
print(welcome_str)

# Counting a character in string
count_space = welcome_str.count(" ")
print("Count of spaces are: ", count_space)

# String Multiplication
res = first_name * 5 # first_name + first_name + ... (5 times)
# print(res)


# Splitting a String
word_list = welcome_str.split()
print(word_list)

word_list2 = welcome_str.split(",")
print(word_list2)


