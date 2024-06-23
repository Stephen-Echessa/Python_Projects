alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceasar(encrypt_text,shift_amount,cipher_direction):
    cipher_text = ""
    for letter in encrypt_text:
        if letter not in alphabet:
            cipher_text+=letter

        else:
            position = alphabet.index(letter) 
            if cipher_direction=="encode":
                new_position=position + shift_amount
                if new_position>=len(alphabet):
                    new_position = new_position%len(alphabet)
                cipher_text += alphabet[new_position]
            elif cipher_direction=="decode":
                new_position=position - shift_amount
                if new_position>=len(alphabet):
                    new_position = new_position%len(alphabet)
                cipher_text += alphabet[new_position]
        
    print(f"The {cipher_direction}d code is {cipher_text}")

def play_game():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #shift = shift % 26

    ceasar(text,shift,direction)

    restart = input("Do you want to play again? Type 'yes' or 'no'\n")
    if restart=="yes":
        restart_game()
    else:
        print("Sayonara")

def restart_game():
    play_game()

play_game()