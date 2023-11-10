# Python program to check if year is a leap year or not

# To get year (integer input) from the user
year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year

# not divided by 100 means not a century year
# year divided by 4 is a leap year

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
