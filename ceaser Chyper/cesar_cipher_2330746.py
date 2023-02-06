def welcome():
    """Function for welcome message"""
    print("\n           Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher ")
    # Arrows emojis
    print("             \U00002B07      \U00002B07       \U00002B07")


def enter_message():
    """Functions to take user's choice and message to encrypt/decrypt"""
    # taking choice from user
    mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
    print("                    \U00002B07       ")

    # checking if the input is correct or not
    while True:
        # wrong input statement
        if not (mode == 'e' or mode == 'd'):
            print("            \U0000274CInvalid Mode\U0000274C")
            mode = input("Would you like to encrypt (e) or decrypt (d): ")
            print("                    \U00002B07       ")
        # right input statement
        else:
            if mode == "e":
                msg = input("What message would you like to encrypt: ").upper()
                print("                    \U00002B07       ")
            else:
                msg = input("What message would you like to decrypt: ").upper()
                print("                    \U00002B07       ")
            break
        # checking if the shift number is valid or not
    while True:
        shift_number = input("What is the shift number: ")
        print("                    \U00002B07       ")
        if shift_number.isnumeric() and int(shift_number) in range(1, 26):
            shift_number = int(shift_number)
            break
        else:
            print("            \U0000274CInvalid Shift\U0000274C")

    # returns the value of user message and choice
    return msg, mode, shift_number


def encrypt(msg, shift_number):
    """Encryption Function"""
    concatenation = ""
    for char in msg:
        if char != " ":

            # converting the char in ASCII value
            char_value = ord(char)

            # Increment the ASCII value by shift number
            next_char_value = char_value + shift_number
            if next_char_value > 90:
                next_char_value -= 26
            # Using chr function to convert the ASCII value back to a character
            # Concatenating all char in a word
            concatenation += chr(next_char_value)
        else:
            concatenation += " "
    print(f"Your encrypted message for shift number {shift_number} is: {concatenation} ")
    print("                    \U00002B07       ")
    return concatenation


def decrypt(msg, shift_number):
    """Decryption Function"""
    concatenation = ""
    for char in msg:
        if char != " ":

            # converting the char in ASCII value
            char_value = ord(char)

            # Increment the ASCII value by shift number
            next_char_value = char_value - shift_number
            if next_char_value < 65:
                next_char_value += 26
            # Using chr function to convert the ASCII value back to a character
            # Concatenating all char in a word
            concatenation += chr(next_char_value)
        else:
            concatenation += " "
    print(f"Your decrypted message for shift number {shift_number} is: {concatenation} ")
    print("                    \U00002B07       ")
    return concatenation


def main():
    """Main function to call all the functions"""
    welcome()
    while True:

        msg, mode, shift_number = enter_message()

        # Calling the return value e_or_d
        if mode == "e":
            encrypt(msg, shift_number)
        else:
            decrypt(msg, shift_number)
        # Loop for user if they want to encrypt/decrypt another message
        another_msg = input("Would you like to encrypt/decrypt another message (y/n): ").lower()
        while "y" != another_msg != "n":
            print("                    \U00002B07       ")
            print("           \U0000274CInvalid option\U0000274C")
            another_msg = input("Would you like to encrypt/decrypt another message (y/n): ").lower()
        if another_msg == "n":
            print("             \U00002B07      \U00002B07       \U00002B07")
            print("Thank you for using the program and see you next time.\U0001F44B\U0001F60A")
            break
        elif another_msg == "y":
            print("                    \U00002B07       ")


main()
