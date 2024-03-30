import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = input("\nEnter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n")

        if player_choice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()

        player = int(player_choice)

        computer_choice = random.choice("123")

        computer = int(computer_choice)

        print("\n🫵  chose " + str(RPS(player)).replace('RPS.', "") + ".")
        print("🐍 chose " + str(RPS(computer)).replace('RPS.', "") + ".")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return "🥳🥳 You Win 🥳🥳"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🥳🥳 You Win 🥳🥳"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🥳🥳 You Win 🥳🥳"
            elif player == computer:
                return "🙌🙌 Game Tied 🙌🙌"
            else: 
                python_wins += 1
                return "🐍🐍 Python Wins 🐍🐍"
            
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame count: " + str(game_count))
        print("Player wins: " + str(player_wins))
        print("Python Wins: " + str(python_wins))

        print("\nPlay Again?")
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
            sys.exit("Bye 👋\n")      
    
    return play_rps

play = rps()

play()