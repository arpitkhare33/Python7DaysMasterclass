customers = [
    {"Name": "Mahesh", "Age": 30, "City": "Mumbai", "Payment Mode": "Card"},
    {"Name": "Raman", "Age": 34, "City": "Delhi", "Payment Mode": "UPI"},
    {"Name": "Mahendra", "Age": 24, "City": "Hyderabad", "Payment Mode": "Cash"},
    {"Name": "Aman", "Age": 29, "City": "Mumbai", "Payment Mode": "Card"},
    {"Name": "Suraj", "Age": 28, "City": "Delhi", "Payment Mode": "Cash"},
    {"Name": "Nitin", "Age": 27, "City": "Pune", "Payment Mode": "UPI"},
    {"Name": "Arpit", "Age": 31, "City": "Delhi", "Payment Mode": "Card"},
    {"Name": "Ashish", "Age": 29, "City": "Mumbai", "Payment Mode": "Card"},
    {"Name": "Amit", "Age": 30, "City": "Bangalore", "Payment Mode": "Cash"},
    {"Name": "Peter", "Age": 30, "City": "Mumbai", "Payment Mode": "Cash"},
    {"Name": "Robert", "Age": 28, "City": "Mumbai", "Payment Mode": "Cash"},
    {"Name": "Mark", "Age": 30, "City": "Mumbai", "Payment Mode": "UPI"},
]

# Importing library
import random
# Generating random number without hard-coding the range
# print(random.randint(1, 10))
# print(len(customers))
i = random.randint(0, len(customers)-1)

# Rotate the Roulette
print(customers[i])
# Display the Bill Payer details
