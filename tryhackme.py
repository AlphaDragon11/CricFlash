def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) + shift) % 10)
        else:
            shifted_char = char
        result += shifted_char
    return result

# Example usage:
text = "This is a secret message!"
encrypted_text = caesar_cipher(text, 3, 'encrypt')
print("Encrypted:", encrypted_text)
decrypted_text = caesar_cipher(encrypted_text, -3, 'decrypt')
print("Decrypted:", decrypted_text)
