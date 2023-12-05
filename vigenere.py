def vigenere_encrypt(plaintext, keyword):
    plaintext = plaintext.upper()
    keyword = keyword.upper()

    key_length = len(keyword)
    padded_key = keyword * (len(plaintext) // key_length + 1)
    padded_key = padded_key[:len(plaintext)]

    shift_dict = {chr(i): i - ord('A') for i in range(ord('A'), ord('Z') + 1)}

    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char not in shift_dict:
            ciphertext += char
            continue

        shift = shift_dict[padded_key[i]]
        new_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
        ciphertext += new_char

    return ciphertext

plaintext = input("Enter the plaintext: ")
keyword = input("Enter the keyword: ")

ciphertext = vigenere_encrypt(plaintext, keyword)
print("Ciphertext:", ciphertext)