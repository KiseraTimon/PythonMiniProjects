#8. File/folder compressor

#Logic
"""
Capture the file/folder path from the user
Check if the path is a file or a folder
If it is a file, compress the file
If it is a folder, compress the folder
Display the compressed file/folder path
"""

#Map
"""
Prompt the user to enter the file path
Check if the file path is a file or a folder
If it is a file, compress the file
If it is a folder, compress the folder
Display the compressed file/folder path
"""

#Implementation

import os
import zipfile

while True:
    # Capture the file/folder path from the user
    print
    (f'Please read the instructions carefully before proceeding.\n 1. Copy the file/folder path you want to compress.\n2. Remove the double quotes surrounding the path if any.\n3. Where there is a single backslash, add another so that they are two\n4. Press Enter to continue.\n')
    filepath = input("f'\n\nPlease read the instructions carefully before proceeding.\n1. Copy the file/folder path you want to compress.\n2. Remove the double quotes surrounding the path if any.\n3. Where there is a single backslash, add another so that they are two\n4. Press Enter to continue.\n5. Example of final path:\n C:\\\\Users\\\\user\\\\documents\\\\Pictures\\\\document_name\n\n\nEnter the file/folder path: ").strip()

    # Debugging print to check the entered file path
    print(f"\nChecking path: {filepath}")

    # Check if the path is a file
    if os.path.isfile(filepath):
        print(f"\nFile detected: {filepath}")

        # Compress the file
        with zipfile.ZipFile(filepath + '.zip', 'w') as zipf:
            zipf.write(filepath, os.path.basename(filepath), zipfile.ZIP_DEFLATED)

        # Display the compressed file path
        print("\nFile compressed successfully. Compressed file path: ", filepath + '.zip')
        continue

    # Check if the path is a folder
    elif os.path.isdir(filepath):
        print(f"\nFolder detected: {filepath}")

        # Compress the folder
        with zipfile.ZipFile(filepath + '.zip', 'w') as zipf:
            for foldername, subfolders, filenames in os.walk(filepath):
                # Add the folder to the zip file
                zipf.write(foldername, os.path.relpath(foldername, filepath), zipfile.ZIP_DEFLATED)

                # Add the files to the zip file
                for filename in filenames:
                    zipf.write(
                    os.path.join(foldername, filename),
                    os.path.relpath(os.path.join(foldername, filename), filepath),
                    zipfile.ZIP_DEFLATED)

        # Display the compressed folder path
        print("\nFolder compressed successfully. Compressed folder path: ", filepath + '.zip')
        continue

    # Otherwise, display an error message
    else:
        print("\nInvalid file/folder path. Please try again.")
