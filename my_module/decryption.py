"""A collection of decryption functions for interpreter.py."""

# variable to hold value of space
space = " "
# ASCII value of space
space_int = 32

def decrypt(cipher_text, key):
    """Given a cipher_text and a key, this function will convert the 
       cipher_text to plain_text. No error handling will be done here."""

    # Convert the cipher_text to upper case
    cipher_text = cipher_text.upper()
    # Get the length of the cipher_text
    cipher_text_length = len(cipher_text)
    # Convert the cipher_text to ASCII value
    cipher_text_int = [ord(i) for i in cipher_text]
    
    # Convert the key to upper case
    key = key.upper()
    # Get the length of the key
    key_length = len(key)
    # Convert the key to ASCII value
    key_int = [ord(i) for i in key]

    # plain_text that we will be returning
    plain_text = ""

    # Iterate through the cipher_text
    for i in range(cipher_text_length):
        # check if there is a space
        if(cipher_text_int[i] == space_int):
            plain_text = plain_text + space
            # Iterate to next character in cipher_text
            continue

        # Decrypt the char with the corresponding key
        value = (cipher_text_int[i] - key_int[i % key_length]) % 26
        plain_text = plain_text + chr(value + 65)

    # return the decrypted aka plain_text
    return plain_text