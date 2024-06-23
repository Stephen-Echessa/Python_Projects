import random

letters = ['a','b','c','d','e','A','B','C','D','E']
numbers =  ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','+','_','$','#','@']

print("Welcome to PyPassword Generator")
nr_letters = int(input("How many letters would you like in the password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

total_letters = ""
for n in range(1,nr_letters+1):
    random_index = random.randint(0,len(letters)-1)
    total_letters += letters[random_index] + " "

total_numbers = ""
for n in range(1,nr_numbers+1):
    random_index = random.randint(0,len(numbers)-1)
    total_numbers += numbers[random_index] + " "

total_symbols = ""
for n in range(1,nr_symbols+1):
    random_index = random.randint(0,len(symbols)-1)
    total_symbols += symbols[random_index] + " "

easy_password = total_letters + total_numbers + total_symbols
print(easy_password)

password_list = easy_password.split()
random.shuffle(password_list)

print(password_list)

hard_password = ''
for key in password_list:
    hard_password += key

print(hard_password) 
