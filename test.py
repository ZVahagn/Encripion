plaintext = "ATTACK AT DAWN"
keyword = "LEMON"

padded_key = keyword * (len(plaintext) // key_length + 1)[:len(plaintext)]
print(padded_key)