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

#game function
def game(play):
    #validates the value of play variable
    while (play is True):

        #Storing the game options
        game = ("Rock", "Paper", "Scissors")

        #Random indexing for system decisions
        pick = random.randint(0,2)

        #System decision
        system_choice = game[pick]

        #Implementing error handling
        try:
            #Fetching the user's choice
            user_choice = str(input("\n\nRock, Paper Scissors? (r/p/s): ")).lower()

            #Outputs if user and system decisions match
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
            
            #Outputs if user and system decisions vary
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
        #Exception handling
        except Exception:
            print("\n\nHmmm. Invalid input. Try again\n")
            confirm()
    
    #validating value of play variable
    while(play is False):
        print("\n\nThank you for playing. The game will exit\n")
        break

#Running the game
start()


#Alternative implementation
import random

"""Valid choices"""
choices  = ("r","p","s")
emojis = {"r": "🪨", "p":"🧻", "s":"✂️"}

while True:
    """Capturing choices"""
    user_choice = str(input("Rock, paper, scissors? (r/p/s): ")).lower()
    if user_choice not in choices:
        print("Invalid choice")
        continue

    system_choice = random.choice(choices)

    """Printing choices"""
    print(f'You chose {emojis[user_choice]}')
    print(f'The system chose {emojis[system_choice]}')

    """Determining the winner"""
    if user_choice == system_choice:
        print("It is a tie")
    elif (
    (user_choice == "r" and system_choice == "s") or
    (user_choice == "s" and system_choice == "p") or
    (user_choice == "p" and system_choice == "r")):
        print("You win")
    else:
        print("You lose")

    """Playing again"""
    play_again = str(input("Do you want to play again? (y/n): ")).lower()
    if play_again == 'n':
        break
