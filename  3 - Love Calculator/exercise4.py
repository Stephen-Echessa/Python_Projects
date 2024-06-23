from tkinter import Y


print("Welcome to Python Pizza Deliveries")
size = input("What size do you want? S, L or M? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

if size=="S":
    bill=15
    if add_pepperoni=="Y":
        bill+=2
elif size=="M":
    bill=20
    if add_pepperoni=="Y":
        bill+=3
elif size=="L":
    bill=25
    if add_pepperoni=="Y":
        bill+=3
if extra_cheese=="Y":
        bill+=1
print(bill)