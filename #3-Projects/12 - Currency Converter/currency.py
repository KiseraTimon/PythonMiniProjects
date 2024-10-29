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

#Looping structure
while True:

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

    #Otherwise, run conversion
    else:

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
            
            #Repeat option
            repeat = str(input("Repeat? (y/n)")).lower()
            if repeat == "n":
                print(f'Thank you for using our converter\nTerminating\n##########\n')
                break

        #Capturing any errors
        except Exception as e:
            print(f'\nAn error occured:\n{e}\nTerminating\n##########\n')
            continue