import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

names_length = len(names)
random_index = random.randint(0,names_length-1)
print(f"{names[random_index]} is going to buy the meal today!")