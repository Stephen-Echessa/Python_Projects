from random import randint

print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type of easy or hard: ")

lives = 0
if difficulty == 'easy':
    lives = 10

elif difficulty == 'hard':
    lives = 5

random_number = randint(1,100)

try_again = True
while try_again:
    print(f"You have {lives} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess == random_number:
        print(f"You got it! The answer was {random_number}")
        try_again = False
    elif guess > random_number:
        lives -= 1
        print(f"Too high! ")
    else:
        lives -= 1
        print(f"Too low!")

    if lives == 0:
        print("Big L. Game Over!!!")
        try_again = False
    

