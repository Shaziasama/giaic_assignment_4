import random

def guess_the_number():
    # Guess number by computer
    number = random.randint(1, 100)
    chances_left = 7

    # Welcome message  
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    # Loop generated
    while chances_left > 0:
        print(f"\nYou have {chances_left} chances left.")
        
        try:
            guess = int(input("Take a guess: "))
        except ValueError: 
            print("Invalid input: Please enter a number.")
            continue

        # Guess the secret number
        if guess < number:
            print("Your number is too low. Try again!")
        elif guess > number:
            print("Your number is too high. Try again!")
        else:
            print("🎉 Congratulations! You got the correct number! 🎉")
            break  # Exit the loop if guessed correctly

        chances_left -= 1  # Reduce the chances

    if chances_left == 0:
        print(f"Sorry, you're out of chances! The correct number was {number}.")

# Run the game
guess_the_number()
