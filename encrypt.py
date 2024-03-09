def vigenere_encrypt(plaintext, keyword):
    ciphertext = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            keyword_index = i % keyword_length
            keyword_char = keyword[keyword_index]
            keyword_shift = ord(keyword_char) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + keyword_shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + keyword_shift) % 26 + ord('a'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext