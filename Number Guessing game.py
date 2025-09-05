import random

while True:
    mystery_number = random.randint(1, 100)
    while True:
        try:
            user_input = int(
                input("Can you guess the mystery number between 1 and 100? ").strip())
            if not 1 <= user_input <= 100:
                print("Enter a number between 1 and 100")
                continue
            if user_input < mystery_number:
                print("Too low! Try again.")
            elif user_input > mystery_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You've guessed the mystery number!")
                break
        except ValueError:
            print("invalid input, please enter a numeber from 1 to 100")
    while True:
        play_again = input("New game or exit? (y/n): ").strip().lower()
        if play_again == "n":
            print("Thanks for playing!")
            break
        elif play_again == "y":
            break
        else:
            print("Invalid option, please enter 'y' or 'n'.")
    if play_again == "n":
        print("Thanks for playing!")
        break
