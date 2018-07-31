import base64
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from Crypto.PublicKey import RSA


DEFAULT_KEY_PATH_PRIVATE = ""
DEFAULT_KEY_PATH_PUBLIC = ""


def set_public_default_key(key_path):
    global DEFAULT_KEY_PATH_PUBLIC
    DEFAULT_KEY_PATH_PUBLIC = key_path


def set_private_default_key(key_path):
    global DEFAULT_KEY_PATH_PRIVATE
    DEFAULT_KEY_PATH_PRIVATE = key_path


def encrypt(text, key_path=None):
    if key_path is None:
        global DEFAULT_KEY_PATH_PUBLIC
        key_path = DEFAULT_KEY_PATH_PUBLIC
    rsa_key = RSA.importKey(open(key_path).read())
    cipher = PKCS1_v1_5.new(rsa_key)
    cipher_text = cipher.encrypt(text.encode('utf-8'))
    return base64.b64encode(cipher_text)


def decrypt(text, key_path=None):
    if key_path is None:
        global DEFAULT_KEY_PATH_PRIVATE
        key_path = DEFAULT_KEY_PATH_PRIVATE
    print(text)
    rsa_key = RSA.importKey(open(key_path).read())
    cipher = PKCS1_v1_5.new(rsa_key)
    cipher_text = base64.b64decode(text)
    print(cipher_text)
    return cipher.decrypt(cipher_text)
