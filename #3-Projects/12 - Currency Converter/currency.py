#12. Currency converter

#Logic
"""
The user selects the default currency
The user enters the amount
The user selects the currency to convert to
"""

#Map
"""
Let the user select the default currency
Capture the amount
Let the user select the desired currency
Convert the amount
Display the amount
"""

#Implementation
from currency_converter import CurrencyConverter

#Start function
def start():
    run = True
    return main(run)
    
def main(run):
    while run == True:

        #Instructions
        print (f'Instructions:\n\n1. Enter the currency using 3 letters representing the nation\n2. Enter the amount\n3. Enter the currency you wish to convert to\n\n')

        #Default currency
        default = str(input(f'What is the default currency? ')).upper()

        #Amount to be converted
        amount = float(input(f'\nEnter the amount: '))

        #Desired currency
        desired = str(input(f'\nEnter the currency to be converted to: ')).upper()

        #Verify length is 3 values long
        if (len(default) != 3) and (len(desired) != 3):
            print(f'\n\n##########\nInvalid input! Try again\n##########')
            continue
        else:
            conversion(default, amount, desired)
            break

    while run == False:
        print(f'\n##########\nThank you for using our converter\nTerminating\n##########')
        break


def conversion(default, amount, desired):

    try:
        #Converter
        c = CurrencyConverter()

        #Store final amount
        """
        The convert func takes 3-4 arguements: (amount, default currency, desired currency, date)
        """
        final = c.convert(amount, default, desired)

        #Conversion message
        print(f'\nConverting {default} {amount} to {desired}...\nThe converted amount is: {final}')
        return repeat()
    
    #Capturing any errors
    except Exception as e:
        print(f'\nAn error occured:\n{e}\nTerminating\n##########\n')
        return repeat()

#Repeat function
def repeat():
    while True:

        #Repeat option
        repeat = str(input("\n\nRepeat? (y/n) ")).lower()
        if repeat == "y":
            run = True
            main(run)
            break
        elif repeat == "n":
            run = False
            main(run)
            break
        else:
            print(f'\nInvalid option! Retry\n##########\n')

#Initializing
start()

#Update
"""
Some currencies are not supported
The map is not adhered to
The functionalities are decomposed into methods
"""