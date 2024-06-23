def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char) + shift_amount
            if char.islower():
                if char_code > ord('z'):
                    char_code -= 26
            elif char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
            encrypted_text += chr(char_code)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Would you like to encrypt(e) or decrypt(d) a message? Enter 'q' to quit: ").lower()
        if choice == 'q':
            break
        elif choice in ['e', 'd']:
            text = input("Enter the message to be encrpted/decrypted: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'e':
                result = encrypt(text, shift)
                print(f"Encrypted message: {result}")
            elif choice == 'd':
                result = decrypt(text, shift)
                print(f"Decrypted message: {result}")
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
