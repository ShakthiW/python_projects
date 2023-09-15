# Guess the word

secret = 'water'
guesses = ''
turns = len(secret) + 3



input(f"Wellcome to the word guess game.You have {turns} turns. Press enter to continue")


print(f"Your secret word is...")
print('_ ' * len(secret))

while turns > 0:
    guess = input("\nGuess a letter in the word: ").lower()
    missed = 0

    if len(guess) > 1:
        guess == guess[1]

    guesses += guess
    turns -= 1
    
    for guess in secret:
        if guess in guesses:
            print('', guess, '', end='')
        else:
            print('_ ', end='')
            missed += 1

    if missed == 0:
        print("\nCongratulations you won the game")
        break

if missed != 0:
    print("\nYou are out of turns.")
       
print("\nEnd of the game.")
