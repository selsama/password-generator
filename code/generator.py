from random import choice
import string

def generate() -> str:
    while True:
        try:
            length = int(input("Length of the password:"))
            if length  < 4 or length > 50:
                raise ValueError("Length not in range")
            break
        except ValueError:
            print("Make sure you have written the length in numbers, and it is between 4-50")
    
    while True:
        allowedCharacters = determineCharacters()
        if len(allowedCharacters) == 0:
            print("Unable to generate a password consisting of no characters. Please select at least some.")
        else:
            break    
    password = ""
    for i in range(length):
        password += choice(allowedCharacters)

    return password

def determineCharacters():
    print("What should the password consist of? If you answer something else than [y/n], the following values will be set to default")
    allowedCharacters = ""

    if checkAnswer("Lowercase letters (y/n, default yes)", True):
        allowedCharacters += string.ascii_lowercase
    if checkAnswer("Uppercase letters (y/n, default yes)", True):
        allowedCharacters += string.ascii_uppercase
    if checkAnswer("Numbers [0-9] (y/n, default yes)", True):
        allowedCharacters += string.digits
    if checkAnswer("All special characters (y/n, default no)", False):
        allowedCharacters += string.punctuation
    
    allowedCharacters += input("Now you can give other characters that you would like the password to have (no spaces, leave empty if none)")

    return allowedCharacters

def checkAnswer(message: str, default: bool):
    answer = input(message)
    if answer == "y" or answer == "yes":
        return True
    if answer == "n" or answer == "no":
        return False
    return default