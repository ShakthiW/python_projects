i = 7
j = 6
space = 0

while i != 0:
    print("*" * i)
    i -= 1
    continue

while j != 0:
    print(f"#", " " * space, "#", sep="")
    space += 1
    j -= 1
    continue

