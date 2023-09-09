import random

user_wins = 0
computer_wins = 0
ties = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter Rock/ Paper/ Scissors or Enter Q to quit: \n").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Please enter a valid option!")
        continue

    random_number = random.randint(0, 2)

    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It's a Tie!")
        ties += 1
        continue
        
    else:
        print("You Lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Tied", ties, "times.")

print("Good Bye!")

    
