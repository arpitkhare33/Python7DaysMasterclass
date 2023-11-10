# BMI = Weight (kg) / (Height (m)) **2
# Input: weight, height
# F Strings

height = float(input("Enter the height in m"))
weight = float(input("Enter the weight in kg"))

bmi = weight / height ** 2

# F string
print(f"Your bmi value is: {bmi}. BMI: {bmi}. Stay healthy.")


