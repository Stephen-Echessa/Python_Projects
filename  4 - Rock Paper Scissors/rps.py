import random

rps = ["Rock","Paper","Scissors"]

user = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))
if user>2:
    print("Cap")
else:
    user_answer = rps[user]
    print(f"User answer: {user_answer}")

    computer_answer = rps[random.randint(0,2)]
    print(f"Computer answer: {computer_answer}")

    if user_answer == computer_answer:
        print("Its a draw")
    elif user_answer=="Rock" and computer_answer=="Paper":
        print("You lose")
    elif user_answer=="Rock" and computer_answer=="Scissors":
        print("You win")
    elif user_answer=="Paper" and computer_answer=="Rock":
        print("You win")
    elif user_answer=="Paper" and computer_answer=="Scissors":
        print("You lose")
    elif user_answer=="Scissors" and computer_answer=="Rock":
        print("You lose")
    elif user_answer=="Scissors" and computer_answer=="Paper":
        print("You win")