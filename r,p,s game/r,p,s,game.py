# the first comment (from line 1-38) is how we coded the game at first go,
# but then Mosh advised us to do somehting called modularization,
# meaning we should break the code into smaller parts,
# so we did that and now we have a newer cleaner code below
# youtube: python projects for beginners (mosh hamedani)

""" 
import random

while True:
    print("Let's play Rock, Paper, Scissors!")
    choices = ["r", "p", "s"]
    emoji_dict = {"r": "✊", "p": "✋", "s": "✌️"}
    user_input = input("Rock, Paper, or Scissors? (r/p/s): ").strip().lower()
    computer_choice = random.choice(choices)

    if user_input not in choices:
        print("Invalid input, please enter (r/p/s).")
        continue

    print(f"You chose {emoji_dict[user_input]}")
    print(f"Computer chose {emoji_dict[computer_choice]}")

    if computer_choice == user_input:
        print("It's a tie!")
    elif (
        (user_input == "r" and computer_choice == "s") or
        (user_input == "p" and computer_choice == "r") or
            (user_input == "s" and computer_choice == "p")):
        print("You win, well done!!")
    else:
        print("You lose, better luck next time!")

    play_again = input("Want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        print("Thanks for playing!")
        break
"""

import random

emoji_dict = {"r": "✊", "p": "✋", "s": "✌️"}
choices = ["r", "p", "s"]


def get_user_choice():
    while True:
        user_input = input(
            "Rock, Paper, or Scissors? (r/p/s): ").strip().lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice!")


def display_choices(user_input, computer_choice):
    print(f"You chose {emoji_dict[user_input]}")
    print(f"Computer chose {emoji_dict[computer_choice]}")


def determine_winner(user_input, computer_choice):
    if computer_choice == user_input:
        print("It's a tie!")
    elif (
            (user_input == "r" and computer_choice == "s") or
            (user_input == "p" and computer_choice == "r") or
            (user_input == "s" and computer_choice == "p")):
        print("You win, well done!!")
    else:
        print("You lose, better luck next time!")


def play_game():
    while True:
        user_input = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_input, computer_choice)
        determine_winner(user_input, computer_choice)

        play_again = input("Want to play again? (y/n): ").strip().lower()
        if play_again == "n":
            break


play_game()
