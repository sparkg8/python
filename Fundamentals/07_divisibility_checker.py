"""
is the number divisible
divisible by 3 and 5: print Divisible by both
by 3: The number is divisible by 3
by 5: the number is divisible by 5
none: The number is not divisible by 3 nor by 5

"""

number = int(input("Enter a number: "))

if number%3 == 0 and number%5 == 0:
    print(f"The number {number} is divisible by both.")
elif number%3 == 0:
    print(f"The number {number} is divisible by 3.")
elif number%5 == 0:
    print(f"The number {number} is divisible by 5.")
else:
    print(f"The number is not divisoble by 3 nor by 5.")