try:
    res = 4/2
    print("Trying to do the division")
except Exception as ex:
    print(ex)
else:
    print("There was no error in the try part.")
finally:
    print("I dont know, what happened above, I will always run.")