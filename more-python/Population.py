try:
    start = int(input("Enter the starting number of organisms : "))
except ValueError:
    print("Please enter a whole number.")
else:
    try:
        inc = float(input("Enter the average daily increment as a percentage : "))
    except ValueError:
        print("Please enter a number")
    else:
        try:
            no_days = int(input("Enter the numb.er of days to multiply : "))
        except ValueError:
            print("Please enter a whole number.")
        else:
            population = start

            print("Day\t\t\t\t\tApproximate Population")
            for day in range(1, no_days+1):
                print(f"{day}\t\t\t\t\t{round(population, 3)}")

                population *= (inc+100)/100
