"""Practoce, desition game"""
import ascii_chars

print(ascii_chars.msg)

print("Wellcome to the desition game.")
print("You're mission will be to find the correct answear\n")

response1 = input("There are two ways left or right? L or R\n")


if response1 == 'L':
    print("Game Over - you lose\n")
elif response1 == 'R':
    print("Good choice, keep going!\n")

    response2 = input("What do you prefer to cross the sea? swim or wait\n")
    if response2 == 'swim':
        print("Game Over")
    elif response2 == 'wait':
        print("Now you can build a boat.\n")
    
        response3 = input("Do you manage to build a boat? Y or N\n")
        if response3 == 'Y':
            print("Congrats, you can go to te treasure island now\n")
        else:
            print("It's dangerous going to the island without a boat")
            print("* Game Over *\n")
else:
    print("\nInvalid answear...\n")


