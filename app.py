import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
import io

# Set the path to Tesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_txt_file(file_path):
    try:
        image = Image.open(file_path)
        return extract_txt_img(image)
    except IOError:
        return extract_txt_unsupported_file(file_path)

def extract_txt_img(image):
    try:
        extracted_text = pytesseract.image_to_string(image)
        return extracted_text.strip(), image
    except Exception as e:
        return f"Error processing image: {e}", None

def extract_txt_unsupported_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            try:
                image = Image.open(io.BytesIO(content))
                return "Image extracted successfully.", image
            except IOError:
                decoded_content = content.decode('utf-8', errors='ignore')
                return decoded_content.strip(), None
    except Exception as e:
        return f"Error: {e}", None

def encode_image(input_image_path, output_image_path, message):
    img = Image.open(input_image_path)
    encoded_img = img.copy()

    message += chr(0)
    binary_message = ''.join(format(ord(c), '08b') for c in message)

    if len(binary_message) > img.width * img.height:
        raise ValueError("Message is too long to fit in the selected image.")

    data_index = 0
    width, height = img.size

    for x in range(width):
        for y in range(height):
            if data_index < len(binary_message):
                pixel = list(encoded_img.getpixel((x, y)))
                pixel[0] = (pixel[0] & ~1) | int(binary_message[data_index])
                encoded_img.putpixel((x, y), tuple(pixel))
                data_index += 1
            else:
                break
        else:
            continue
        break

    encoded_img.save(output_image_path, format='PNG')

def decode_image(image_path):
    img = Image.open(image_path)
    binary_message = ""
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            binary_message += str(pixel[0] & 1)

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '00000000':
            break
        message += chr(int(byte, 2))

    return message

def select_image_to_extract_text():
    file_path = filedialog.askopenfilename(title="Select an Image for Text Extraction", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        extracted_text, image = extract_txt_file(file_path)
        messagebox.showinfo("Extracted Content", extracted_text)
        if image:
            image.show()

def select_image_to_encode():
    try:
        input_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if input_path:
            output_path = filedialog.asksaveasfilename(title="Save Encoded Image As", defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
            if output_path:
                message = message_entry.get()
                if message:
                    encode_image(input_path, output_path, message)
                    messagebox.showinfo("Success", "Message encoded successfully!")
                else:
                    messagebox.showwarning("Input Error", "Please enter a message to encode.")
    except ValueError as ve:
        messagebox.showerror("Encoding Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def select_image_to_decode():
    try:
        input_path = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if input_path:
            hidden_message = decode_image(input_path)
            if hidden_message:
                messagebox.showinfo("Decoded Message", f"Hidden message: {hidden_message}")
            else:
                messagebox.showwarning("Decoding Warning", "No hidden message found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("Image Processing Tool")

tk.Label(root, text="Message to Encode:").pack(pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

encode_button = tk.Button(root, text="Encode Message in Image", command=select_image_to_encode)
encode_button.pack(pady=10)

decode_button = tk.Button(root, text="Decode Message from Image", command=select_image_to_decode)
decode_button.pack(pady=10)

extract_text_button = tk.Button(root, text="Extract Text from Image", command=select_image_to_extract_text)
extract_text_button.pack(pady=10)

root.mainloop()
