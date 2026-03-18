import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def generate_key_from_password(password: str, salt: bytes):
    """Generate a key from password using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),   # use SHA256 for hashing
        length=32,    
        salt=salt,          # unique salt for each encryption
        iterations=100000,  # number of iterations
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key
# encrypt and decrypt functions
def encrypt_data(data, password):
    salt = os.urandom(16)
    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)

    encrypted = fernet.encrypt(data)
    return salt + encrypted  # store salt with data

def decrypt_data(data, password):
    salt = data[:16]
    encrypted_data = data[16:]    #extract salt and encrypted data

    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)

    return fernet.decrypt(encrypted_data)