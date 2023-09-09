# Rock, Paper, Scissors Game

import random
num = random.randint(1, 3)


def main():
    user_choice = input("Please type your choice ('rock' 'paper' or 'scissors'): ").capitalize()
    comp_choice = computer(num)
    print(f"The Computer Chose {comp_choice}")
    print(results(user_choice, comp_choice))


def results(choice_comp, choice_user):
    if choice_comp == 'Rock' and choice_user == 'Paper':
        return 'You lost this time.'
    elif choice_comp == 'Paper' and choice_user == 'Scissors':
        return 'You lost this time.'
    elif choice_comp == 'Scissors' and choice_user == 'Rock':
        return 'You lost this time.'
    elif choice_comp == choice_user:
        return 'It\'s a draw.'
    else:
        return 'Congratulations you won the round.'


def computer(num):
    if num == 1:
        comp_choice = 'Rock'
    elif num == 2:
        comp_choice = 'Paper'
    else:
        comp_choice = 'Scissors'
    return comp_choice


main()