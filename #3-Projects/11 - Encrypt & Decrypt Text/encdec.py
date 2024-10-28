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
        service = int(input("\nSelect a service to proceed:\n1. Encrypt text\n2. Decrypt file\n3. Exit\n\n"))

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
        textinput = str(input("\nEnter text to encrypt:\n"))

        try:

            #Encryption key
            key = Fernet.generate_key()
            global f
            f = Fernet(key)
            global token
            token = f.encrypt(b'{textinput}')

            #Storing key and token in txt file
            with open("crypt.txt", "w") as file:
                file.write(f'Key:\n{key.decode()}\nToken:\n{token.decode()}\n')
                print("\nKey and token saved successfully")
                return main(init)

        except Exception as e:
            print(f'\nAn error has occured:\n{e}\n')
            retry = str(input("Retry? (y/n) ")).lower()

            if retry == "n":
                init = True
                return main(init)
                break
            else:
                print("Invalid input. The system will retry\n")
                continue
            

def decrypt():
    while True:
        
        print(f'\n\nDecrypting procedure starting\n\n')
        
        try:

            data = f.decrypt(token)
            b'{data}'
            print(data)

        except Exception as e:
            print(f'Decryption failed:\n{e}\n')
            retry = str(input("Retry? (y/n) ")).lower()

            if retry == "n":
                init = True
                main(init)
                break
            else:
                print("Invalid input. The system will retry\n")
                continue

start()