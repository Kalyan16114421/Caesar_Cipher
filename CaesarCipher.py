def caesar_cipher(text, shift, mode):
  """
    Encrypts or decrypts text using the Caesar Cipher.

    Args:
    text (str): The text to encrypt or decrypt.
    shift (int): The shift value.
    mode (str): 'encrypt' or 'decrypt'.

    Returns:
    str: The encrypted or decrypted text.
    """
  result = ''
  for char in text:
      if char.isalpha():
          start = ord('a') if char.islower() else ord('A')
          shifted_char = chr((ord(char) - start + shift * (1 if mode == 'encrypt' else -1)) % 26 + start)
          result += shifted_char
      else:
          result += char # Keep non-alphabetic characters unchanged
  return result

def main():
    while True:
       print("\nCaesar Cipher Program")
       print("1. Encrypt")
       print("2. Decrypt")
       print("3. Exit")

       choice = input("Enter your choice (1/2/3): ")

       if choice == '1':
           message = input("Enter the message to encrypt:")
           try:
             shift = int(input("Enter the shift value:"))
             encrypted_message = caesar_cipher(message, shift, 'encrypt')
             print("Encrypted message:", encrypted_message)
           except ValueError:
            print("Invalid shift value. Please enter an integer.")

       elif choice == '2':
           message = input("Enter the message to decrypt:")
           try:
               shift = int(input("Enter the shift value:"))
               decrypted_message = caesar_cipher(message, shift, 'decrypt')
               print("Decrypted message:", decrypted_message)
           except ValueError:
             print("Invalid shift value. Please enter an integer.")

       elif choice == '3':
         print("Exiting...")
         break

       else:
           print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()