import random
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwd_generator =[]

pwd_letter_count = random.choices(letters,k=nr_letters)
pwd_generator.append(pwd_letter_count)

pwd_symbols_count = random.choices(symbols,k=nr_symbols)
pwd_generator.append(pwd_symbols_count)

pwd_numbers_count = random.choices(numbers,k=nr_numbers)
pwd_generator.append(pwd_numbers_count)

pwd =''
for e in pwd_generator:
    for i in e:
        pwd = pwd + i

str_to_list = list(pwd) #convert str to list

random.shuffle(str_to_list) #shuffle the list for random arrangement for letters
print("your password is: ", "".join(str_to_list))