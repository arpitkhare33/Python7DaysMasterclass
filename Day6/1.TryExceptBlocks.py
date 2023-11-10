# What is error handling, why do we need them?
def division(num1, num2):
    return num1 / num2


n1 = int(input("Enter the Numerator"))
n2 = int(input("Enter the Denominator"))
res = "No result"
try:
    res = division(n1, n2)
except Exception as ex:
    print(ex)
print("The division is :", res)
# Try Except blocks
