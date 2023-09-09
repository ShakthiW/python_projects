#Author - Shakthi
#Date - 24th Oct. 2022

#Number Guess

import random
y = 10

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    guess_count = 1
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x} : "))
        if guess > random_number:
            print("Sorry, guess again. Too high : ")
            guess_count += 1

        elif guess < random_number:
            print("Sorry, guess again. Too low : ")
            guess_count += 1
        
    print(f"Yay! congrtas you guessed the number {random_number} correctly in {guess_count} guesses.")
  

guess(10)

print(f"It's computer's turn to guess the number. Think of a number between 1 and {y} \n")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    guess_count = 1
    while feedback != "c":
        if high != low:
            guess = random.randint(low, high)
        else:
            guess = high
            
        feedback = input(f"Is {guess} too high (H), too low(L) or correct(C) : ").lower()

        if feedback == "h":
            high = guess - 1
            guess_count += 1
            
        elif feedback == "l":
            low = guess + 1
            guess_count += 1

        elif feedback == "c":
            print(f"Yay! the computer guessed {guess} correctly in {guess_count} attempts.")   
            return

        else:
            print("Enter a valid letter!")

   
        
computer_guess(10)

