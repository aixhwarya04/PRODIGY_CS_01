# Caesar Cipher Implementation

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift letters
            shift_amount = shift % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char  # Keep spaces and punctuation unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just shifting backwards

# Main program
print("=== Caesar Cipher ===")
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))

encrypted_message = encrypt(message, shift_value)
print(f"Encrypted: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, shift_value)
print(f"Decrypted: {decrypted_message}")
