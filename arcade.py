import sys 
from rps import rps
from guess_number import guess_number

def play_game(name='PlayerOne'):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade Menu.")

            player_choice = input("\nPlase choose a game:\n 1. Rock Paper Scissors\n2. Guess My Number\n3. Exit the Arcade Menu\n\n")

            if player_choice not in ["1", "2", "3"]:
                print(f"{name}, please choose from 1, 2, or 3.")
                return play_game(name)
            
            welcome_back = True

            if player_choice == 1:
                rock_paper_scissors = rps(name)
                rock_paper_scissors
            elif player_choice == 2:
                guess_the_number = guess_number(name)
                guess_the_number
            elif player_choice == 3:
                print("\nSee you next time\n")
                sys.exit(f"Bye {name} 👋")

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

    print(f"\n{args.name}, welcome to the Arcade 🤖")
    play_game(args.name)
            
