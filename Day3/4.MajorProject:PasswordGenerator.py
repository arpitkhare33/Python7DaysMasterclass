# ============================================= Importing libraries ================================================
import random
import array

MAX_LEN = 12

# ======================================== Sets of Characters to mix match =========================================
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOWERCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                        'U', 'V', 'W', 'X', 'Y', 'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

# ======================================== Password Logic Starts here ==============================================

# Combining Lists
COMBINED_LIST = DIGITS + LOWERCASE_CHARACTERS + UPPERCASE_CHARACTERS + SYMBOLS
print(COMBINED_LIST)

# Generating password from combined list
len_password = 0
password = []
while len_password < MAX_LEN:
    temp = random.choice(COMBINED_LIST)
    password.append(temp)
    len_password = len_password + 1

print(password)
my_password = ",".join(password)
print(my_password)
