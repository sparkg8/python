"""
Ask time in 24hr format.
if hour is between 0 - 11, Good Morning
if hour is between 12 - 17, Good afternoon
if it is between 18 - 23, Good evening
"""

usr_time = int(input("Enter tie in 24Hr format: "))

if usr_time >= 0 and usr_time <= 11:
    print("Good morning!\n")
elif usr_time > 11 and usr_time < 18:
    print("Good afternoon!\n")
elif usr_time > 17 and usr_time < 24:
    print("Good evening!")



