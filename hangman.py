"""
CodeAlpha Task 1: Hangman Game
A simple text-based Hangman game played in the console.
"""

import random


WORDS = ["python", "program", "keyboard", "internet", "developer"]
MAX_WRONG = 6


def display_word(word, guessed_letters):
    """Return the word with unguessed letters shown as underscores."""
    shown = []
    for letter in word:
        if letter in guessed_letters:
            shown.append(letter)
        else:
            shown.append("_")
    return " ".join(shown)


def play_game():
    word = random.choice(WORDS)
    guessed_letters = []  
    wrong_guesses = 0

    print("\n=== Welcome to Hangman! ===")
    print(f"I'm thinking of a word with {len(word)} letters.")
    print(f"You can make up to {MAX_WRONG} incorrect guesses.\n")

    while wrong_guesses < MAX_WRONG:
        print("Word:", display_word(word, guessed_letters))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "none")
        print(f"Incorrect guesses left: {MAX_WRONG - wrong_guesses}")

        guess = input("Guess a letter: ").lower().strip()

       
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

       
        if all(letter in guessed_letters for letter in word):
            print("Word:", display_word(word, guessed_letters))
            print(f"Congratulations, you won! The word was '{word}'.")
            return

    print(f"Game over! You ran out of guesses. The word was '{word}'.")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
