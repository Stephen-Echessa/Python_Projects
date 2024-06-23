# import data and random
from random import choice
from game_data import data

# Compare their number of followers
def compare_followers(a,b):
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}\n\n\n")
    print(f"VS\n\n\n")
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}\n\n\n")

    if a['follower_count']>b['follower_count']:
        return 'a'
    elif b['follower_count']>a['follower_count']:
        return 'b'

    
    
print('''
    HIGHER LOWER GAME
    -----------------
''')
game_score = 0
should_continue = True

a = choice(data)
b = choice(data)


# Use while to continue game
while should_continue:
    #b should not be equal to a
    if b==a:
        b = choice(data)

    correct_answer = compare_followers(a,b)

    # If one guesses right, compare with other random celebrity
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == correct_answer:
        game_score += 1
        print(f"Excellent! Current score is {game_score}")
        a = b
        b = choice(data)

    # If wrong, game over
    else:
        print(f'Sorry, that is wrong. Final score is {game_score}')
        should_continue = False