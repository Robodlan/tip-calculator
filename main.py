print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
percentage = int(input("How much tip would you like to give? 10, 12, 15 "))
people = int(input("How many people to split the bill? "))
bill_tip = percentage / 100 * total + total
tip =  bill_tip / people
print(f"Your tip would be ${round(tip, 2)}")

# tip = total_plus_perc / people
# print(f"Your tip would be {tip}")

# print(round(15.22345, -1))

