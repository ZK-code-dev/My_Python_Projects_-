🔍 Mystery Number Guessing Game

Welcome to the Mystery Number Guessing Game! 🕵️‍♀️
Test your intuition and luck by trying to guess the mystery number between 1 and 100. Can you find it? 🎯

🕹 How to Play

When you run the game, it will ask you:

Can you guess the mystery number between 1 and 100?

Type a number between 1 and 100.

If your guess is too low, the game will say:

Too low! Try again.

If your guess is too high, it will say:

Too high! Try again.

If your guess is correct, the game will congratulate you:

Congratulations! You've guessed the mystery number!

After guessing correctly, you can choose to start a new game or exit:

New game or exit? (y/n):

y → start a new round with a new mystery number 🔄

n → exit the game 👋

Any other input → the game will ask for a valid option ⚠️

The game continues until you decide to exit.

💡 How the Code Works

The game uses nested while loops:

Outer loop → repeats the game until the player chooses to exit. 🔁

Inner loop → continues asking the player to guess until the mystery number is found. 🔢

The mystery number is generated using random.randint(1, 100). 🎲

Input is validated using a try/except block:

Non-integer inputs show an error message. ❌

Numbers outside 1–100 are rejected. ⚠️

🖥 📝Example Gameplay
Can you guess the mystery number between 1 and 100? 50
Too low! Try again.
Can you guess the mystery number between 1 and 100? 75
Too high! Try again.
Can you guess the mystery number between 1 and 100? 63
Congratulations! You've guessed the mystery number!
New game or exit? (y/n): y

⚙️ Features

Randomly generates a mystery number each round 🎲

Input validation for numbers and invalid entries ✅

Repeats the game until the player wants to exit 🔄

Friendly messages and interactive prompts 😄

🎉 Try your luck and see how quickly you can guess the mystery number! 💯✨
