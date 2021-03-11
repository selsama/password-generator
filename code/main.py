import generator

print("Welcome to password generator!")
while (True):
    try:
        choice = int(input("1 - Create a new password, 0 - Quit \n"))
    except ValueError:
        choice = -1
    
    if choice == 0:
        break
    elif choice == 1:
        print("Here is your password: " + generator.generate())
    else:
        print("Command not found")

