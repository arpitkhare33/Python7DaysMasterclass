# 1. Read secret msg from the txt file.
file = open("secretMsg.txt", 'r')
secret_msg = file.read()
print(secret_msg)
file.close()


# 2. Decrypt the secret msg to get the actual msg.
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