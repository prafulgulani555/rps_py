import sys
import random
from enum import Enum

def play_rps():
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

    print("\nYou chose " + str(RPS(player)).replace('RPS.', "") + ".")
    print("Computer chose " + str(RPS(computer)).replace('RPS.', "") + ".\n")

    if player == 1 and computer == 3:
        print("You Win 🥳")
    elif player == 2 and computer == 1:
        print("You Win 🥳")
    elif player == 3 and computer == 2:
        print("You Win 🥳")
    elif player == computer:
        print("Tie Game 🙌")
    else: 
        print("Python Wins 🐍")

    print("\nPlay Again?")

    while True:
        play_again = input("\nY for Yes or \nQ to Quit \n\n")
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

play_rps()