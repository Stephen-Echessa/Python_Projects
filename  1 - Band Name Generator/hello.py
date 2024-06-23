# print("Welcome to the Band Name Generator\n")
# bandName = input("What's name of the city you grew up in?\n")
# petName = input("What's your pet name?\n")
# print("Your band name could be " + bandName + " " + petName)

import os
dir = "C:/Users/pp/Documents/Python Projects"
os.chdir(dir)
files = os.listdir(dir)
for i in range(len(files)):
    os.rename(files[i], files[i].replace("Day", ""))