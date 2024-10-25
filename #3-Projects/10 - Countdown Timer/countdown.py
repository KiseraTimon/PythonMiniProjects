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

def start_timer(timer):
    while (timer[2] < 60 and timer[2] != 0):
        timer[2] = timer[2] - 1
        print(timer)
    else:
        while (timer[1] < 60 and timer[1] != 0):
            timer[1] = timer[1] - 1
            print (timer)
        else:
            while (timer[0] == 0 and timer[1] == 0 and timer[2] == 0):
                print(timer)
                print(f'Timer completed')
                retry = str(input(f'Reset time? (y/n) ')).lower()

                if retry == "n":
                    break

while True:
    hours = int(input("How many hours? "))
    minutes = int(input("How many minutes? "))
    seconds = int(input("How many seconds? "))

    timer = [hours, minutes, seconds]
    start_timer(timer)
