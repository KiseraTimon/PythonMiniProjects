#11. A simple python code to encrypt and decrypt text

#Logic
"""
On user input,
the text is saved in an encrypted format in a txt file
"""

#Map
"""
The system accepts user's text input
The system encrypts the input and saves in a txt file the encrypted data
The system asks the user if they want to decrypt a txt file
If yes:
    - Decrypt the txt content
If no:
    - Ask the user if they have more text to encrypt
    If yes:
        - Encrypt
    If no: Break the loop
"""

#Implementation
import os
from cryptography.fernet import Fernet


#Start function
def start():
    init = True
    return main(init)

#Service function
def main(init):
    while init == True:

        #Encrypt/Decrypt
        service = int(input("Select a service to proceed:\n1. Encrypt text\n2. Decrypt file\n3. Exit\n\n"))

        if service == 1:
            encrypt()
            break
        elif service == 2:
            decrypt()
            break
        elif service == 3:
            init = False
            main(init)
            break
        else:
            print("\nInvalid input. Try again\n")
            continue
        

#Encryption function
def encrypt():
    while True:
        pass

def decrypt():
    while True:
        pass

start()