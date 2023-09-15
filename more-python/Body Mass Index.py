'''Write a program that calculates and displays a person’s body mass index (BMI).
The BMI is often used to determine whether a person is overweight or underweight for his or her height.
A person’s BMI is calculated with the following formula:
BMI 5 weight 3 703/height2
where weight is measured in pounds and height is measured in inches.
The program should ask the user to enter his or her weight and height, then display the user’s BMI.
The program should also display a message indicating whether the person has optimal weight, is underweight, or is overweight.
A person’s weight is considered to be optimal if his or her BMI is between 18.5 and 25.
If the BMI is less than 18.5, the person is considered to be underweight.
If the BMI value is greater than 25, the person is considered to be overweight.
'''

try:
    weight = float(input("Enter the weight in pounds : "))
    height = float(input("Enter the height in inches : "))

except ValueError:
    print("Enter a number for the height and weight!")

else:
    BMI = weight * (703/height**2)

    if BMI < 18.5:
        state = "Underweight"

    elif BMI > 25 and BMI < 18.5:
        state = "Optimal"

    elif BMI > 25:
        state = "Overweight"

    print(f"Your BMI is {round(BMI,3)} and you are {state}.")

