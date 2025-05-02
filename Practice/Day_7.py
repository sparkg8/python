"""
HANGMAN GAME

"""
import random
stages = [
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
  LOSE  |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
 
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
]
# Create a list of words and chose one randomly
word_list = ["ardvark", "baboon", "camel"]
display = []

chosen_word = random.choice(word_list)

# ask user to guess a letter and store it as lower case
print("\nHint: ", chosen_word)

for _ in range(len(chosen_word)):
    display += "_"

print("\n", display)

end_of_game = False
lives = len(stages)

while not end_of_game:

    guess = input("\nGuess a letter: ").lower()
    # compare the guess letter with the chosen word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:           
            end_of_game = True
            print("You Lose.\n")
        print(f"Lives: {lives}")

    print(display, "\n")
    #lose condition
        
        
    # Win condition
    if "_" not in display:
        end_of_game = True
        print("You Win!\n")









