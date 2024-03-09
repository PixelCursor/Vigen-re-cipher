def vigenere_decrypt(ciphertext, keyword):
    plaintext = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            keyword_index = i % keyword_length
            keyword_char = keyword[keyword_index]
            keyword_shift = ord(keyword_char) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - keyword_shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - keyword_shift) % 26 + ord('a'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext