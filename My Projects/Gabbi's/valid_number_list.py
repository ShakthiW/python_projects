# valid number Information
'''
Design a program that uses a loop to build a list named valid_numbers
that contains only the numbers between 0 and 100 from the numbers list below.
The program should then determine and display the total and average of
the values in the valid_numbers list.

'''

valid_numbers = []
total = 0

numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

for number in numbers:
    if number in range(0,101):
        valid_numbers.append(number)

print(valid_numbers)
