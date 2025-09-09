🎲 Dice Rolling Game

Welcome to the Dice Rolling Game! This is a simple, fun game where you can roll two dice as many times as you like. Perfect for testing your luck or just having a bit of fun with code! 😄

🕹 How to Play

When you run the game, it will ask:

Roll the dice? (y/n):

Type y to roll the dice. 🎲

Type n to exit the game. ❌

If you type anything else, the game will ask you to enter a valid option. ⚠️

If you choose y, the game will randomly generate two numbers between 1 and 6 (just like rolling real dice) and show the result:

You rolled a (3, 5)!

After each roll, you can choose to roll again or exit. The game continues until you type n.

If you type n, the game will say:

Thank you for playing!

and then stop. 🎉

💡 How the Code Works

The game uses a while loop to keep asking the player if they want to roll again. 🔄

It uses Python’s random.randint(1, 6) to simulate rolling a dice. 🎲

Input is cleaned using .strip().lower() to handle spaces or uppercase letters like Y or N. ✨

Comments in the code explain important parts, like why the loop continues or how invalid input is handled. 📝

Some comments in the code show a short explanation of the game or just my notes while coding it. These are there to explain the thought process and learning journey. You can remove them if you want a cleaner code version. 😎

🖥 Example Gameplay
Roll the dice? (y/n): y
You rolled a (2, 6)!
Roll again? (y/n): y
You rolled a (5, 3)!
Roll again? (y/n): n
Thank you for playing!

⚙️ Features

Continuous rolling until the user exits

Random dice rolls (1–6)

Input validation to prevent mistakes

Friendly messages for fun interaction

🎉 Enjoy rolling the dice and may luck be on your side! 🎲🍀
