import random
from words_list import word_list

stages = ["*","**","***","****","*****","******"]
lives = 6

chosen_index = random.randint(0,len(word_list)-1)
chosen_word = word_list[chosen_index]
# chosen_word = random.choice(word_list)

# print(f"Yooo, the chosen word is {chosen_word}")

display = []

for dash in chosen_word:
    display.append("_")

print(display)
print(f"Lives: {stages[lives-1]}")

loop = True

while loop:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        if guess in display:
            print(f"You have already guessed {guess}")

        else:
            print(f"You guessed the letter {guess}, which is in the chosen word")


    for index in range(0,len(chosen_word)):
        letter = chosen_word[index]
        if guess == letter:
            display[index] = guess

    if guess not in chosen_word:
        lives-=1
        print(f"Cap...The letter {guess} is not in the word, thus you lose a life")
        print(f"Lives: {stages[lives-1]}")

    print(display)

    if "_" not in display:
        loop = False
        print("You win!")

    if lives==0:
        loop = False
        print("You lose!")    

    