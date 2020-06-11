"""A collection of interpreter functions for doing my project."""

# import all 3 modules that we will be wrapping in this script
from my_module.encryption import encrypt
from my_module.decryption import decrypt
from my_module.error_check import input_error

# variable to hold value of the string 1
one = "1"
# variable to hold value of the string 2
two = "2"
# variable to hold value of the string 3
three = "3"

def main():
    """"The main function that will be interacting with the JupyterNotebook. 
        Will be the wrapper for encryption.py, decryption.py, and 
        error_check.py"""

    # Bool value to keep prompting the user for input until user quits program
    chat = True

    # Print disclaimer of valid input
    print("Key and Message can only be alphabetic \n")

    # Keep looping until the user quits the program
    while chat:

        # Print to user the possible use cases
        print("1. Encryption")
        print("2. Decryption")
        print("3. Quit")

        # Read the user's input choice to decide which branch to go to
        cmdline = input("Choose (1, 2, 3) : \t")

        # User's input was 1 so we will do encryption logic
        if(cmdline == one):
            print("\n---Encryption---")
            # Read in the message from the user
            plain_text = input("Enter message: \t\t")
            # Read in the key from the user
            key = input("Enter key: \t\t")
            # Ensure user input was valid otherwise, input_error will reprompt
            plain_text, key = input_error(plain_text, key)
            # Delegate encryption logic to encrypt function
            cipher_text = encrypt(plain_text, key) 
            print("Encrypted message:\t", cipher_text) 

        # User's input was 2 so we will do decryption logic
        elif(cmdline == two):
            print("\n---Decryption---")
            # Read in the message from the user
            cipher_text = input("Enter message: \t\t")
            # Read in the key from the user
            key = input("Enter key: \t\t")
            # Ensure user input was valid otherwise, input_error will reprompt
            cipher_text, key = input_error(cipher_text, key)
            # Delegate decryption logic to encrypt function
            plain_text = decrypt(cipher_text, key) 
            print("Encrypted message:\t", plain_text)

        # User's input was 3 so we will close the program
        elif(cmdline == three):
            print("\n--Quit---")
            print("Exiting program")
            chat = False
            return
        
        # User's input was invalid so we will reprompt the user at next loop
        else:
            print("Invalid input...")

        # Make the prompt pretty by adding extra new line
        print("\n")