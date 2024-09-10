import random

def choose_word():
    # List of predefined words
    words = ['python', 'hangman', 'programming', 'developer', 'code']
    # Randomly select a word from the list
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with guessed letters revealed and unguessed letters as underscores
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    # Game setup
    word = choose_word()  # Choose a word from the predefined list
    guessed_letters = set()  # Set of guessed letters
    attempts = 6  # Number of attempts allowed
    guessed_word = set()  # To track the correctly guessed letters
    
    print("Welcome to Hangman!")
    print("Try to guess the word before you run out of attempts.")
    
    while attempts > 0:
        # Display the current state of the word
        print(display_word(word, guessed_letters))
        
        # Ask the user for a letter guess
        guess = input("Guess a letter: ").lower()
        
        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        # Add the guessed letter to the set
        guessed_letters.add(guess)
        
        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_word.add(guess)
        else:
            # If the letter is not in the word, reduce the number of attempts
            attempts -= 1
            print(f"'{guess}' is not in the word. You have {attempts} attempts left.")
        
        # Check if the user has guessed all letters in the word
        if guessed_word == set(word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        # If the loop exits without breaking, the user has run out of attempts
        print(f"Sorry, you're out of attempts. The word was: {word}")

# Run the game
if __name__ == "__main__":
    hangman()