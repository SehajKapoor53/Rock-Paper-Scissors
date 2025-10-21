"""
Rock Paper Scissors Game
Author: Sehaj Kapoor
Version: 1.0
Date: October 2025
"""

import random


def get_choices():
    """
    Ask the player for their choice and randomly select the computer's choice.
    Includes input validation to ensure valid entries.
    """
    available_choices = ["rock", "paper", "scissors"]

    while True:
        player_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()

        if player_choice in available_choices:
            break
        else:
            print("❌ Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

    computer_choice = random.choice(available_choices)

    return {"player": player_choice, "computer": computer_choice}


def determine_winner(player: str, computer: str) -> str:
    """
    Determine the result of the Rock-Paper-Scissors match.
    Returns a message describing whether the player won, lost, or tied.
    """
    print("\n==============================")
    print(f"🧍 You chose: {player}")
    print(f"💻 Computer chose: {computer}")
    print("==============================")

    if player == computer:
        return "🤝 It's a tie!"

    match player:
        case "rock":
            match computer:
                case "paper":
                    return "😢 You lost!"
                case "scissors":
                    return "🎉 You won!"
        case "paper":
            match computer:
                case "rock":
                    return "🎉 You won!"
                case "scissors":
                    return "😢 You lost!"
        case "scissors":
            match computer:
                case "paper":
                    return "🎉 You won!"
                case "rock":
                    return "😢 You lost!"


def play_game():
    """
    Main loop that runs the Rock-Paper-Scissors game.
    """
    print("=== Welcome to Rock Paper Scissors ===")

    while True:
        choices = get_choices()
        result = determine_winner(choices["player"], choices["computer"])
        print(result)

        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        print()

        if again != "y":
            print("👋 Thanks for playing! See you next time.")
            break


# Start the game
if __name__ == "__main__":
    play_game()
