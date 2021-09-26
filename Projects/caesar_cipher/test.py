alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# input1 = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
# text = input("Type your message: ")
# shift = int(input("Type the shift number: "))


def startCipher():
    input1 = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
    if input1 == "decode":
        text = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        decrypt(text, shift)
    elif input1 == "encode":
        text = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        encrypt(text, shift)
    else:
        print("Please insert something meaningful.")


def encrypt(message, shift_number):
    encrypted_stuff = ""
    for letter in message:
        position = alphabet.index(letter)
        new_pos = position + shift_number
        encrypted_stuff = encrypted_stuff + alphabet[new_pos]
    print(f"The encoded text is {encrypted_stuff}")


def decrypt(message, shift_number):
    decrypted_stuff = ""
    for letter in message:
        c_positions = alphabet.index(letter)
        real_position = c_positions - shift_number
        decrypted_stuff = decrypted_stuff + alphabet[real_position]
    print(f"The decrypted text is {decrypted_stuff}")


startCipher()
