# codealphatask2
Explanation
Imports and Function Definitions

import random: Imports the random module to randomly select a word from the list.
Function choose_word

This function defines a list of words and randomly selects one word from this list using random.choice.
Function display_word

This function takes the word and a set of guessed_letters as arguments. It constructs and returns a string where each letter in the word is replaced with an underscore if it has not been guessed yet.
Function hangman

This function orchestrates the Hangman game:
Chooses a word using choose_word.
Initializes a set guessed_letters to keep track of guessed letters.
Sets attempts to 6, which is the number of incorrect guesses allowed.
Runs a while loop that continues as long as there are attempts left.
Prompts the user to guess a letter and checks if the input is valid.
Updates the set of guessed letters and checks if the guess is correct.
Prints the current state of the word and remaining attempts.
Ends the game if the word is completely guessed or if attempts run out.
Main Check

The block if __name__ == "__main__": ensures that hangman() runs only if the script is executed directly, not if it is imported as a module.
How to Play
Run the script.
The program will display underscores for the letters in the word and prompt you to guess letters.
For each correct letter, the corresponding underscores will be replaced.
For each incorrect letter, the number of remaining attempts decreases.
The game ends when you guess all letters correctly or run out of attempts.
Feel free to adjust the list of words or the number of attempts to suit your preferences!
