#My attempt at a Tip Calculator
print("Welcome to the tip calculator.")
total_amount = float(input("What was the total bill? £"))
no_of_guests = int(input("How many people to split the bill? "))
bill_tip = int(input("What % tip would you like to give? 10, 12 or 15? "))

tip_increase = bill_tip /100
total_plus_bill = total_amount + (total_amount * tip_increase)
split_bill = float(total_plus_bill/no_of_guests)

print(f"Each person should pay: £{split_bill:.2f}")
