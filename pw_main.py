"""Generates a non-pronounceable password using the random module from the
Python standard library."""

import random

def output_txt(pw, filename="pw_out.txt"):
    """Write a password string output to a text file. Overwrite the existing
    pw_out.txt file unless the function call passes a different file name.

    Args:
        pw (string): a string of a pw to output to .txt.
        filename (string): string of the name of an existing .txt file or
            name of new text file to create.

    Returns:
        None
    """
    file = open(filename, 'w', encoding='utf-8')
    file.write(pw)
    file.close()

def get_chars(upper=True, lower=True, numerals=True,
              specials=True, spaces=False, all_whitespace=False):
    """Return a list of characters for use in the password.

    Args:
        upper (bool): True to include uppercase. Defaults to True.
        lower (bool): True to include lowercase letters. Defaults to True.
        numerals (bool): True to include numerals 0 through 9. Defaults to True.
        specials (bool): True to include common unicode special characters like
            punctuation and mathematical operators. Defaults to True.
        spaces (bool): True to include space character. Defaults to False.
        all_whitespace(bool): True to include all of space, newline, and tab.
            Defaults to False. 
        
    Returns:
        (list): a list of strings
    """
    characters = []
    if upper == True:
        characters += [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    if lower == True:
        characters += [chr(i) for i in range(ord('a'), ord('z') + 1)]
    if numerals == True:
        characters += [str(i) for i in range(10)]
    if specials == True:
        special_chars = [chr(i) for i in range(33, 48)] +\
            [chr(i) for i in range(58, 65)] +\
            [chr(i) for i in range(91, 97)] +\
            [chr(i) for i in range(123, 127)]
        characters += special_chars
    if spaces == True:
        characters += [' ']
    if all_whitespace == True:
        characters += ['\t', '\n']
    return characters

def generate_pw(length, characters):
    """Generate a non-pronounceable password of the given length using a
    random selection of the given characters.

    Args:
        length (int): number of characters to include in the password
        characters (list or str): iterable string object. String or list of
            strings.

    Returns
        (str): a password string.
    """
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

def get_char_options_input():
    """
    Used by the command_line() function.
    
    Returns:
        characters (list or str): iterable set of characters for use by pw
            generator.
    """
    print("Enter the full function call for get_chars().")
    print("Default call get_chars(upper=True, lower=True, numerals=True,\
        specials=True, spaces=False, all_whitespace=False)")
    try:
        expression = input(">>> ")
        characters = eval(expression)
    except:
        print(f"Bad eval(). Try again? Y/N")
        choice = input(">>> ").lower()
        if choice == 'y':
            characters = get_char_options_input()
        else:
            characters = get_chars()    
    return characters

def command_line():
    """Runs simple CLI interface to pass arguments to the password generator.

    Returns:
        None
    """

    length = int(input("Enter desired password length\n>>> "))
    print(f"Default character list is upper and lowercase letters, digits 0 \
through 9, and normal special characters.")
    choice = input("Change default character list? Enter Y/N\n>>> ").lower()
    if choice == 'y':
        characters = get_char_options_input()
    elif choice == 'n':
        characters = get_chars()
    else:
        choice = input("Change default character list? Enter Y/N\n>>> ")
    password = generate_pw(length, characters)
    print("Generated password. Enter 'p' to print to command line or 'w' to \
write to text file.")
    choice = input(">>> ").lower()
    if choice == 'p':
        print(f"Password:\n\t{password}")
    elif choice == 'w':
        output_txt(password)
        print(f"Saved to pw_out.txt")
    input("Press any key to exit\n>>>")

def main():
    command_line()

if __name__ == '__main__':
    main()
