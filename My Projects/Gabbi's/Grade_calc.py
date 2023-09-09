# Grade Calculator

grade = None

def test_check(display, upper_range = 25, lower_range = 0):
    while True:
        try:
            mark = int(input(display))

        except ValueError:
            print("Please enter a number.")

        else:
            if mark > upper_range or mark < lower_range:
                print("Invaild mark. Out of range!")
                continue
            else:
                return mark

while True:    
    test_1 = test_check("Enter the marks for the test 01: ")

    test_2 = test_check("Enter the marks for the test 02: ")

    exam = test_check("Enter the marks for the exam: ", 50)

    tot = test_1 + test_2 + exam

    if tot > 49 and exam > 24:
        if tot > 80:
            grade = "Distinction"

        elif tot > 60:
            grade = "Credit"

        else:
            grade = "Pass"

    else:
        print("You've failed the exam!")
        break

    print(f"You have a {grade} as the overall result.")
    break
