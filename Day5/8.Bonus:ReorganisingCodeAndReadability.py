# Date Created:
# Created by:
# Last modification date:
# Last modification:
# Description: 


# 1. Read secret msg from the txt file.

def read_file(file_name):
    file = open(file_name, 'r')
    secret_msg = file.read()
    file.close()
    print(secret_msg)


read_file("secretMsg.txt")


# 2. Decrypt text: Parameter Name: msg
def decrypt(msg):
    original_msg = ""
    for ch in msg:
        asc = ord(ch) - 3
        ench = chr(asc)
        original_msg = original_msg + ench

    return original_msg


o_msg = decrypt(secret_msg)


# 3. Display the original msg to the user.
print("The original msg sent from sender was: ")
print(o_msg)