# wifi Diagnostic tree

list_questions = [
    "Reboot the computer and try to connect.",
    "Reboot the router and try to connect.",
    "Make sure the cables between the router and modem are plugged in firmly.",
    "Move the router to a new location.",
    "Get a new router"
    ]

print("Dear Customer we are sorry to hear that you have come up with a problem in your router 😢")

for question in list_questions:
    print(question)
    
    if question == "Get a new router":
        break
    
    ans = input("Did that fix the problem? ")

    if ans == 'yes':
        break

    else:
        continue

print("Thank you for using our service. Have a nice day")
