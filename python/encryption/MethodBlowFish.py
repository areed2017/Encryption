import base64

from Crypto import Random
from Crypto.Cipher import Blowfish


class MethodBlowfish:

    key = b'An arbitrarily long key'

    def __init__(self, iv=None):
        self.initial_vector = iv

    @staticmethod
    def encrypt_ecb(text):
        des = Blowfish.new(MethodBlowfish.key, Blowfish.MODE_ECB)
        text = pad(text, 16)
        encrypted = des.encrypt(text)
        return base64.b64encode(encrypted)

    @staticmethod
    def decrypt_ecb(text):
        text = base64.b64decode(text)
        des = Blowfish.new(MethodBlowfish.key, Blowfish.MODE_ECB)
        decrypted = des.decrypt(text)
        decrypted = remove_padding(decrypted)
        return decrypted

    @staticmethod
    def encrypt_cbc(text, iv=None):
        if iv is None:
            iv = Random.new().read(Blowfish.block_size)

        aes = Blowfish.new(MethodBlowfish.key, Blowfish.MODE_CBC, iv)
        text = pad(text, 16)
        encrypted = aes.encrypt(text)
        return base64.b64encode(iv + encrypted)

    @staticmethod
    def decrypt_cbc(text):
        text = base64.b64decode(text)
        iv = text[0:Blowfish.block_size]
        text = text.replace(iv, "")
        aes = Blowfish.new(MethodBlowfish.key, Blowfish.MODE_CBC, iv)
        decrypted = aes.decrypt(text)
        decrypted = remove_padding(decrypted)
        return decrypted


    @staticmethod
    def test_all():
        line_break = "\n=============================MODE=============================\n"
        text = raw_input("Text to encrypt: ")  # "This is a confidential string"

        des = MethodBlowfish()

        print("Given;\n\t-key\t\t\t\t'" + str(MethodBlowfish.key) + "'\n\t-Text\t\t\t\t'" + str(text) + "'")

        raw_input("Continue...")
        print(line_break.replace("MODE", "Mode ECB"))
        for i in range(3):
            encrypted = des.encrypt_ecb(text)
            print("Encrypted: " + encrypted)
            print("Encrypted Length: " + str(len(encrypted)))
            print("Decrypted: " + des.decrypt_ecb(encrypted))
            print("")

        raw_input("Continue...")
        print(line_break.replace("MODE", "Mode CBC With Random Initial Vector"))
        for i in range(3):
            encrypted = des.encrypt_cbc(text)
            print("Encrypted: " + encrypted)
            print("Encrypted Length: " + str(len(encrypted)))
            print("Decrypted: " + des.decrypt_cbc(encrypted))
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


