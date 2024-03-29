import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

play_again = True

while play_again:

    player_choice = input("\nEnter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n")

    player = int(player_choice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1,2, or 3.")

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

        play_again = input("\nPlay Again? \nY for Yes or \n Q to Quit \n\n")

        if play_again.lower() == "y":
            continue
        else:
            print("\n🎉🎉🎉")
            print("Thank you for Playing\n")
            play_again = False

sys.exit("Bye 👋")