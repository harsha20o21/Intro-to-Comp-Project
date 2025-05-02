from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
import os

def generate_key():
    return Fernet.generate_key()

def save_key(key, key_filename="key.key"):
    with open(key_filename, "wb") as key_file:
        key_file.write(key)

def encrypt_file(file_path, fernet_key):
    with open(file_path, "rb") as file:
        file_data = file.read()
    fernet = Fernet(fernet_key)
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    show_popup(f"File {file_path} encrypted successfully.")

def show_popup(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Encryption Complete", message)
    root.quit()

def main():
    key = generate_key()
    save_key(key)
    encrypt_file("/home/seed/Desktop/Text_file", key)
    encrypt_file("/home/seed/Desktop/Tiger.jpeg", key)

if __name__ == "__main__":
    main()
