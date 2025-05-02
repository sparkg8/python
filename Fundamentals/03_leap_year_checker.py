"""
Leap Year Checker
ask user:
    leap year is divisible by 4, but 100, or divisible by 400
"""
year = int(input("Ingresa el año: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} Es un año bisiesto. ")
else:
    print(f"{year} no es un año bisiesto.\n")
