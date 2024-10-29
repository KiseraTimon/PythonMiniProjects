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
from currencies import Currency
from currency_converter import CurrencyConverter

while True:
    print (f'Instructions:\n\n1. Enter the currency using 3 letters representing the nation\n2. Enter the amount\n3. Enter the currency you wish to convert to\n\n')
    default = str(input(f'What is the default currency? ')).upper()
    amount = float(input(f'\nEnter the amount: '))
    desired = str(input(f'\nEnter the currency to be converted to: ')).upper()

    if len(default) != 3:
        print(f'\n\n##########\nInvalid input! Try again\n##########')
        continue
    else:

        try:
            #Converter
            c = CurrencyConverter()
            final = c.convert(amount, default, desired)

            print(f'\nConverting {default} {amount} to {desired}...\nThe converted amount is: {final}')
            
            try_again = str(input("Repeat? (y/n)")).lower()
            if try_again == "n":
                print(f'Thank you for using our converter\nTerminating\n##########\n')
                break

        except Exception as e:
            print(f'\nAn error occured:\n{e}\nTerminating\n##########\n')
            continue