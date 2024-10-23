#4. QR Code Generator

#Logic
"""
The user enters the URL or the data they intend to store in the QR code
The user enters the name they intend to store their file as including the extension (.jpg/.cpp)
"""

#Map
"""
capture data and filename from the user
using qrcode module, generate the QR code:
    set the box size to 10
    set the border to 4
    add the data to the QR code
    make the image with a black fill and white background
save the QR code as the filename entered by the user
"""

#Implementation
import qrcode

data = input("Enter text or a URL: ").strip()
filename = input("Enter the filename including extension (eg: .jpg .png): ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color = "black", back_color = "white")
image.save(filename)
print(f'QR code saved as {filename}')

#Step by step guide to creating a QR code generator
"""
1. Download and install the qrcode module from the Python Package Index (PyPI)
2. Create and activate a virtual environment
3. In your file, import the qrcode module
4. Enjoy
"""