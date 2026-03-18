import os
from utils.crypto_utils import encrypt_data, decrypt_data
from utils.file_handler import read_file, write_file

# folder encryption and decryption functions
def encrypt_folder(folder_path, password):
    for root, _, files in os.walk(folder_path):
        for file in files:
            path = os.path.join(root, file) # encrypt each file in folder
            data = read_file(path)
            if data:
                encrypted = encrypt_data(data, password) # encrypt data
                write_file(path + ".enc", encrypted)

def decrypt_folder(folder_path, password):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".enc"):
                path = os.path.join(root, file) # decrypt each .enc file in folder
                data = read_file(path)
                if data:
                    try:
                        decrypted = decrypt_data(data, password) # decrypt data
                        new_path = path.replace(".enc", "_dec")
                        write_file(new_path, decrypted)
                    except:
                        pass