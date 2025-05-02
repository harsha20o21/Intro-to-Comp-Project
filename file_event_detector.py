import os
import shutil
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox

def show_popup(message):
    root = tk.Tk()
    root.title("Backup/Restore Process")
    root.geometry("300x150")
    label = tk.Label(root, text=message, font=("Arial", 12))
    label.pack(pady=20)
    ok_button = tk.Button(root, text="OK", command=root.quit)
    ok_button.pack()
    root.mainloop()
    root.destroy()

def load_key(key_filename="key.key"):
    with open(key_filename, "rb") as key_file:
        return key_file.read()

def backup_files(file_paths, backup_directory="/home/seed/Downloads"):
    for file_path in file_paths:
        if os.path.exists(file_path):
            shutil.copy(file_path, backup_directory)
            show_popup(f"Backup is generated for {file_path}!")

def decrypt_files(file_paths, fernet_key):
    for file_path in file_paths:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        fernet = Fernet(fernet_key)
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(decrypted_data)
        show_popup(f"Backup restored and files decrypted for {file_path}!")

def restore_files(backup_directory="/home/seed/Downloads"):
    files_to_restore = [
        "/home/seed/Desktop/Text_file", 
        "/home/seed/Desktop/Tiger.jpeg"
    ]
    for file_path in files_to_restore:
        backup_path = os.path.join(backup_directory, os.path.basename(file_path))
        if os.path.exists(backup_path):
            shutil.copy(backup_path, file_path)
            show_popup(f"Restoring {file_path} from backup!")
    key = load_key("key.key")
    decrypt_files(files_to_restore, key)

def is_encrypted(file_paths):
    for file_path in file_paths:
        if file_path.endswith('.enc'):
            return True
    return False

def main():
    files_to_backup = [
        "/home/seed/Desktop/Text_file", 
        "/home/seed/Desktop/Tiger.jpeg"
    ]
    if is_encrypted(files_to_backup):
        restore_files()
    else:
        backup_files(files_to_backup)

if __name__ == "__main__":
    main()
