from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
import os

def load_key(key_filename="key.key"):
    with open(key_filename, "rb") as key_file:
        return key_file.read()

def decrypt_file(file_path, fernet_key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    fernet = Fernet(fernet_key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    show_popup(f"File {file_path} decrypted successfully.")

def show_popup(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Decryption Complete", message)
    root.quit()

def main():
    key = load_key("key.key")
    decrypt_file("/home/seed/Desktop/Text_file", key)
    decrypt_file("/home/seed/Desktop/Tiger.jpeg", key)

if __name__ == "__main__":
    main()
