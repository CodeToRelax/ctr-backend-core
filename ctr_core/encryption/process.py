from cryptography.fernet import Fernet
from ctr_core.aws.aws_ssm import fetch_ssm_config


def load_key(key_name):
    """
    Load the generated key
    """
    return fetch_ssm_config(key_name).decode()


def encrypt_message(message, key_name):
    """
    Encrypts a message
    """
    key = load_key(key_name)
    encoded_message = message.encode()
    f = Fernet(key)
    return f.encrypt(encoded_message)


def decrypt_message(encrypted_message, key_name):
    """
    Decrypts an encrypted message
    """
    key = load_key(key_name)
    f = Fernet(key)
    return f.decrypt(encrypted_message)
