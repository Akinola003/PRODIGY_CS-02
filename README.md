Explanation:
Libraries:

PIL (Python Imaging Library) is used to handle image operations.
numpy is used for efficient manipulation of image pixel data.
Encrypting the Image:

The image is first converted into a numpy array for easy manipulation.
Each pixel value is altered using the bitwise XOR operation with a key. This operation ensures that the encryption is reversible.
The modified pixel data is then converted back into an image and saved.
Decrypting the Image:

The decryption process is identical to encryption because XOR is a symmetric operation. When you XOR the encrypted pixel values with the same key, you recover the original pixel values.
Key:

The key used here is an integer. The security of this method depends on the key being kept secret. In real-world applications, keys should be randomly generated and sufficiently large.
How to Use:
Replace 'input_image.png' with the path to the image you want to encrypt.
The encrypted image will be saved as 'encrypted_image.png'.
To decrypt, use the same key and pass the path to the encrypted image to the decrypt_image function. The decrypted image will be saved as 'decrypted_image.png'.
This code is a basic demonstration of image encryption. For more secure implementations, more sophisticated algorithms like AES should be used, but this example provides a clear understanding of how pixel manipulation can be employed for simple image encryption.