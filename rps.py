import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = input(f"\n{name}, please enter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n")

        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(player_choice)

        computer_choice = random.choice("123")

        computer = int(computer_choice)

        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', "")}.")
        print(f"🐍 chose {str(RPS(computer)).replace('RPS.', "")}.")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return "🥳🥳 {name}, you Win 🥳🥳"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🥳🥳 {name}, you Win 🥳🥳"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🥳🥳 {name}, you Win 🥳🥳"
            elif player == computer:
                return "🙌🙌 Game Tied 🙌🙌"
            else: 
                python_wins += 1
                return "🐍🐍 Python Wins 🐍🐍"
            
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"Python Wins: {python_wins}")

        print("\nPlay Again, {name}?")
        while True:
            play_again = input("Y for Yes or \nQ to Quit \n\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉")
            print("Thank you for Playing")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}👋\n")
            else:
                return  
    
    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )
    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()