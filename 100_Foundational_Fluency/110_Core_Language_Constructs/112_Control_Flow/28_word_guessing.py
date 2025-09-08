# The foundational logic for a word-guessing game where the user has a limited number of tries.

import random

def word_guessing_game():
    words = ["python", "java", "kotlin", "javascript", "ruby", "swift"]
    word_to_guess = random.choice(words)
    max_attempts = 6
    attempts = 0
    guessed_letters = set()
    correct_letters = set(word_to_guess)

    print("Welcome to the Word Guessing Game!")
    print(f"The word has {len(word_to_guess)} letters.")

    while attempts < max_attempts:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
        print(f"Word: {display_word}")
        print(f"Attempts left: {max_attempts - attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in correct_letters:
            print("Good guess!")
            if correct_letters.issubset(guessed_letters):
                print(f"Congratulations! You've guessed the word '{word_to_guess}' correctly!")
                break
        else:
            attempts += 1
            print("Wrong guess!")

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    word_guessing_game()