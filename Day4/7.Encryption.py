def encrypt(msg):  # msg = "Meetatten"
    enc_msg = ""
    for ch in msg:
        asc = ord(ch) + 3
        ench = chr(asc)
        enc_msg = enc_msg + ench
        print(enc_msg)
    print("Encrypted message:", enc_msg)


msg_to_encrpyt = input("Enter the message you want to encrypt: ")
encrypt(msg_to_encrpyt)

