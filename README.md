# StegoVision

This Python-based application provides a user-friendly interface for performing several image processing tasks, such as text extraction from images using OCR and encoding/decoding hidden messages within images. It uses `Tkinter` for the GUI, `pytesseract` for OCR, and `Pillow` for image manipulation.

## Features

- **Text Extraction**: Extracts text from image files using Tesseract OCR.
- **Message Encoding**: Hides a user-provided message within an image using steganography.
- **Message Decoding**: Retrieves hidden messages from encoded images.

## Requirements

Ensure the following dependencies are installed:

- **Python 3.6+**
- **Tkinter** (usually comes pre-installed with Python)
- **Pillow**: Install via `pip install pillow`
- **pytesseract**: Install via `pip install pytesseract`
- **Tesseract OCR**: [Download and install Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and set the executable path in the code.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Vansh-Visaria/StegoVision.git
   cd image-processing-tool
Install the required packages:

```bash
pip install -r requirements.txt
```

Set the Tesseract OCR path: Open the code and modify the following line with your Tesseract installation path:

python
```
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

Run the application:

```bash
python app.py
```

## Usage
GUI
Upon running the script, a graphical interface will appear with the following options:
- Encode Message in Image:
- Enter the message you want to hide in the image.
- Select the image where the message will be hidden.
- Specify the output path to save the encoded image.
- Decode Message from Image:
Select an encoded image to extract the hidden message.
The decoded message will be displayed if found.
- Extract Text from Image:
Choose an image with text, and the tool will extract any readable text using OCR.

## Core Functions
- extract_txt_file(file_path): Extracts text from an image or text file.
- encode_image(input_image_path, output_image_path, message): Encodes a message within an image using LSB steganography.
- decode_image(image_path): Decodes and retrieves a message from an encoded image.
  
