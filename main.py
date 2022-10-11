"""
Title: Hangman
Author: Michał Chojna
Date: 07.06.2022
Description: Hangman game
"""

# Imports modules
import random
import hangman_art
import hangman_words
from replit import clear

# Creates a list of words imported from hangman_words.py
word_list = hangman_words.word_list

# Randomly takes one word from list of words which will be used as word to guess
chosen_word = random.choice(word_list)

# Creates a list to store lower underscores which will represent the hidden letter in the word to guess
display = []

# Creates a list with number of lower underscores the same as number of letters in chosen word
for letter in chosen_word:
    # Adds the lower underscore to the list
    display.append("_")

# Number of player's lives in a game
lives = 6

# Takes a list of available letters imported from hangman_words.py
letters = hangman_words.letter_list

# Takes a list of graphical representation of player's level of life imported from hangman_art.py
stages = hangman_art.stages

# Prints welcome logo imported from hangman_art.py and welcome message
print(hangman_art.logo + "\n")

# Boolean to initialize a game
hangman = True

# While loop to initialize a game
while hangman:

    # Checks if the list which contains lower underscore is not empty
    # And
    # Checks if player's level of life is above 0
    if "_" in display and lives > 0:

        # If these conditions are met the game continues to run
        # Clean the window
        clear()

        # Prints available letters which could be used to guess
        print(f"Available letters: {letters}\n")

        # While loop to take the guessed letter from the player
        while True:

            # Takes player's guess
            guess = input("Guess a letter: ").lower()

            # Checks if the letter given by a player is not already used
            if guess in letters:

                # If letter given by a player is not used
                # Removes guess letter from list of available letters
                letters.remove(guess)

                # Breaks the loop
                break

            # If the letter given by a player is already used
            else:

                # Prints that letter is already used
                print("Letter is already used.\n")

        # Checks if guessed letter given by player is in the word
        if guess in chosen_word:

            # If guessed letter is in the word
            # For loop changes the lower underscore to the give letter
            for index in range(len(chosen_word)):

                # Check if each letter in the world is the guessed letter
                if chosen_word[index] == guess:

                    # If letter in the world is the guessed letter
                    # Changes the lower underscore to the letter
                    display[index] = guess

        # If guessed letter given by a player is not in the word
        else:

            # If guessed letter given by a player is not in the word
            # Players loses 1 life
            lives -= 1

        # Prints the list of lower underscores
        print(f"\n{display}")

        # Prints the graphical interface of player's level of life
        print(stages[lives])

    # Checks if the list of lower underscores does not contain any lower underscore
    # And
    # Checks if the level of life is above 0
    elif "_" not in display and lives > 0:

        # If the list of lower underscore does not contain any lower underscore and player's level of life is above 0

        # Prints the hidden word from list of lower underscores
        print(f"{' '.join(display)}\n")

        # Prints that player wins
        print("You win!")

        # Boolean to finish the game
        hangman = False

    # Check if the player's level of life is below 0
    elif lives <= 0:

        # If player's level of life is below 0
        # Prints the list of lower underscores
        print(f"{' '.join(display)}\n")

        # Prints the hidden word
        print(f"{chosen_word.split}\n")

        # Prints that player loses
        print("You lose!")

        # Boolean to finish the game
        hangman = False
