import random

should_continue = True
all_positions = ['TL', 'TC', 'TR', 'ML', 'MC', 'MR', 'BL', 'BC', 'BR']
users_score = 0
computers_score = 0

# Create dictionary containing lists of winner slots
winner_arrays = {
    'top_horizontal': ['TL', 'TC', 'TR'],
    'middle_horizontal': ['ML', 'MC', 'MR'],
    'bottom_horizontal': ['BL', 'BC', 'BR'],
    'left_vertical': ['TL', 'ML', 'BL'],
    'center_vertical': ['TC', 'MC', 'BC'],
    'right_vertical': ['TR', 'MR', 'BR'],
    'diagonal': ['TL', 'MC', 'BR'],
    'reverse_diagonal': ['TR', 'MC', 'BL'],
}

horizontal_lines = '------------------------------'
vertical_lines = ' | '


def game_difficulty():
    difficulty_level = input('Choose your difficulty: Easy or Hard \n').upper().strip()
    if difficulty_level != 'EASY' and difficulty_level != 'HARD':
        print("Sorry! I didn't get that")
        game_difficulty()
    elif difficulty_level == 'EASY':
        return False
    else:
        return True


def diagram():
    return (f"   {slot_dict['TL']}    {vertical_lines}   {slot_dict['TC']}   {vertical_lines}   {slot_dict['TR']}   \n"
            f"{horizontal_lines}\n"
            f"   {slot_dict['ML']}    {vertical_lines}   {slot_dict['MC']}   {vertical_lines}   {slot_dict['MR']}   \n"
            f"{horizontal_lines}\n"
            f"   {slot_dict['BL']}    {vertical_lines}   {slot_dict['BC']}   {vertical_lines}   {slot_dict['BR']}   \n")


# User's play
def users_move(positions):
    chosen_slot = input(f'Choose slot to place your value: {",".join(positions)} \n').upper().strip()
    if chosen_slot not in positions:
        print("Please pick a valid option from the ones provided\n")
        users_move(positions)
    else:
        print(f"You chose {chosen_slot}")
        users_array.append(chosen_slot)
        slot_dict[chosen_slot] = user_pick
        slots.remove(chosen_slot)
        print(diagram())
        if len(users_array) >= 3:
            check_for_winner()
            if game_goes_on:
                computers_move(slots)
            else:
                pass
        else:
            computers_move(slots)


difficult = game_difficulty()


# Computer's play
def computers_move(positions):
    chosen_slot = random.choice(positions)
    if not difficult:
        pass
    else:
        random.shuffle(positions)
        for item in positions:
            for key in winner_arrays:
                if item in winner_arrays[key]:
                    new_array = list(winner_arrays[key])
                    new_array.remove(item)
                    users_check = all(i in users_array for i in new_array)
                    computers_check = all(i in computers_array for i in new_array)
                    if computers_check:
                        chosen_slot = item
                    elif users_check:
                        chosen_slot = item

    print(f'The computer chose {chosen_slot}')
    computers_array.append(chosen_slot)
    slot_dict[chosen_slot] = computers_pick
    slots.remove(chosen_slot)
    print(diagram())
    if len(computers_array) >= 3:
        check_for_winner()
        if game_goes_on:
            users_move(slots)
        else:
            pass
    else:
        users_move(slots)


def check_for_winner():
    global game_goes_on, users_score, computers_score
    filled_array = []
    for item in users_array:
        filled_array.append(item)
    for item in computers_array:
        filled_array.append(item)

    for winner_array in winner_arrays:
        users_check = all(item in users_array for item in winner_arrays[winner_array])
        computers_check = all(item in computers_array for item in winner_arrays[winner_array])

        if users_check:
            print('You won')
            game_goes_on = False
            users_score += 1
            print(f"Your score is {users_score} and the computer's score is {computers_score}")
            break
        elif computers_check:
            print('You lost')
            game_goes_on = False
            computers_score += 1
            print(f"Your score is {users_score} and the computer's score is {computers_score}")
            break
        else:
            game_goes_on = True

    check = all(item in filled_array for item in all_positions)
    if check:
        print('All slots are filled')
        game_goes_on = False


def keep_playing():
    keep_going = input('Would you like to continue: Yes or no?\n').upper().strip()
    if keep_going == 'NO':
        return False
    if keep_going == 'YES':
        return True
    else:
        print("Sorry I didn't get that.")
        keep_playing()


while should_continue:
    # Create list containing all playable slots
    slots = []

    for val in winner_arrays:
        for slot in winner_arrays[val]:
            if slot not in slots:
                slots.append(slot)

    slot_dict = {slot: ' ' for slot in slots}
    users_array = []
    computers_array = []

    game_goes_on = True

    user_pick = input("What will you play as: X or O? \n").upper().strip()
    if user_pick == 'O':
        computers_pick = 'X'
        while game_goes_on:
            computers_move(slots)
    elif user_pick == 'X':
        computers_pick = 'O'
        while game_goes_on:
            users_move(slots)
    else:
        print('Invalid option. Please choose between X and O')

    should_continue = keep_playing()
