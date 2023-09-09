# Restaurant Selector

choices = ['Joe’s Gourmet Burgers','Main Street Pizza Company','Corner Café','Mama’s Fine Italian','The Chef’s Kitchen']

vegetarian = input("Is anyone in your party a vegetarian? (Yes/ No) ").lower()
vegan = input("Is anyone in your party a vegan? (Yes/ No) ").lower()
gluten_free = input("Is anyone in your party gluten-free? (Yes/ No) ").lower()

if vegetarian == 'yes':
    del choices[0]
    if vegan == 'yes':
        del choices[0]
        del choices[-2]
        
    elif gluten_free == 'yes':
        del choices[-2]

elif vegan == 'yes':
    del choices[0:1]
    del choices[-2]

elif gluten_free == 'yes':
    del choices[0]
    del choices[-2]

print(f"Here are the restaurant choices: ")

for choice in choices:
    print("\t",choice)
