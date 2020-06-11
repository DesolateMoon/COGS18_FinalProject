"""A collection of error checking functions for interpreter.py."""

# ASCII Value of 'A'
A = 65
# ASCII Value of 'Z'
Z = 90
# ASCII Value of space
space = 32
def input_error(msg, key):
    """Verifies that the message and the key are alphabet values, if not
       keep reprompting the user till the values are valid. All errors
       from the JupyterNotebook are handled here.
       
       Parameters
       ----------
       msg: string
            A string of the user's input that we error check
       key: string
            A string of the user's input that we error check
            
       Returns
       -------
       msg: string
            A valid input for message from the user
       key: string
            A valid input for key from the user
                   
    """

    # Bool value to keep looping until user enters valid message and key
    yikes = True

    # Bool value to ensure that the message is valid
    msg_bool = False

    # Bool value to ensure that the key is valid
    key_bool = False

    # Keep looping until user enters valid message and key
    while yikes:
        # Convert the message to upper case
        msg = msg.upper()
        # Convert the key to upper case
        key = key.upper()

        # Iterate through the message
        for i in msg:
            # Check if the character is not space nor within valid ASCII Range
            if ord(i) != space and (ord(i) < A or Z < ord(i)):
                # Message is not valid so set flag to false
                msg_bool = False
                # reprompt the user for valid message
                msg = input("Please input alphabetic string for message: \t\t")
                # break out of the for loop to check if key is valid
                break
            else:
                msg_bool = True

        # Iterate through the key
        for j in key:
            # Check that the character is not within the valid ASCII Range
            if ord(j) < A or Z < ord(j):
                # Key is not valid so set flag to false
                key_bool = False
                # reprompt the user for valid key
                key = input("Please input alphabetic non-space string for key: \t")
                # break out of the for loop to check if message is valid
                break
            # Character is within the valid ASCII range
            else:
                key_bool = True

        # Ensures that both the message and key are valid alphabetic strings
        if msg_bool and key_bool:
            yikes = False

    # Return the new message and key to the main function
    return msg, key