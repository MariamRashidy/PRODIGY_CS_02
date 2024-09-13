from PIL import Image
import argparse

def encrypt_image(input_path, output_path, shift_value):
    """
    Encrypt an image by shifting RGB values and swapping red and blue channels.
    
    Parameters:
    input_path (str): Path to the input image.
    output_path (str): Path to save the encrypted image.
    shift_value (int): Value to shift the RGB channels.
    """
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Apply shift to RGB values
            r = (r + shift_value) % 256
            g = (g + shift_value) % 256
            b = (b + shift_value) % 256

            # Swap red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully")


def decrypt_image(input_path, output_path, shift_value):
    """
    Decrypt an image by reversing the channel swap and RGB shift.
    
    Parameters:
    input_path (str): Path to the encrypted image.
    output_path (str): Path to save the decrypted image.
    shift_value (int): Value to reverse the RGB channel shift.
    """
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Swap back red and blue channels
            decrypted_pixel = (b, g, r)

            # Reverse the shift
            r = (decrypted_pixel[0] - shift_value) % 256
            g = (decrypted_pixel[1] - shift_value) % 256
            b = (decrypted_pixel[2] - shift_value) % 256

            pixels[i, j] = (r, g, b)

    img.save(output_path)
    print("Image decrypted successfully")


if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt an image using pixel manipulation.")

    # Add arguments for the command line tool
    parser.add_argument("--encrypt", action="store_true", help="Encrypt the image.")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt the image.")
    parser.add_argument("--input", type=str, required=True, help="Path to the input image.")
    parser.add_argument("--output", type=str, required=True, help="Path to save the output image.")
    parser.add_argument("--shift", type=int, required=True, help="Shift value for pixel manipulation (0-255).")

    # Parse the arguments
    args = parser.parse_args()

    # Run encrypt or decrypt based on the command
    if args.encrypt:
        encrypt_image(args.input, args.output, args.shift)
    elif args.decrypt:
        decrypt_image(args.input, args.output, args.shift)
    else:
        print("Please specify --encrypt or --decrypt.")

