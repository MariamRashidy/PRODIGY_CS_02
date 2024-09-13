# Image Encryption Tool

This is a simple tool to encrypt and decrypt images by manipulating pixel values. It allows you to apply a shift to the RGB values and swap the red and blue channels.

## Requirements

To use this tool, you need Python installed along with the `Pillow` library for image processing. You can install the required package by running:

```bash
pip install Pillow
```
### How to Use
You can use the tool from the command line to encrypt or decrypt an image.

Encrypt an image:
```bash
python PRODIGY_CS_02.py --encrypt --input path_to_input_image.png --output path_to_output_image.png --shift 50
```
Decrypt an image:
```bash
python PRODIGY_CS_02.py --decrypt --input path_to_encrypted_image.png --output path_to_output_image.png --shift 50
```
Notes:
Make sure to use the same shift value during decryption as the one used during encryption.
You can adjust the shift value (e.g., 50 in this case) to any number between 0 and 255.

Example:
Place your input image in the same directory as PRODIGY_CS_02.py.
Run the encryption command to encrypt the image.
Use the decryption command to restore the original image.
