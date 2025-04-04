
import random

def rock_paper_scissors():
    # Game choices
    choices = ["rock", "paper", "scissors"]

    while True:
        # Player choice
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

        if player_choice == "quit":
            print("Thanks for playing! Goodbye. 👋")
            break

        if player_choice not in choices:
            print("❌ Invalid choice! Please enter rock, paper, or scissors.")
            continue

        # Computer choice
        computer_choice = random.choice(choices)

        # Display choices
        print(f"\nPlayer chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        # Winner decision
        if player_choice == computer_choice:
            print("🔄 It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win!")
        else:
            print("💻 Computer wins!")

        print("\n--------------------------\n")

# Run the game
rock_paper_scissors()
