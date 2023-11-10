import io

try:
    file = open("sample.txt", 'r')
    try:
        file.write("Arpit Khare")
    except io.UnsupportedOperation as nw:
        print(nw)
        print("File is not writable")
    file.close()
except FileNotFoundError as ex:
    print(ex)
    print("Some problem in opening the file.")
else:
    print("File opened successfully")
