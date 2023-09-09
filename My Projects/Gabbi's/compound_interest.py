# Compound Interest

p = float(input("The amount of principal originally deposited : Rs. "))

r = float(input("The annual interst rate paid by the bank : "))
R = r/100

n = int(input("The number of times per year the interest is compunded : "))

t = int(input("The number of years the account will be left to earn interst : "))

A = p*((1+(R/n))**(n*t))

print(f"The amount of money that will be in the account is Rs. {A} ")


