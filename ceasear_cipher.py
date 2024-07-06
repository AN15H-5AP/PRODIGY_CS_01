#Write a program that uses ceasear cipher algorithm to encrypt and decrypt the provided message whith the help of shift _value
def encrypt(message, shift_value):
    result = ""
    for char in message:
        # Encrypt the uppercase character
        if char.isupper():
            result += chr((ord(char) + shift_value - 65) % 26 + 65)
        # Encrypt the lowercase character
        elif char.islower():
            result += chr((ord(char) + shift_value - 97) % 26 + 97)
        else:
            result += char
    return result

# Function to decrypt the encrypted message
def decrypt(message, shift_value):
    result = ""
    for char in message:
        # Decrypt the uppercase to original text
        if char.isupper():
            result += chr((ord(char) - shift_value - 65) % 26 + 65)
        # Decrypt the lowercase in the original text
        elif char.islower():
            result += chr((ord(char) - shift_value - 97) % 26 + 97)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt the message? Or enter Q to quit: ").upper()
        if choice == 'Q':
            break
        elif choice not in ['E', 'D']:
            print("Invalid choice. Please make the correct choice.")
            continue

        message = input("Enter the message: ")
        shift_value = int(input("Enter the shift value: "))

        if choice == 'E':
            encrypted_text = encrypt(message, shift_value)
            print(f"Encrypted message: {encrypted_text}")
        elif choice == 'D':
            decrypted_text = decrypt(message, shift_value)
            print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
