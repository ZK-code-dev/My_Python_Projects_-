🔐 DigiCore Password Manager

Welcome to DigiCore – a simple Python password manager to securely store and view your login credentials! 🖥️💾
All your credentials are encrypted before being saved and can be decrypted for viewing when needed.

🕹 How to Use

Run the program. You’ll see a menu:

==== DigiCore Password Manager ====
{1} Add your credentials
{2} View stored credentials
{e} Exit program

Choose an option:

1 → Add a new credential set (website, username, password) ✏️

2 → View all saved credentials 🔍

e → Exit the program 👋

When adding credentials, you’ll be prompted for:

URL/Website 🌐

Username 👤

Password 🔑

All data will be encrypted and saved in digicore_credentials.txt.

Viewing credentials decrypts them and displays in a neat table:

URL_web Username Password

---

example.com myUser123 MyP@ssw0rd

💡 How the Code Works
1️⃣ Global Variables

DIGICORE_CREDENTIALS_FILE → stores credentials in a text file. 📝

char_set → defines the characters recognized for encryption and decryption. 🔣

2️⃣ Encryption & Decryption

encrypted_text(value, shift=3) → shifts each character forward in the char_set. 🔒

decrypted_text(encrypted_value, shift=3) → reverses the shift to get original text. 🔓

Unknown characters are left unchanged.

Comments in the code may include info about looping through characters and the index calculations, or just my notes while coding. 📝

3️⃣ Saving & Viewing Credentials

save_login_info(URL_web, Username, Password) → encrypts and appends credentials to the file.

view_saved_logins() → decrypts saved credentials and prints them in a formatted table.

The code handles missing files, blank lines, and ensures readability.

4️⃣ Menu System

DigiCore_Menu() → looped menu to allow:

Adding credentials

Viewing credentials

Exiting program

Input validation ensures only 1, 2, or e are accepted. ⚠️

5️⃣ Program Flow

The menu runs in a loop until the user chooses to exit. 🔄

Encryption ensures stored passwords aren’t readable in plain text. 💪

🖥 Example Usage
==== DigiCore Password Manager ====
{1} Add your credentials
{2} View stored credentials
{e} Exit program
Please choose an option: 1
URL_web: example.com
Username: myUser123
Password: MyP@ssw0rd
Your details have successfully been saved!

==== DigiCore Password Manager ====
{1} Add your credentials
{2} View stored credentials
{e} Exit program
Please choose an option: 2

Saved User Credentials:

URL_web Username Password

---

example.com myUser123 MyP@ssw0rd

⚙️ Features

Secure storage with custom character shift encryption 🔐

User-friendly menu navigation 🖥️

Handles invalid inputs gracefully ⚠️

Stores credentials in a text file for persistent access 💾

Easy to extend for more security features in the future 🌟

📌 Notes

Some comments reflect earlier code ideas or versions, which is useful for learning or future improvements. 💡

The program can be expanded with features like password generation, stronger encryption, or multiple user support. 🚀

🎉 DigiCore makes storing and accessing your credentials simple, safe, and organized! 🔑✨
