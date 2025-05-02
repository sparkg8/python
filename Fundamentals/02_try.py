"""
Temperature comparison
less or equal than 20, disply a message that it's cold
greater 20 and less or equal than 30 it is warm
greater than 30 it is hot
"""

temperature = 45

if temperature <= 20:
    print("It is cold\n")
elif temperature > 20 and temperature <= 30:
    print("It is warm\n")
else:
    print("It is hot\n")


