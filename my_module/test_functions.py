"""Test for my encryption, decryption, and error_check functions."""

# import all 3 modules utilized in interpreter.py that needs to be tested
from my_module.encryption import encrypt
from my_module.decryption import decrypt
from my_module.error_check import input_error

def test_encrypt():
  """"Test encrypt functionality.
  
      Parameters
      ----------
      none

      Returns
      -------
      none

  """
  # Keep track of number of tests that pass
  pass_test = 0
  # Total number of asserts
  total_test = 6
  
  # Try, except to catch failed asserts
  try:
    # Test Case 1 (Sanity Check)                                #
    assert (encrypt("ABCDEF", "A") == "ABCDEF")
    pass_test = pass_test + 1

    # Test Case 2 (Shift 1)                                     #
    assert (encrypt("ABCDEF", "B") == "BCDEFG")
    pass_test = pass_test + 1

    # Test Case 3 (Shift -1)                                    #
    assert (encrypt("ABCDEF", "Z") == "ZABCDE")
    pass_test = pass_test + 1

    # Test Case 4 (No difference between upper and lower case)  #
    assert (encrypt("ABCDEF", "a") == "ABCDEF")
    pass_test = pass_test + 1

    # Test Case 5 (No difference between upper and lower case)  #
    assert (encrypt("AbCdEf", "a") == "ABCDEF")
    pass_test = pass_test + 1

    # Test Case 6 (Longer key)                                  #
    assert (encrypt("ABCDEF", "ABC") == "ACEDFH")
    pass_test = pass_test + 1

    print("Assertions passed for encrypt: " 
            + str(pass_test) 
           + "/" 
            + str(total_test))

  # An assert failed so print how many tests have passed so far
  except:
    print("Assertions passed for encrypt: " 
            + str(pass_test) 
           + "/" 
            + str(total_test))

def test_decrypt():
  """"Test decrypt functionality.
      Parameters
      ----------
      none

      Returns
      -------
      none
  """
  # Keep track of number of tests that pass
  pass_test = 0
  # Total number of asserts
  total_test = 6
  
  # Try, except to catch failed asserts
  try:
    # Test Case 1 (Sanity Check)                                #
    assert (decrypt("ABCDEF", "A") == "ABCDEF")
    pass_test = pass_test + 1

    # Test Case 2 (Shift 1)                                     #
    assert (decrypt("BCDEFG", "B") == "ABCDEF")
    pass_test = pass_test + 1

    # Test Case 3 (Shift -1)                                    #
    assert (decrypt("ZABCDE", "Z") == "ABCDEF")
    pass_test = pass_test + 1

    # Test Case 4 (No difference between upper and lower case)  #
    assert (decrypt("ABCDEF", "a") == "ABCDEF")
    pass_test = pass_test + 1

    # Test Case 5 (No difference between upper and lower case)  #
    assert (decrypt("AbCdEf", "a") == "ABCDEF")
    pass_test = pass_test + 1

    # Test Case 6 (Longer key)                                  #
    assert (decrypt("ACEDFH", "ABC") == "ABCDEF")
    pass_test = pass_test + 1

    print("Assertions passed for decrypt: " 
            + str(pass_test) 
            + "/" 
            + str(total_test))

  # An assert failed so print how many tests have passed so far 
  except:
    print("Assertions passed for decrypt: " 
            + str(pass_test) 
            + "/" 
            + str(total_test))

def test_input_error():
  """"Test input_error functionality.
      Parameters
      ----------
      none

      Returns
      -------
      none
  """
  # Keep track of number of tests that pass
  pass_test = 0
  # Total number of asserts
  total_test = 4

  try:
    # Test Case 1 (Sanity Check)                                #
    msg, key = input_error("ABCDEF", "A")
    assert(msg == "ABCDEF")
    assert(key == "A")
    pass_test = pass_test + 1

    # Test Case 2 (No difference between upper and lower case)  #
    msg, key = input_error("ABCDEF", "a")
    assert(msg == "ABCDEF")
    assert(key == "A")
    pass_test = pass_test + 1

    # Test Case 3 (No difference between upper and lower case)  #
    msg, key = input_error("AbCdEf", "a")
    assert(msg == "ABCDEF")
    assert(key == "A")
    pass_test = pass_test + 1

    # Test Case 4 (Longer key)                                  #
    msg, key = input_error("ABCDEF", "ABC")
    assert(msg == "ABCDEF")
    assert(key == "ABC")
    pass_test = pass_test + 1

    print("Assertions passed for input_error: " 
            + str(pass_test) 
            + "/" 
            + str(total_test))
    pass
  except:
    print("Assertions passed for input_error: " 
            + str(pass_test) 
            + "/" 
            + str(total_test))