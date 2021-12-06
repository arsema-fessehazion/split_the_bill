#My attempt at a Tip Calculator
#Input functions to allow the user to set the relevant information
print("Welcome to the tip calculator.")
total_amount = float(input("What was the total bill? £"))
no_of_guests = int(input("How many people to split the bill? "))
bill_tip = int(input("What % tip would you like to give? 10, 12 or 15? "))

#calulates the tip as a % from user input
tip_increase = bill_tip /100
#Calculates the new total bill including tip
total_plus_bill = total_amount + (total_amount * tip_increase)
split_bill = float(total_plus_bill/no_of_guests)

#f function to call the variable within the print statement
print(f"Each person should pay: £{split_bill:.2f}")
