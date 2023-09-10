# Image Steganography Tool 🤖

## Overview

The Image Steganography Tool is a simple yet powerful utility for hiding and extracting secret data within digital images. This tool allows you to securely transmit information, protect your images with watermarks, or conceal sensitive data, all while maintaining the image's visual integrity.

## Features

- **Embedding**: Seamlessly hide text or another image within the least significant bits of the pixel values in your chosen image.
- **Extraction**: Effortlessly extract hidden data from steganographic images using the provided decryption key or algorithm.
- **Security**: Utilize strong encryption techniques to protect your hidden data.
- **Visual Integrity**: Ensure that the cover image appears unchanged to the human eye.
- **Various Formats**: Support for popular image formats like JPEG, PNG, and BMP.
- **User-Friendly Interface**: A simple and intuitive graphical user interface for ease of use.

## Getting Started

1. **Installation**: Clone this repository or download the latest release from the Releases section.

2. **Dependencies**: Ensure you have the required dependencies installed. You may need libraries for image processing and cryptography.

3. **Usage**: Refer to the user manual or documentation for instructions on how to use the tool effectively.

## Prerequisites
Before you begin, ensure you meet the following requirements:
* Python3
* Tkinter (Used for creating GUI's)
* Customtkinter   (Used for creating Modern GUI's)
* stegano
* PIL

## Setup

1. Clone the Repository:
   
```bash
git clone https://github.com/k-sameer701/Image-Steganography.git
```

2. Navigate to the Project Directory:
   
```
cd Image-Steganography
```

3. Run the app:
   
```bash   
python3 app.py
```

## Usage 💻:

## Encrypting Message 

1. Open the app on your system.
2. Select the image 
3. Write the message you want to encrypt in the message box.
4. Press the Encrypt Button.
5. A new image file will be created with name untitle.png
6. The encrypted message is now hidden in untitle.png

## Decrypting Message

1. Open Show tab.
2. Select the image .
3. Press the Decrypt Button.
4. If the image has some encrypted text, the message will be displayed on the new window.

## Developer
Sameer Kumar - [k-sameer701](https://github.com/k-sameer701)
