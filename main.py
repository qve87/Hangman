"""
Simple version of famous game HANGMAN.
"""

import random
from art import stages, logo
from words_list import word_list

LIVES = 6

print(logo)
chosen_word = random.choice(word_list)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#  Adding '_' to the display list with an amount equal to number of letters in chosen word
display = ["_" for _ in range(len(chosen_word))]
used_letters = []

is_game_on = False

while not is_game_on:

    while True:

        print(f"Lives: {LIVES}")
        print(f"Word to guess: {' '.join(display)}\n")

        guess = input("Guess a letter: ").lower()

        if len(guess) > 1:    # Checking if user type more than one letter
            print("Type only one letter\n")
        elif guess.isdigit():  # Checking if user type number
            print(f"{guess} is not a letter. Try again.\n")
        # Checking if user already guessed a letter or a letter was already used
        elif guess in display or guess in used_letters:
            print(f"You've already chosen {guess}. Choose a different letter\n")
        else:
            used_letters.append(guess)
            break

    for i in range(len(chosen_word)):
        if chosen_word[i] in guess:
            display[i] = guess

    if guess not in chosen_word:
        LIVES -= 1
        print(f"Letter {guess} is not in the word. You have {LIVES} lives.\n")
        if LIVES == 0:
            print("You lose")
            is_game_on = True

    if "_" not in display:
        print("You won!\nThanks for playing!")

    print(" ".join(display), end="\n\n")
    print(f"Used letters: {', '.join(used_letters)}")
    print(stages[LIVES])


