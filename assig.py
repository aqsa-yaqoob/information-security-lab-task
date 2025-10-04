def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isupper():  # For uppercase letters
            result += chr(65 + (25 - (ord(char) - 65)))
        elif char.islower():  # For lowercase letters
            result += chr(97 + (25 - (ord(char) - 97)))
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result


# Get input from the user
plaintext = input("Enter text to encrypt using Atbash Cipher: ")

# Encrypt (Atbash is symmetric — encryption = decryption)
encrypted = atbash_cipher(plaintext)
print("Encrypted text:", encrypted)

# Decrypt (same function works)
decrypted = atbash_cipher(encrypted)
print("Decrypted text:", decrypted)i 