import os
import shutil
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox

# Function to show popup notifications
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

# Load the Fernet key from file
def load_key(key_filename="key.key"):
    with open(key_filename, "rb") as key_file:
        return key_file.read()

# Backup files to the Downloads folder
def backup_files(file_paths, backup_directory="/home/seed/Downloads"):
    for file_path in file_paths:
        if os.path.exists(file_path):
            shutil.copy(file_path, backup_directory)  # Copy the file to the backup directory
            show_popup(f"Backup is generated for {file_path}!")

# Decrypt files
def decrypt_files(file_paths, fernet_key):
    for file_path in file_paths:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        fernet = Fernet(fernet_key)
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(file_path, "wb") as file:
            file.write(decrypted_data)

        show_popup(f"Backup restored and files decrypted for {file_path}!")

# Restore files from backup
def restore_files(backup_directory="/home/seed/Downloads"):
    files_to_restore = [
        "/home/seed/Desktop/Text_file", 
        "/home/seed/Desktop/Tiger.jpeg"
    ]
    
    for file_path in files_to_restore:
        backup_path = os.path.join(backup_directory, os.path.basename(file_path))

        if os.path.exists(backup_path):
            shutil.copy(backup_path, file_path)  # Restore the backup to the original location
            show_popup(f"Restoring {file_path} from backup!")

    # Load key and decrypt the files
    key = load_key("key.key")
    decrypt_files(files_to_restore, key)

# Check if files are encrypted or not (simple check based on file extension, this can be more sophisticated)
def is_encrypted(file_paths):
    for file_path in file_paths:
        # Check if the file extension is `.enc` (encrypted files assumed to have `.enc` extension)
        if file_path.endswith('.enc'):
            return True
    return False

# Main process
def main():
    files_to_backup = [
        "/home/seed/Desktop/Text_file", 
        "/home/seed/Desktop/Tiger.jpeg"
    ]
    
    # Check if files are encrypted
    if is_encrypted(files_to_backup):
        # If files are encrypted, decrypt and restore them
        restore_files()
    else:
        # If files are not encrypted, perform backup
        backup_files(files_to_backup)

if __name__ == "__main__":
    main()
