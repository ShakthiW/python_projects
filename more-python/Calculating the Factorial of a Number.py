'''
Write a program that lets the user enter a nonnegative integer then uses a loop to calculate the factorial
of that number. Display the factorial.
'''
ans = 1

try:
    num = int(input("Enter the number : "))
except ValueError:
    print("Please enter a whole number.")
else:
    if num < 0:
        print("Please enter a positive number.")
    else:
        for i in range(1,num+1):
            ans *= i

        print(f"The factorial of {num} is {ans}.")
