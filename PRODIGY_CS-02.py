from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    """
    Encrypt an image by manipulating its pixel values using a key.
    

    Parameters:
    - input_image_path: str, path to the input image to be encrypted.
    - output_image_path: str, path where the encrypted image will be saved.
    - key: int, an integer value used as a key for encryption.
    """
    
    # Load the image
    img = Image.open(input_image_path)
    img = img.convert('RGB')  # Ensure image is in RGB mode
    pixels = np.array(img)

    # Encrypt the pixels
    encrypted_pixels = np.bitwise_xor(pixels, key)

    # Convert the numpy array back to an image
    encrypted_img = Image.fromarray(encrypted_pixels)
    
    # Save the encrypted image
    encrypted_img.save(output_image_path)
    print(f"Your Image has been encrypted {output_image_path}")

def decrypt_image(encrypted_image_path, output_image_path, key):
    """
    Decrypt an encrypted image by reversing the pixel manipulation using the same key.
    
    Parameters:
    - encrypted_image_path: str, path to the encrypted image.
    - output_image_path: str, path where the decrypted image will be saved.
    - key: int, an integer value used as a key for decryption (must be the same key used for encryption).
    """
    
    # Load the encrypted image
    img = Image.open(encrypted_image_path)
    img = img.convert('RGB')  # Ensure image is in RGB mode
    pixels = np.array(img)

    # Decrypt the pixels
    decrypted_pixels = np.bitwise_xor(pixels, key)

    # Convert the numpy array back to an image
    decrypted_img = Image.fromarray(decrypted_pixels)
    
    # Save the decrypted image
    decrypted_img.save(output_image_path)
    print(f"Your Image has been decrypted and saved as {output_image_path}")

# Example Usage
key = 192 # Key for encryption and decryption

# Encrypt the image
encrypt_image('picnic-img3.jpg', 'encrypted_image.png', key)

# Decrypt the image
decrypt_image('encrypted_image.png', 'decrypted_image.png', key)
