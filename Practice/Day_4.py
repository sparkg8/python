""" 
Nested lists
"""
"""
fruits = ["apple", "banana", "peach", "strawberry"]
vegetables = ["letuce", "spinach", "brocoli"]
nested_list = [fruits, vegetables]

print(nested_list[1][2])

"""
"""
RULES:
    - Rock wind against scissors
    - Scissors win against paper
    - Paper wins against rock
"""
rock = """
       _____
 ____.' _ _ )_ 
        (_ _ _)
        (_ _ _)        "Chose Rock"
____    ( _ _)
    '--(_ _)

"""

paper = """
     _ _ _ 
___.' _ _ _)_ 
     _ _ _ _ _)
       _ _ _ _ _)       "Chose Paper"
       _ _ _ _ )
----._ _ _ _ )
    

"""

scissors = """

     _ _ _ 
----' _ _ )_ _ _
       _ _ _ _ _)_
       _ _ _ _ _ _)     "Chose Scissors"
      (_ _ _)
-----.(_ _ )
     
       
"""
import random

user_choice = input("Rock, Paper, Scissors (r, p, s)\n").lower()
computer = [rock, paper, scissors]
size = len(computer)

computer_choice = random.randint(0, size)

print("=================° Welcome to Rock, Paper, Scissors game °====================================")
if user_choice == 'r':
    print(f"You {rock}\n")
    if computer_choice == 0:
        print(f"Computer {rock}\n")
        print("It's a Tie\n")
    elif computer_choice == 1:
        print(f"Computer {paper}\n")
        print("Computer won!!\n")
    else:
        print(f"Computer {scissors}\n")
        print("Congratulations you Won!!!\n")

# user selection (Paper)
if user_choice == 'p':
    print(f"You {paper}\n")
    if computer_choice == 1:
        print(f"Computer {paper}\n")
        print("It's a Tie\n")
    elif computer_choice == 2:
        print(f"Computer {scissors}\n")
        print("Computer won!!\n")
    else:
        print(f"Computer {rock}\n")
        print("Congratulations you Won!!!\n")

# user selection (Paper)
if user_choice == 's':
    print(f"You {scissors}\n")
    if computer_choice == 2:
        print(f"Computer {scissors}\n")
        print("It's a Tie\n")
    elif computer_choice == 0:
        print(f"Computer {rock}\n")
        print("Computer won!!\n")
    else:
        print(f"Computer {paper}\n")
        print("Congratulations you Won!!!\n")
    
