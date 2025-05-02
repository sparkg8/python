"""
Ask the age, and classify it in these cathegories 
Child: < 12
Teenager: > 12 and < 19
Adult: >= 20
"""

usr_age = int(input("How old are you? "))

if usr_age <= 12:
    print("You are a Child\n")
elif usr_age > 12 and usr_age < 19:
    print("You are a Teenager\n")
else:
    print("You are an Adult\n")