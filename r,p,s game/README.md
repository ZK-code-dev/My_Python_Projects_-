✊✋✌️ Rock, Paper, Scissors Game

Welcome to your Rock, Paper, Scissors game! 🎮
Try your luck against the computer and see who wins! 🏆

🕹 How to Play

Run the game. You will be prompted:

Rock, Paper, or Scissors? (r/p/s):

r → Rock ✊

p → Paper ✋

s → Scissors ✌️

The computer will also make a choice, and the game will show both:

You chose ✊  
Computer chose ✌️

The winner is determined:

Tie: "It's a tie!" ⚖️

Player wins: "You win, well done!!" 🎉

Computer wins: "You lose, better luck next time!" 😅

After each round, you can choose to play again (y) or exit (n).

💡 How the Code Works
1️⃣ First Version (Commented Out)
"""
import random
while True:
...
"""

The first part of the code (the commented out code line 1-38) shows our first attempt at coding the game.

Mosh Hamedani advised that as beginners this is fine, but we could make the code simpler, shorter, and easier to maintain by breaking it into smaller parts (modularization).

So we created a cleaner, modular version below. ✅

You can watch his tutorial here: Python Projects for Beginners - Mosh Hamedani

2️⃣ Modular Version

get_user_choice() → handles user input and ensures it’s valid. ✅

display_choices() → prints both the player’s and computer’s choices. 👀

determine_winner() → compares choices and decides who wins. 🏆

play_game() → main game loop that calls the other functions and asks if you want to play again. 🔄

Modularization makes the code easier to read, maintain, and reuse for other projects.

🖥 Example Gameplay
Rock, Paper, or Scissors? (r/p/s): r
You chose ✊
Computer chose ✌️
You win, well done!!

Want to play again? (y/n): n
Thanks for playing!

⚙️ Features

Handles invalid input gracefully ⚠️

Displays choices with emojis ✨

Modularized for clean, readable code 🧩

Lets you play multiple rounds 🔄

🎉 Have fun playing Rock, Paper, Scissors and see if you can beat the computer! ✊✋✌️
