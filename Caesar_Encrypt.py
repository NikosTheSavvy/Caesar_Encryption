def caesar_encrypt(text, shift):
    result = ''

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char

    return result

def caesar_decrypt(text, shift):
    result = ''

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base - shift) % 26 + base
            result += chr(shifted)
        else:
            result += char

    return result

if __name__ == "__main__":
    print("Julius Caesar Cipher")
    mode = input("Do you want to encrypt or decrypt? ").strip().lower()
    text = input("Enter your message: ")

    if mode in ['encrypt', 'decrypt']:
        shift = int(input("Enter the shift value (e.g., 3): "))
        if mode == 'encrypt':
            print("Encrypted message:", caesar_encrypt(text, shift))
        else:
            print("Decrypted message:", caesar_decrypt(text, shift))
    else:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
