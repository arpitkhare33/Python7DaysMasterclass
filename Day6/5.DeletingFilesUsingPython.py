import os
try:
    os.remove("sample.txt")
    print("File deleted successfully.")
except Exception as ex:
    print(ex)
    print("File not Found")
