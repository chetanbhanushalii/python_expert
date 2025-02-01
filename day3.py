print("Welcome to Python Pizza Deliveries!")
size = str(input("What size pizza do you want? S, M or L: "))
pepperoni = str(input("Do you want pepperoni on your pizza? Y or N: "))
extra_cheese = str(input("Do you want extra cheese? Y or N: "))

total_price = 0

if size == 'S':
    total_price+=15
    if pepperoni == "Y":
        total_price += 2

elif size == 'M':
    total_price += 20
    if pepperoni == "Y":
        total_price += 3

elif size == 'L':
    total_price += 25
    if pepperoni == "Y":
        total_price += 3
else:
    print("Invalid input!!! Try Again.")

if extra_cheese == "Y":
    total_price += 1

print("Your final bill: ",total_price)