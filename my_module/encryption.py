"""A collection of encrypt functions for interpreter.py."""

# variable to hold value of space
space = " "
# ASCII value of space
space_int = 32

def encrypt(plain_text, key):
    """Given a plain_text and a key, this function will convert the 
       plain_text to cipher_text. No error handling will be done here.

       Parameters
       ----------
       plain_text: string
                   A string of the user's input that we will convert
       key: string
            A string of the user's input that will be the offset
            
       Returns
       -------
       cipher_text: string
                    A string that is the user's input encrypted
    """

    # Convert the plain_text to upper case
    plain_text = plain_text.upper()
    # Get the length of the plain_text
    plain_text_length = len(plain_text)
    # Convert the plain_text to ASCII value
    plain_text_int = [ord(i) for i in plain_text]

    # Convert the key to upper case
    key = key.upper()
    # Get the length of the key
    key_length = len(key)
    # Convert the key to ASCII value
    key_int = [ord(i) for i in key]

    # cipher_text that we will be returning
    cipher_text = ""

    # Iterate through the plain_text
    for i in range(plain_text_length):
        # check if there is a space
        if(plain_text_int[i] == space_int):
            cipher_text = cipher_text + space
            # Iterate to next character in plain_text
            continue
        # Encrypt the char with the corresponding key
        value = (plain_text_int[i] + key_int[i % key_length]) % 26
        cipher_text = cipher_text + chr(value + 65)

    # return the enecrypted aka cipher_text
    return cipher_text