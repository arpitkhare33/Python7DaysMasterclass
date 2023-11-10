# The Food bill amount
food_bill = float(input("Enter the food bill amount: "))

# percent of tip
tip_perc = float(input("Enter the tip percentage: ")) #10

final_amount = food_bill + tip_perc * food_bill / 100

print(f"The final bill amount including {tip_perc} tip is: {final_amount}")
