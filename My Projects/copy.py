import random

def main(): # main function
    print("Welcome to the number guesser game")
    range_func()
    max_guess_number(lower_range_cut, upper_range_cut)
    evaluation(random_number, total_guesses)

def range_func():   # allows user to select a range for the number guess
    print("Please select a range in which you would like to guess.")
    lower_range_cut = int(input("Lower boundary limit: "))
    global lower_range_cut
    upper_range_cut = int(input("Upper boundary limit: "))
    global upper_range_cut
    random_number = random.randint(lower_range_cut,upper_range_cut)
    global random_number
    return lower_range_cut, upper_range_cut, random_number

def max_guess_number(low,high): # returns the total number of guesses
    total_numbers = (high - low) + 1
    total_guesses = 0
    while (2**total_guesses) < total_numbers:
        total_guesses += 1
    print ("You have a total of %d guesses\n"
           "for your range between %d to %d"
           % (total_guesses, low, high))
    global total_guesses
    return total_guesses

def evaluation(random_number, total_guesses): # evaluates the users input
    guess_count = 0
    while guess_count < total_guesses:
        user_guess = int(input("Your guess: "))
        print("Your guess is: %d" % (user_guess))
        if (random_number == user_guess):
            print("You got it ")
            break
        elif user_guess > random_number:
            print("Guess lower!")
            guess_count += 1
        else:
            print("Guess higher!")
            guess_count += 1

if __name__ == "__main__":
    main()
