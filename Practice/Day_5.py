"""
Password generator
"""
import random

letters = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letters_upper = []
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','#','$','%','&','(',')','*','+']


for l in letters:
    l = l.upper()
    letters_upper.append(l)

all_letters = letters + letters_upper

print("Welcome to the Python Password generator!\n")
usr_letters = int(input("How many letters you need?\n"))
usr_numbers = int(input("How many numbers you want in your password?\n"))
usr_symbols = int(input("How many symbols are in your password?\n"))

password = []

for char in range(1, usr_letters + 1):
    password.append(random.choice(all_letters)) 

for char in range(1, usr_symbols+1):
    password.append(random.choice(symbols))

for char in range(1, usr_numbers+1):
    password.append(random.choice(numbers))

#shuffle the characters order
random.shuffle(password)

password2 = ""

for char in password:
    password2 += char

print(f"\nYour final password is: {password2}\n")

"""
lett = random.sample(all_letters, usr_letters)
nums = random.sample(numbers, usr_numbers)
sym_bol = random.sample(symbols, usr_symbols)

#Concatenate all lists elements
passw = lett + nums + sym_bol

# Shuffle the characters in the new list
ran_passw = random.sample(passw, len(passw))

# Create a string variable to store final result
str_passw = ""

# Access the list and concatenate into string all elements
for character in ran_passw:
    str_passw += str(character)

print(f"\nThis is your password: {str_passw}\n")
"""

