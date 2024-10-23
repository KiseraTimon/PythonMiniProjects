#1. Dice Rolling Game

#Logic
"""
The player chooses whether to roll dice.
There are two dice blocks involved and the system generates
a random result for the various faces
"""

#Map
"""
Implementing a looping structure
Ask if the user wants to play
If yes, generate two random numbers as dice faces
if no, thank the user for playing and terminate
Otherwise, flag the input as invalid
"""

#Implementation

#Importing module to generate random variables
import random

#Loop to keep the game running once the code executes
while True:
    #Capturing user input
    option = str(input("Ready to roll the dice? (y/n): ")).upper()

    #Conditions
    if option == "Y":
        #Generating random nums
        face1 = random.randint(1,6)
        face2 = random.randint(1,6)
        print(f'({face1},{face2})')

    elif option == "N":
        print("***** Thanks for playing *****")
        #Exit the loop
        break
    else:
        print("Invalid option")