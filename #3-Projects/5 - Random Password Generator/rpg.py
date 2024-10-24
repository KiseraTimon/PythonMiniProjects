#5. Random Password Generator

#Logic
"""
The user enters the length of the password they want to generate.
The program generates a random password of the desired length.
The program displays the password to the user.
"""

#Map
"""
1. Capture the required length of the password
2. Generate a random password of the desired length
3. Display the password to the user
4. Ask the user if they want to generate another password
5. If yes,
    repeat the process
6. If no,
    exit the program
"""

#Implementation

#Module to generate randomize items
import random

#Loop if the user wants to regenerate
while True:

    #Fetch desired password length
    length = int(input("Enter the length of your desired password: "))

    #Generate password
    password = random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()", k=length)

    #Display password
    print(f'Your password is: {"".join(password)}')

    #Ask user if they want to regenerate
    regen = str(input("Generate again? (y/n) ")).lower()

    #Exit if user doesn't want to regenerate
    if regen == "n":
        print("\nThe program will exit now.\n")
        break

