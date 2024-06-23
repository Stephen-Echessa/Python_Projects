print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

bill_per_person = round((bill * (100 + tip_percentage)/100)/number_of_people,2)

print(f"Each person should pay: ${bill_per_person}")