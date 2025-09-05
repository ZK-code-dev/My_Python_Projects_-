import random 

user_input = input("Roll the dice? (y/n): ").strip().lower()
while True:
    if user_input == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"You rolled a ({dice1}, {dice2})!")
        user_input = input("Roll again? (y/n): ").strip().lower() 
    elif user_input == "n":
        print("Thank you for playing!")
        break
    else:
        user_input = input("Invalid option, please enter 'y' to roll or 'n' to exit the game: ").strip().lower()

# This dice rolling game should allow the user to type in an option shown from the message y/n, either to roll or exit,
# if y was chosen, the game should generate two ranom numbers, ask to roll again and continue
# if n was chosen, then the game should exit, showing a thank you message
# else: invalid input wont be accepted and a message will show up asking for a vaild option.
# we should use a loop so the game will continue until user wants to exit.'''