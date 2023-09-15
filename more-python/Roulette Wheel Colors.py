'''On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are
as follows:
• Pocket 0 is green.
• For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered
pockets are black.
• For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered
pockets are red.
• For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered
pockets are black.
• For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered
pockets are red.
Write a program that asks the user to enter a pocket number and displays whether the pocket is green, red, or black.
The program should display an error message if the user enters a number that is outside the range of 0 through 36.
'''
try:
    num = int(input("Please enter the pocket number : "))

except ValueError:
    print("Please enter a number.")

else:
    if num not in range(1,37,1):
        print("The number not in range.")
    elif num == 0:
        print("Green")
    elif num in range(1,19):
        if num%2 == 0:
            print("Red")
        else:
            print("Black")
    elif num in range(19,29):
        if num%2 == 0:
            print("Black")
        else:
            print("Red")
    elif num%2 == 0:
        print("Red")
    else:
        print("Black")

