import pandas

# TODO 1. Create a dictionary in this format:
nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_csv.iterrows()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
should_continue = True
while should_continue:
    user_input = input("Enter a word: ").upper()
    try:
        nato_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(nato_list)
        should_continue = False
