import tkinter as tk
from decrypt import vigenere_decrypt
from encrypt import vigenere_encrypt
import pyperclip

def show_ciphertext():
    text = text_entry.get("1.0", tk.END).strip()
    keyword = keyword_entry.get("1.0", tk.END).strip()
    ciphertext = vigenere_encrypt(text, keyword)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, ciphertext)

def show_plaintext():
    text = text_entry.get("1.0", tk.END).strip()
    keyword = keyword_entry.get("1.0", tk.END).strip()
    plaintext = vigenere_decrypt(text, keyword)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, plaintext)

def copy_text():
    text = result_text.get("1.0", tk.END).strip()
    pyperclip.copy(text)

root = tk.Tk()
root.title("Vigenere")
root.geometry("500x400")

text_label = tk.Label(root, text="Text:")
text_label.pack()

text_entry = tk.Text(root, width=50, height=2)
text_entry.pack()

keyword_label = tk.Label(root, text="Keyword:")
keyword_label.pack()

keyword_entry = tk.Text(root, width=50, height=2)
keyword_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=show_ciphertext, width=20)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=show_plaintext, width=20)
decrypt_button.pack()

result_text = tk.Text(root, height=10)
result_text.pack()

copy_button = tk.Button(root, text="Copy", command=copy_text, width=20)
copy_button.pack()

root.mainloop()