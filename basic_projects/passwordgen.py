import random
import string


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    """
    Generates a random password based on users preferences.
    """

    # character pools based on user preferences.

    character_pool = ""
    if use_uppercase:
        character_pool += string.ascii_uppercase # A - Z
    if use_lowercase:
        character_pool += string.ascii_lowercase # a - z
    if use_numbers:
        character_pool += string.digits # 0 - 9
    if use_special:
        character_pool += string.punctuation

    # if no character type is selected return an error message
    if not character_pool:
        return None

    # generate a random password from the character pool

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def validate_integer_input(prompt, min_value=None):
    """ Validate that the user inputs a valid integer, optionally with a minimum value"""

    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if min_value is not None and value < min_value:
                print(f"Please enter a number greater than or equal to {min_value}")
                continue
            return value
        except ValueError:
            print('Invalid input! Please enter a valid number')


def validate_yes_no_input(prompt):
    """Validates that the user input 'y' or 'n' """

    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print("Invalid input! Please enter 'y' for yes or 'n' for no.")


def password_generator():
    """A complete program to generate random secure passwords based on user preference"""

    print('Welcome to the password Generator!')

    # get password length
    password_length = validate_integer_input('Enter the desired paswword length (minimum 8): ', min_value=8)

    # get user preference for character tyepes
    print('would you like to include the following in your password?')
    use_uppercase = validate_yes_no_input('Uppercase letters (A - Z)? (y/n): ')
    use_lowercase = validate_yes_no_input('Lowercase letters (a - z)? (y/n): ')
    use_numbers = validate_yes_no_input('Numbers (0 - 9)? (y/n): ')
    use_special = validate_yes_no_input('Special characters (!, @, #, $ etc)? (y/n): ')

    # generate the password

    password = generate_password(password_length, use_uppercase, use_lowercase, use_numbers, use_special)


    if password is None:
        print('Error: you must select at least one character type!')
    else:
        print('------your secure password-------')
        print(password)
        print('Thank you for using the password generator')

password_generator()