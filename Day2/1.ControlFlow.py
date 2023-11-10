# If statements
x = 44
# if x < 50:
#     print("Number is less than 50")

    # print("Number is greater than 50") # if block
# If-Else statements
# if x < 50:
#     # block starts here
#     print("Number is less than 50")
#     # ends here
# else:
#     # starts here
#     print("Number is greater than 50")
#     # ends here

# If elif else
#
# if x < 30:
#     print("Less than 30")
# elif x < 40:
#     print("Less than 40")
# elif x < 50:
#     print("Less than 50")
#
# else:
#     print("Number out of range")


# Nested If-Else statements
x = 4
if x < 30:
    if x < 20:
        if x < 10:
            print("X is less than 10")


# Ternary Operators
a = 300
b = 400
min = a if a < b else b
print("Min value is: ", min)

# Logical Operators : and, or, not
# if a > 250 and b < 50:
#     print("Jackpot")
#
# if a > 250 or b < 50:
#     print("Jackpot2.0")

if not a < 250:
    print("Jackpot3.0")