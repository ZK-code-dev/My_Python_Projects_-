import os 
import string as s 

    #---Global Variables---
DIGICORE_CREDENTIALS_FILE = "digicore_credentials.txt"  #file that stores credentials
char_set = s.ascii_letters + s.digits + s.punctuation  # characters recognized in the program for encryption/decryption


    # == Encryption + Decryption defined functions == 

def encrypted_text(value, shift = 3):   #defined the function, moves 4 char forward in encryption.
    encrypted_text = ""        # empty string, that'll contain the encrypted message later on. 


    for char in value:            #loops through every character.  
        origin_index = char_set.find(char)      # finds the index position of the character in char_set. 

        if origin_index != -1:   # when not equivelent to an unknown char. 
            encrypted_index = (origin_index + shift) % len(char_set)     #shifts forward + wraps around 
            encrypted_text += char_set[encrypted_index]

        else: 
            encrypted_text += char    # keep char unchanged in output if it can't be encrypted.

    return encrypted_text

def decrypted_text(encrypted_value, shift = 3):
    decrypted_text = ""

    for char in encrypted_value:
        origin_index = char_set.find(char)

        if origin_index != -1:
            decrypted_index = (origin_index - shift) % len(char_set)  #shifts backwards + wraps around
            decrypted_text +=char_set[decrypted_index]

        else:
            decrypted_text += char

    

    return decrypted_text        


        # === Saving and Displaying Credentials ===

def save_login_info(URL_web, Username, Password):  # encrypted credentials will be saved to file.
    with open(DIGICORE_CREDENTIALS_FILE, "a" ) as file:  #'a' = mode append, adds data to file without erasing existing content.
        encrypted_URL_web = encrypted_text(URL_web)
        encrypted_Username = encrypted_text(Username)
        encrypted_Password = encrypted_text(Password) 
        # Credentials should be formatted as : URL_web, username, password and separated by commas for better reading. 
        # Use'\n' to add a new line after new entries so new data will be saved on new lines. 
        file.write(f"{encrypted_URL_web}, {encrypted_Username}, {encrypted_Password}\n")  

def view_saved_logins(): 
    if not os.path.exists(DIGICORE_CREDENTIALS_FILE):  # First we needed to check if the file exists. 
        print("\nOops! Looks like there are no credentials saved yet.\n")  # Inform user here
        return    # exits if no function is found.

    print("\nSaved User Credentials: \n")  # Chose a heading for the contents of the credential file. 
    print(f"{'URL_web':<35} {'Username':<35} {'Password':<35}")   
    print("_" * 90)         # In this stage we printed the headings + format of the table. 


    with open(DIGICORE_CREDENTIALS_FILE, "r") as file:  # we open file in "r" = read mode. 
        for line in file:           # goes through file line by line
            if line.strip():        # remove any blank lines if found.
                encrypted_URL_web, encrypted_Username, encrypted_Password = [item.strip() for item in line.strip().split(",")]
                URL_web = decrypted_text(encrypted_URL_web)
                Username = decrypted_text(encrypted_Username)
                Password = decrypted_text(encrypted_Password)
                print(f"{URL_web:<25} {Username:<25} {Password:<25}") 
""" The last few steps where splitting the line into encrypted URL_web, Username and Password using ","
    as a separator for formating purposes. Then we decrypted each encrypted values to get the original input,
    Then we print out the decrypted credentials in columns. """


                # == Implementing Menu System ==
def DigiCore_Menu():
    #Made Loop for navigating menu options.
    while True:
        print("\n==== DigiCore Password Manager ====") 
        print("{1} Add your credentials")
        print("{2} View stored credentials")
        print("{e} Exit program")

        option = input("Please choose an option: ")  # First asking user to choose an option, user input then returned as a string.  

        # Option one is choosing credentials, asking user for login info. 
        if option == '1':
            URL_web = input("URL_web: ")
            Username = input("Username: ")
            Password = input("Password: ")
            save_login_info(URL_web, Username, Password)  # saved the info. 
            print("Your details have successfully been saved!\n")  
            
        # option two is viewing the stored credentials.
        elif option == '2':
            view_saved_logins()  # calling the defined function. 
        elif option == 'e':       # option 'e' is exiting the program. 
            print("Thank you and Goodbye! ")
            break
        else:
            print("Error: Please choose option 1, 2, or e.")  # Made code that will handle any invalid input. 


# Running the DigiCore_Menu
if __name__ == "__main__": 
    DigiCore_Menu()

