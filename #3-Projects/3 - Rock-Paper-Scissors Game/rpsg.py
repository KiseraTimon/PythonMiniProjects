#3. Rock, Paper Scissors Game

#Logic
"""
Both the user and the system pick either rock(r) paper(p) or scissors(s)
If one is s and the other is r, r wins because rock crushes scissors
If one is s and the other is p, s wins because scissors cut paper
If one is r and the other is p, p wins because p folds rock
"""

#Map
"""
game logic function:
    The system picks r/p/s
    The user picks r/p/s
    The system runs the logic
    Output the result

Check if the user wants to play again through a function
    If yes, repeat, if no, terminate
"""

#Implementation

#Module to randomize items
import random

#function to start the game
def start():
    play = True
    return game(play)

#function to verify if the user wants to play again
def confirm():
        while True:
            #capture interest to play again
            repeat = str(input("Do you want to play again? (y/n): ")).lower()

            #conditional implementation of interest
            if repeat == "y":
                play = True
                game(play)
                break
            elif repeat == "n":
                play = False
                game(play)
                break
            else:
                print("\n\n***** Invalid choice. Try again *****")

def game(play):
    while (play is True):

        game = ("Rock", "Paper", "Scissors")
        pick = random.randint(0,2)
        system_choice = game[pick]

        user_choice = str(input("\n\nRock, Paper Scissors? (r/p/s): ")).lower()

        if user_choice == "r" and system_choice == "Rock":
            print("\n\nDraw! You both picked rock\n")
            confirm()
            break
        if user_choice == "p" and system_choice == "Paper":
            print("\n\nDraw! You both picked paper\n")
            confirm()
            break
        if user_choice == "s" and system_choice == "Scissors":
            print("\n\nDraw! You both picked scissors\n")
            confirm()
            break

        if user_choice == "r" and system_choice == "Paper":
            print("\n\nYou lost!\nYou picked 🪨 and the system picked 🧻\nPaper wraps rock\n")
            confirm()
            break
        if user_choice == "r" and system_choice == "Scissors":
            print("\n\nYou won!\nYou picked 🪨 and the system picked ✂️\nRock crushes scissors\n")
            confirm()
            break
        if user_choice == "p" and system_choice == "Rock":
            print("\n\nYou won!\nYou picked 🧻 and the system picked 🪨\nPaper wraps rock\n")
            confirm()
            break
        if user_choice == "p" and system_choice == "Scissors":
            print("\n\nYou lost!\nYou picked 🧻 and the system picked ✂️\nScissors cut paper\n")
            confirm()
            break
        if user_choice == "s" and system_choice == "Rock":
            print("\n\nYou lost!\nYou picked ✂️ and the system picked 🪨\nRock crushes scissors\n")
            confirm()
            break
        if user_choice == "s" and system_choice == "Paper":
            print("\n\nYou won!\nYou picked ✂️ and the system picked 🧻\nScissors cut paper\n")
            confirm()
            break
    
    while(play is False):
        print("\n\nThank you for playing. The game will exit\n")
        break

start()