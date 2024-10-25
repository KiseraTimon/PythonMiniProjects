#10. Countdown timer

#Logic
"""
The user enters the hours, minutes and seconds they intend
The system runs down the time
A message is displayed at the end
"""

#Map
"""
Capture user input for hours, minutes and seconds
Start the timer and display the countdown on the terminal
Display a message on completion
"""

#Implementation

import time

#Function to computer time
def start_timer(hours, minutes, seconds):

    #Convert time to seconds
    totalseconds = (hours *3600) + (minutes *60) + seconds

    #Countdown
    while totalseconds > 0:

        #Converting seconds to hours, minutes and seconds
        hrs, remainder = divmod(totalseconds, 3600)
        mins, secs = divmod(remainder, 60)

        #Displaying the time
        print (f"{hrs:02}:{mins:02}:{secs:02}", end="\r")

        #Delay to realisitically display the time
        time.sleep(1)

        #Decrementing the time
        totalseconds -= 1
    
    #Displaying the end of the timer
    print(f"\nTimer has ended")

    #Prompting the user to reset the timer
    retry = str(input(f'Reset time? (y/n) ')).lower()
    return retry == "y"


#Looping timer body
while True:

    #Capture user input
    hours = int(input("\n\nHow many hours? "))
    minutes = int(input("How many minutes? "))
    seconds = int(input("How many seconds? "))


    #Start the timer
    if start_timer(hours, minutes, seconds):
        continue

    #End the timer
    else:
        print("Thank you for using the countdown timer!")
        break
