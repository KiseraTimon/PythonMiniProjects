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

#System interaction module
import os
#Importing cryptography module
from cryptography.fernet import Fernet


#Start function
def start():
    #Initializer set to true
    init = True

    #Running service function
    return main(init)

#Service function
def main(init):

    #Verify initializer is true
    while init == True:

        #Option input
        service = int(input("\nSelect a service to proceed:\n1. Encrypt text\n2. Decrypt file\n3. Exit\n\n"))

        #Encrypt service
        if service == 1:
            encrypt()
            break

        #Decrypt service
        elif service == 2:
            decrypt()
            break

        #Terminate program
        elif service == 3:
            init = False
            main(init)
            break

        #Repeat loop otherwise
        else:
            print("\nInvalid input. Try again\n")
            continue
        
    #If initializer is false
    while init == False:
        print("\n\n##########")

        #Terminate the program
        break

#Encryption function
def encrypt():

    #Fetching user input to encrypt
    textinput = str(input("\nEnter text to encrypt:\n"))

    try:

        #Encryption key
        key = Fernet.generate_key()
        f = Fernet(key)

        #Encryption token
        token = f.encrypt(textinput.encode())

        #Storing key and token in txt file
        with open("crypt.txt", "w") as file:
            file.write(f'Key:\n{key.decode()}\nToken:\n{token.decode()}\n')
            print("\nKey and token saved successfully\nData can be decrypted by restarting the program")

            #Return to service page
            init = True
            return main(init)

    #In case of exceptions, print the error and return the service page
    except Exception as e:
        print(f'\nAn error has occured:\n{e}\n')

        init = True
        return main(init)

#Decryption function
def decrypt():
        
    try:
        #Note for commencement of decryption
        print(f'\n\nDecrypting procedure starting\n\n')

        #Read key and token value from stored file
        with open ("crypt.txt", "r") as file:
            lines = file.readlines()
            key = lines[1].strip()
            token = lines[3].strip()

        #Decryption procedure
        f = Fernet(key.encode())
        decrypt = f.decrypt(token.encode()).decode()

        #Message on success
        print(f'Decryption successfull\n\nDecrypted data:\n{decrypt}')
        
        #Clear data from stored file by overwriting
        print(f'\n\n##########\nFile contents will be cleared immediately\n##########')
        with open ("crypt.txt", "w") as file:
            file.write("")

        #User heads-up note
        print(f'Files encrypted after decryption are saved on exit')

        #Return service page
        init = True
        return main(init)

    #In case of exceptions, return error message and go to service page
    except Exception as e:
        print(f'Decryption failed:\n{e}\n')
        
        init = True
        main(init)

#Start the program
start()