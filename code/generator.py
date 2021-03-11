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
    #print("If you answer something else than the given options, the following values will be set to default (told in paranthesis)")
    

    allowedCharacters = string.ascii_letters
    
    password = ""
    for i in range(length):
        password += choice(allowedCharacters)

    return password