"""
Ask the user to enter a number, and tells wether it is a positive or negative number
"""

number = int(input("Enter a number: "))

if number >= 0:
    print(f"{number} is a Positive number\n")
else:
    print(f"{number} is a negative number\n")