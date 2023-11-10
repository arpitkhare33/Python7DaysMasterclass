# 1. Take msg as input from user.
msg = input("Enter your secret msg")


# 2. Encrypt the msg
def encrypt(msg):
    enc_msg = ""
    for ch in msg:
        asc = ord(ch) + 3
        ench = chr(asc)
        enc_msg = enc_msg + ench
        print(enc_msg)

    return enc_msg


encrypted_msg = encrypt(msg)

# 3. Store the msg in the secret_msg txt file.
file = open("secretMsg.txt", 'a')
file.write(encrypted_msg)
file.close()

