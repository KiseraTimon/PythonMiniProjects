#6. Web Page Links Retriever

#Logic
"""
The system takes a URL from the user.
The system reads the page and capture all links in a txt file
The system displays the links to the user in the console
"""

#Map
"""
1. Prompt the user to enter the URL
2. Read the page and capture all links
3. Write the links to a txt file
4. Display the links to the user from the console
"""

#Implementation

#Modules
import requests
from bs4 import BeautifulSoup

while True:
    print("\n\nThis system will retrieve all links from a webpage.")
    url = input("Enter the URL of the page: ")

    #Mimicking a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    #Error handling
    try:

        #Fetching the page code
        page = requests.get(url)

        #Check if request was successful
        if page.status_code == 200:
            print("\n***** Page retrieved successfully. Proceeeding *****\n")
            soup = BeautifulSoup(page.content, 'html.parser')

            #Extracting all links
            links = [a['href'] for a in soup.find_all('a', href=True)]

            #Writing the links in the txt file
            with open("links.txt", "w") as file:
                for link in links:
                    file.write(f'Links in ({url}): {link}\n')

            print("Links have been extracted successfully")

            #Print the links in the console
            print("Links extracted: \n")
            for link in links:
                print(link)
            
        #Otherwise if request was not successful
        else:
            print(f'Error retrieving page')
            retry = str(input("Do you want to try again? (y/n) ")).lower()

            if retry == "n":
                break

    #Capturing and outputting the exception
    except requests.exceptions.RequestException as e:
        print(f'Error fetching the url:\n{e}')
        continue
        