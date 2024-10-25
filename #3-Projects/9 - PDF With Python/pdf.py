#9. Handling PDFs with Python

#Logic
"""
The file path of the PDF file is captured from the user
The PDF file is opened in read mode
The PDF file is read and the text content is extracted
The extracted text content is displayed to the user
"""

#Map
"""
Prompt the user to enter the file path of the PDF file
Open the PDF file in read mode
Read the PDF file and extract the text content
Display the extracted text content to the user
"""

#Implementation
from pypdf import PdfReader
import os

while True:
    #read file path
    filepath = str(input("\n\nEnter the file path of the associated pdf: ")).strip()

    try:
    #Open the PDF file
        fileread = PdfReader(filepath)

        #Count pages
        pagecount = len(fileread.pages)

        #Extract content
        pdfcontent = ""

        #Looping through pages to extract content
        for page in fileread.pages:
            pdfcontent += page.extract_text()

        #Outputs
        print(f'Your filepath is: {filepath}\n\n')
        print(f'Document page count is: {pagecount}\n\n')
        print(f'PDF content is: \n{pdfcontent}\n\n')

        #Retrying
        retry = str(input("Retry? (y/n) ")).lower()

        if retry == "n":
            print(f'Thank you extracting with us: ')
            break

    except Exception as e:
        print(f'An error occured:\n{e}')