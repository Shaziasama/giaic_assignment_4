#project8 Hamgman game

import random
words = ["python", "typescript", "javascript"]

word = random.choice(words)
guesses_file = []
attempt = 6

print("welcome to Hangman game")
print("_" * len(words))

while attempt > 0:
    guess = input("\n Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter")
        continue
    if guess in guesses_file:
        print("this letter is already guess chose another letter")
        continue
    guesses_file.append(guess)
    if guess in word:
        print("Good guess")
    else:
        attempt -= 1
        print(f"Wrong {attempt} attempts")

        display_word = "" .join([letter if letter in guess else "_" for letter in word])
        print(display_word)
        if "_" not in display_word:
            print(f" congratatulations! the correct word is: {word}")
            break
        else:
            print(f"Game over! the correct word is: {word}")

