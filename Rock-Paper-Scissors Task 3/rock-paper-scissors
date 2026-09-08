import random

# Game choices
choices = ["rock", "paper", "scissors"]

# Score
user_score = 0
computer_score = 0

print("=" * 45)
print("     ROCK - PAPER - SCISSORS GAME")
print("=" * 45)

print("\nRules:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")

while True:

    # User input
    user_choice = input(
        "\nEnter your choice (rock/paper/scissors): "
    ).lower()

    # Check valid input
    if user_choice not in choices:
        print("❌ Invalid choice! Please enter rock, paper, or scissors.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    # Display choices
    print("\nYour choice      :", user_choice)
    print("Computer choice  :", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("🤝 Result: It's a TIE!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "scissors" and computer_choice == "paper")
        or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("🎉 Result: YOU WIN!")
        user_score += 1

    else:
        print("😔 Result: COMPUTER WINS!")
        computer_score += 1

    # Display score
    print("\n-------------------------")
    print("       SCORE")
    print("-------------------------")
    print("Your Score     :", user_score)
    print("Computer Score :", computer_score)

    # Play again
    play_again = input(
        "\nDo you want to play again? (yes/no): "
    ).lower()

    if play_again != "yes":
        break

# Final result
print("\n" + "=" * 45)
print("             FINAL SCORE")
print("=" * 45)

print("Your Score     :", user_score)
print("Computer Score :", computer_score)

if user_score > computer_score:
    print("🏆 Congratulations! You are the overall winner!")

elif computer_score > user_score:
    print("💻 Computer is the overall winner!")

else:
    print("🤝 The game ended in a tie!")

print("\nThank you for playing! 😊")