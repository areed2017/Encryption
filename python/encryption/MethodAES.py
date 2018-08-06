import base64
import hashlib

import Crypto.Random
from Crypto.Cipher import AES
from Crypto.Util import Counter


class MethodAES:
    def __init__(self, key, iv=None):
        self.key = key
        self.initial_vector = iv

    """ MODE ECB """
    def encrypt_ecb(self, text):
        key = hashlib.sha256(self.key.encode('UTF-8')).digest()
        aes = AES.new(key, AES.MODE_ECB)
        text = pad(text, 16)
        encrypted = aes.encrypt(text)
        return base64.b64encode(encrypted)

    def decrypt_ecb(self, text):
        key = hashlib.sha256(self.key.encode("utf-8")).digest()
        text = base64.b64decode(text)
        aes = AES.new(key, AES.MODE_ECB)
        decrypted = aes.decrypt(text)
        decrypted = remove_padding(decrypted)
        return decrypted

    """ MODE CBC """
    def encrypt_cbc(self, text, iv=None):
        if iv is None:
            iv = Crypto.Random.new().read(AES.block_size)

        key = hashlib.sha256(self.key.encode('UTF-8')).digest()
        aes = AES.new(key, AES.MODE_CBC, iv)
        text = pad(text, 16)
        encrypted = aes.encrypt(text)
        return base64.b64encode(iv + encrypted)

    def decrypt_cbc(self, text):
        key = hashlib.sha256(self.key.encode("utf-8")).digest()
        text = base64.b64decode(text)
        iv = text[0:AES.block_size]
        text = text.replace(iv, "")
        aes = AES.new(key, AES.MODE_CBC, iv)
        decrypted = aes.decrypt(text)
        decrypted = remove_padding(decrypted)
        return decrypted

    """ MODE CTR """
    def encrypt_ctr(self, text):
        key = hashlib.sha256(self.key.encode('UTF-8')).digest()
        iv = Counter.new(128)
        aes = AES.new(key, AES.MODE_CTR, counter=iv)
        text = pad(text, 16)
        encrypted = aes.encrypt(text)
        return base64.b64encode(encrypted)

    def decrypt_ctr(self, text):
        key = hashlib.sha256(self.key.encode("utf-8")).digest()
        text = base64.b64decode(text)
        iv = Counter.new(128)
        aes = AES.new(key, AES.MODE_CTR, counter=iv)
        decrypted = aes.decrypt(text)
        decrypted = remove_padding(decrypted)
        return decrypted

    """ MODE CFB """
    def encrypt_cfb(self, text, iv=None):
        if iv is None:
            iv = Crypto.Random.new().read(AES.block_size)

        key = hashlib.sha256(self.key.encode('UTF-8')).digest()
        aes = AES.new(key, AES.MODE_CFB, iv)
        text = pad(text, 16)
        encrypted = aes.encrypt(text)
        return base64.b64encode(iv + encrypted)

    def decrypt_cfb(self, text):
        key = hashlib.sha256(self.key.encode("utf-8")).digest()
        text = base64.b64decode(text)
        iv = text[0:AES.block_size]
        text = text.replace(iv, "")
        aes = AES.new(key, AES.MODE_CFB, iv)
        decrypted = aes.decrypt(text)
        decrypted = remove_padding(decrypted)
        return decrypted

    """ MODE OFB """
    def encrypt_ofb(self, text, iv=None):
        if iv is None:
            iv = Crypto.Random.new().read(AES.block_size)

        key = hashlib.sha256(self.key.encode('UTF-8')).digest()
        aes = AES.new(key, AES.MODE_OFB, iv)
        text = pad(text, 16)
        encrypted = aes.encrypt(text)
        return base64.b64encode(iv + encrypted)

    def decrypt_ofb(self, text):
        key = hashlib.sha256(self.key.encode("utf-8")).digest()
        text = base64.b64decode(text)
        iv = text[0:AES.block_size]
        text = text.replace(iv, "")
        aes = AES.new(key, AES.MODE_OFB, iv)
        decrypted = aes.decrypt(text)
        decrypted = remove_padding(decrypted)
        return decrypted

    @staticmethod
    def test_all():
        line_break = "\n=============================MODE=============================\n"
        text = raw_input("Text to encrypt: ")  # "This is a confidential string"
        key = raw_input("Key for encryption: ")  # "key"
        iv = pad("hard code", 16)

        aes = MethodAES("key")

        print("Given;\n\t-key\t\t\t\t'" + str(key) + "'\n\t-Text\t\t\t\t'" + str(
            text) + "'\n\t-Initial Vector\t\t'" + iv + "'")

        raw_input("Continue...")
        print(line_break.replace("MODE", "Mode ECB"))
        for i in range(3):
            encrypted = aes.encrypt_ecb(text)
            print("Encrypted: " + encrypted)
            print("Encrypted Length: " + str(len(encrypted)))
            print("Decrypted: " + aes.decrypt_ecb(encrypted))
            print("")

        raw_input("Continue...")
        print(line_break.replace("MODE", "Mode CBC With Hardcoded Initial Vector"))
        for i in range(3):
            encrypted = aes.encrypt_cbc(text, iv)
            print("Encrypted: " + encrypted)
            print("Encrypted Length: " + str(len(encrypted)))
            print("Decrypted: " + aes.decrypt_cbc(encrypted))
            print("")

        raw_input("Continue...")
        print(line_break.replace("MODE", "Mode CBC With Random Initial Vector"))
        for i in range(3):
            encrypted = aes.encrypt_cbc(text)
            print("Encrypted: " + encrypted)
            print("Encrypted Length: " + str(len(encrypted)))
            print("Decrypted: " + aes.decrypt_cbc(encrypted))
            print("")

        raw_input("Continue...")
        print(line_break.replace("MODE", "Mode CTR"))
        for i in range(3):
            encrypted = aes.encrypt_ctr(text)
            print("Encrypted: " + encrypted)
            print("Encrypted Length: " + str(len(encrypted)))
            print("Decrypted: " + aes.decrypt_ctr(encrypted))
            print("")

        raw_input("Continue...")
        print(line_break.replace("MODE", "Mode CFB With Hardcoded Initial Vector"))
        for i in range(3):
            encrypted = aes.encrypt_cfb(text, iv)
            print("Encrypted: " + encrypted)
            print("Encrypted Length: " + str(len(encrypted)))
            print("Decrypted: " + aes.decrypt_cfb(encrypted))
            print("")

        raw_input("Continue...")
        print(line_break.replace("MODE", "Mode CFB With Random Initial Vector"))
        for i in range(3):
            encrypted = aes.encrypt_cfb(text)
            print("Encrypted: " + encrypted)
            print("Encrypted Length: " + str(len(encrypted)))
            print("Decrypted: " + aes.decrypt_cfb(encrypted))
            print("")

        raw_input("Continue...")
        print(line_break.replace("MODE", "Mode OFB With Random Initial Vector"))
        for i in range(3):
            encrypted = aes.encrypt_ofb(text)
            print("Encrypted: " + encrypted)
            print("Encrypted Length: " + str(len(encrypted)))
            print("Decrypted: " + aes.decrypt_ofb(encrypted))
            print("")


def pad(text, buffer_size):
    number_of_blank_space = buffer_size - len(text) % buffer_size
    character_by_that_value = chr(number_of_blank_space)
    filler = number_of_blank_space * character_by_that_value
    return text + filler


def remove_padding(text):
    last_char = text[len(text) - 1:]
    number_of_blank_space = ord(last_char)
    length_of_text = len(text) - number_of_blank_space
    removed_filter = text[:length_of_text]
    return removed_filter


