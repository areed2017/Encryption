import base64
from Crypto.Cipher import AES
import hashlib

from encryption.Utillities import pad, unpad


def encrypt(text, key):
    key = hashlib.sha256(key.encode('UTF-8')).digest()

    iv = pad("softgenetics", 16)
    aes = AES.new(key, AES.MODE_CBC, iv)

    text = pad(text, 16)
    encrypted = aes.encrypt(text)
    return base64.b64encode(encrypted)


def decrypt(text, key):
    key = hashlib.sha256(key.encode("utf-8")).digest()
    text = base64.b64decode(text)
    iv = pad("softgenetics", 16)
    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypted = aes.decrypt(text)
    decrypted = unpad(decrypted, 16)
    return decrypted
