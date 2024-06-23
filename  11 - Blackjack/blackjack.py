import random
from art import logo

print(logo)
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


should_continue = True

play = input("Do you want to play a game of Blackjack? 'y' or 'n': ")
if play=='n':
    should_continue = False

while should_continue:
    dealer_score = 0
    dealer_cards = []
    user_cards = []

    def dealer_chooses_card():
        dealer_card = random.choice(cards)
        dealer_cards.append(dealer_card)
    def user_chooses_card():
        user_card = random.choice(cards)
        user_cards.append(user_card)

    def calc_scores():
        user_score = 0
        dealer_score = 0

        user_chooses_card()
        user_chooses_card()

        for total in user_cards:
            user_score += total
        
        print(f"    Your cards: {user_cards}, current score: {user_score}")

        dealer_chooses_card()
        print(f"    Computer's first card: {dealer_cards[0]}")

        should_pick = True

        while should_pick and user_score<=21:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            
            if another_card== "y" and user_score==21:
                user_score = 0
                cards.remove(11)
                cards.append(1)
                user_chooses_card()
                for total in user_cards:
                    user_score += total

                if user_score == 22:
                    return (f"    Your cards: {user_cards}, current score: {user_score}, thus you win!")

            elif another_card == "y":
                user_score = 0
                user_chooses_card()
                for total in user_cards:
                    user_score += total

                print(f"    Your cards: {user_cards}, current score: {user_score}")

            else:
                should_pick = False

        if user_score>21:
            return "You went over. You lose!"

        while dealer_score<17:
            dealer_chooses_card()
            dealer_score = 0

            for total in dealer_cards:
                dealer_score += total

        print(f"    Computer's final hand: {dealer_cards}, current score: {dealer_score}")

        if dealer_score>21:
            return "Computer went over. You win!"

        if dealer_score>user_score:
            return "Your scores are lower. You lose!"

        if dealer_score==user_score:
            return "Your scores are equal. Its a draw"

        if dealer_score<user_score:
            return "Your scores are higher. You win"
                
    print(calc_scores())

    restart = input("Do you want to play again? 'y' or 'n': ")
    if restart=='n':
        should_continue = False