"""
Ask user type two numbers, then prints the greater number
"""

number_one = int(input("Enter a first number: "))
number_two = int(input("Enter a second number: "))

if number_one > number_two:
    print(f"{number_one} is greater than {number_two}\n")
elif number_one < number_two:
    print(f"{number_two} is greater than {number_one}\n")
else:
    print(f"{number_one} and {number_two} are equal numbers\n")
    