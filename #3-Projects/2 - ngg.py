#2. Number Guessing Game

#Logic
"""
The program generates a random number between 1 and 30
The user attempts to guess the number
The system evaluates if the number generated and the user's guess match
"""

#Map
"""
The system is in a looping structure on executing
Ask the user if they want to play
If yes:
    Generate a random number
    Prompt the user to input a number within the range
    Evaluate if the random number and the guess match
    Output the results and inquire again on interest in playing
If no:
    Terminate the program
Otherwise, flag the input as invalid
"""

#Implementation

import random

while True:
    option = str(input("\n\nDo you want to play? (y/n): ")).upper()

    if option == "Y":
        num = random.randint(1,30)
        guess = int(input("\nEnter a number between 1 and 30: "))

        while (guess>0 and guess<=30):
            if num == guess:
                print("\nHooraaayyy! Your guess is correct\n")
                break
            else:
                print("\nWhoopssies! Try again\nThe number was: "+str(num)+"\nYour guess was: "+str(guess)+"\n\n")
                break
        else:
            print("Please enter a number in the specified range")
    
    elif option == "N":
        print("Thanks for playing!")
        break
    else:
        print("Invalid option")

