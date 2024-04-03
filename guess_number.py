import sys
import random

def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    wrong_guess = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins
        nonlocal wrong_guess

        player_choice = input(f"\n{name}, Guess the number I'm thinking... 1, 2 or 3\n")

        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please choose from 1, 2, or 3.")
            return play_guess_number()

        computer_choice = random.choice("123")

        print(f"\n{name}, you chose {player}.")
        print(f"I was thinking about the number {computer_choice}.")

        player = int(player_choice)
        computer = int(computer_choice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal wrong_guess

            if player == computer:
                player_wins += 1
                return "🥳🥳 {name}, You Win 🥳🥳"
            else: 
                wrong_guess += 1
                return "🐍🐍 Wrong guess 🐍🐍"
            
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"\nWin Percentage: {player_wins/game_count:.2%}")

        print(f"\nPlay Again, {name}?")
        while True:
            play_again = input("Y for Yes or \nQ to Quit \n\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_guess_number()
        else:
            print("\n🎉🎉🎉")
            print("Thank you for Playing")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}👋\n")
            else:
                return      
    
    return play_guess_number


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

    guess_the_number = guess_number(args.name)
    guess_the_number()