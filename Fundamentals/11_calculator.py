"""
Calcuator: Ask user to enter two numbers and a operator sign (+, -, *, /)
"""

num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter a number: "))
answ = input("What to calculate +, -, *, / : ")

if answ == '+':
    print(f"{num_1} + {num_2} = {num_1+num_2}")
elif answ == '-':
    print(f"{num_1} - {num_2} = {num_1 - num_2}")
elif answ == '*':
    print(f"{num_1} * {num_2} = {num_1*num_2}")
elif answ == '/':
    print(f"{num_1} / {num_2} = {num_1/num_2}")
else:
    print("Enter a valid answear\n")


