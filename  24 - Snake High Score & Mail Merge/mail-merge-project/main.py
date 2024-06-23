#TODO: Create a letter using starting_letter.txt
names_list = []
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.read().splitlines()

for name in names:
    #Replace the [name] placeholder with the actual name.
    with open("./Input/Letters/starting_letter.txt") as letter_file:
        letter = letter_file.read()

    print(f"{name}")
    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_for_{name}.doc", mode="w") as output_file:
        send_letter = letter.replace("[name]", name)
        output_file.write(send_letter)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp