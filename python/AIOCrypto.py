import base64
import hashlib

import Crypto
import Crypto.Random
from Crypto.Cipher import PKCS1_v1_5, DES3
from Crypto.Cipher import AES as METHOD_AES
from Crypto.PublicKey import RSA as METHOD_RSA
from Crypto.Cipher import Blowfish as MethodBlowFish
from Crypto.Util import Counter


def encode_utf8(text):
    return text.encode('utf-8')


def encode_base64(text, iv=None):
    if iv is None:
        return base64.b64encode(text)
    return base64.b64encode(iv + text)


def decode_base64(text, iv=None):
    if iv is None:
        return base64.b64decode(text)
    new_text = decode_base64(text)
    iv = new_text[0:METHOD_AES.block_size]
    return new_text.replace(iv, "")


def encrypt(cipher, text):
    return cipher.encrypt(text)


def decrypt(cipher, text):
    return cipher.decrypt(text)


class BlockEncryption:

    def __init__(self):
        pass

    @staticmethod
    def create_key(key):
        hashed = encode_utf8(key)
        return Hash.sha256(hashed)

    @staticmethod
    def create_counter():
        return Counter.new(128)

    @staticmethod
    def create_iv(iv):
        if iv is None:
            iv = Crypto.Random.new().read(METHOD_AES.block_size)
        return iv
    
    @staticmethod
    def pad(text, buffer_size=16):
        number_of_blank_space = buffer_size - len(text) % buffer_size
        character_by_that_value = chr(number_of_blank_space)
        filler = number_of_blank_space * character_by_that_value
        return text + filler

    @staticmethod
    def remove_padding(text):
        last_char = text[len(text) - 1:]
        number_of_blank_space = ord(last_char)
        length_of_text = len(text) - number_of_blank_space
        removed_filter = text[:length_of_text]
        return removed_filter



class AES:

    def __init__(self):
        pass

    @staticmethod
    def encrypt_ecb(key, text):
        var1 = BlockEncryption.create_key(key)
        var2 = BlockEncryption.pad(text)
        var3 = METHOD_AES.new(var1, METHOD_AES.MODE_ECB)
        var4 = encrypt(var3, var2)
        return encode_base64(var4)

    @staticmethod
    def decrypt_ecb(key, text):
        var1 = BlockEncryption.create_key(key)
        var2 = decode_base64(text)
        var3 = METHOD_AES.new(var1, METHOD_AES.MODE_ECB)
        var4 = decrypt(var3, var2)
        return BlockEncryption.remove_padding(var4)

    @staticmethod
    def encrypt_cbc(key, text, iv=None):
        var1 = BlockEncryption.create_iv(iv)
        var2 = BlockEncryption.create_key(key)
        var3 = BlockEncryption.pad(text)
        var4 = METHOD_AES.new(var2, METHOD_AES.MODE_CBC, var1)
        var5 = encrypt(var4, var3)
        return encode_base64(var5, var1)

    @staticmethod
    def decrypt_cbc(key, text):
        var1 = BlockEncryption.create_key(key)
        var2, var3 = decode_base64(text, True)
        var4 = METHOD_AES.new(var1, METHOD_AES.MODE_CBC, var2)
        var5 = decrypt(var4, var3)
        return BlockEncryption.remove_padding(var5)

    @staticmethod
    def encrypt_ctr(key, text):
        var1 = BlockEncryption.create_key(key)
        var2 = BlockEncryption.pad(text)
        var3 = BlockEncryption.create_counter()
        var4 = METHOD_AES.new(var1, METHOD_AES.MODE_CTR, counter=var3)
        var5 = encrypt(var4, var2)
        return encode_base64(var5)

    @staticmethod
    def decrypt_ctr(key, text):
        var1 = BlockEncryption.create_key(key)
        var2 = decode_base64(text, True)
        var3 = BlockEncryption.create_counter()
        var4 = METHOD_AES.new(var1, METHOD_AES.MODE_CTR, counter=var3)
        var5 = decrypt(var4, var2)
        return BlockEncryption.remove_padding(var5)

    @staticmethod
    def encrypt_cfb(key, text, iv=None):
        var1 = BlockEncryption.create_iv(iv)
        var2 = BlockEncryption.create_key(key)
        var3 = BlockEncryption.pad(text)
        var4 = METHOD_AES.new(var2, METHOD_AES.MODE_CFB, var1)
        var5 = encrypt(var4, var3)
        return encode_base64(var5, iv)

    @staticmethod
    def decrypt_cfb(key, text):
        var1 = BlockEncryption.create_key(key)
        var2, var3 = decode_base64(text, True)
        var4 = METHOD_AES.new(var1, METHOD_AES.MODE_CFB, var2)
        var5 = decrypt(var4, var3)
        return BlockEncryption.remove_padding(var5)

    @staticmethod
    def encrypt_ofb(key, text, iv):
        var1 = BlockEncryption.create_iv(iv)
        var2 = BlockEncryption.create_key(key)
        var3 = BlockEncryption.pad(text)
        var4 = METHOD_AES.new(var2, METHOD_AES.MODE_OFB, var1)
        var5 = encrypt(var4, var3)
        return encode_base64(var5, var4)

    @staticmethod
    def decrypt_ofb(key, text):
        var1 = BlockEncryption.create_key(key)
        var2, var3 = decode_base64(text, True)
        var4 = METHOD_AES.new(var1, METHOD_AES.MODE_OFB, var2)
        var5 = decrypt(var4, var3)
        return BlockEncryption.remove_padding(var5)


class RSA:

    def __init__(self):
        pass

    @staticmethod
    def create_key(location):
        return METHOD_RSA.importKey(open(location).read())

    @staticmethod
    def encrypt(text, key_location=None, key=None):
        if key_location is None and key is None:
            print("Either key_location or key must be input to encrypt")
            return
        if key_location is not None and key is not None:
            print("Both a key_location and a key where given, use only one.")
            return

        if key_location is not None:
            key = RSA.create_key(locals())

        var1 = PKCS1_v1_5.new(key)
        var2 = encode_utf8(text)
        var3 = encrypt(var1, var2)
        return encode_base64(var3)

    @staticmethod
    def decrypt(text, key_location=None, key=None):
        if key_location is None and key is None:
            print("Either key_location or key must be input to encrypt")
            return
        if key_location is not None and key is not None:
            print("Both a key_location and a key where given, use only one.")
            return

        if key_location is not None:
            key = RSA.create_key(locals())

        var1 = PKCS1_v1_5.new(key)
        var2 = decode_base64(var1)
        return decrypt(var1, var2)

    @staticmethod
    def instructions_make_keys(location):

        private_key = "private_key.pem"
        public_key = "public_key.pem"

        # paths
        private_key_pem = location + private_key
        public_key_pem = location + public_key
        private_key_der = location + private_key.replace("pem", "der")
        public_key_der = location + public_key.replace("pem", "der")

        # commands
        print("openssl genrsa -out " + private_key_pem + " 2048")
        print("openssl pkcs8 -topk8 -inform PEM -outform DER -in " + private_key_pem + " -out " + private_key_der + " -nocrypt")
        print("openssl rsa -in " + private_key_pem + " -pubout -outform DER -out " + public_key_der)
        print("openssl rsa -in " + private_key_pem + " -pubout -outform PEM -out " + public_key_pem)


class BlowFish:

    def __init__(self):
        pass

    @staticmethod
    def encrypt_ecb(key, text):
        var1 = BlockEncryption.create_key(key)
        var2 = BlockEncryption.pad(text)
        var3 = MethodBlowFish.new(var1, MethodBlowFish.MODE_ECB)
        var4 = encrypt(var3, var2)
        return encode_base64(var4)

    @staticmethod
    def decrypt_ecb(key, text):
        var1 = BlockEncryption.create_key(key)
        var2 = decode_base64(text)
        var3 = MethodBlowFish.new(var1, MethodBlowFish.MODE_ECB)
        var4 = decrypt(var3, var2)
        return BlockEncryption.remove_padding(var4)

    @staticmethod
    def encrypt_cbc(text, key, iv=None):
        var1 = BlockEncryption.create_iv(iv)
        var2 = BlockEncryption.create_key(key)
        var3 = BlockEncryption.pad(text)
        var4 = MethodBlowFish.new(var2, MethodBlowFish.MODE_CBC, var1)
        var5 = encrypt(var4, var3)
        return encode_base64(var5, var1)

    @staticmethod
    def decrypt_cbc(key, text):
        var1 = BlockEncryption.create_key(key)
        var2, var3 = decode_base64(text, True)
        var4 = MethodBlowFish.new(var1, MethodBlowFish.MODE_CBC, var2)
        var5 = decrypt(var4, var3)
        return BlockEncryption.remove_padding(var5)


class TDES:

    def __init__(self):
        pass

    @staticmethod
    def encrypt_ecb(key, text):
        var1 = BlockEncryption.create_key(key)
        var2 = BlockEncryption.pad(text)
        var3 = DES3.new(var1, DES3.MODE_ECB)
        var4 = encrypt(var3, var2)
        return encode_base64(var4)

    @staticmethod
    def decrypt_ecb(key, text):
        var1 = BlockEncryption.create_key(key)
        var2 = encode_base64(text)
        var3 = DES3.new(var1, DES3.MODE_ECB)
        var4 = decrypt(var3, var2)
        return BlockEncryption.remove_padding(var4)

    @staticmethod
    def encrypt_cbc(key, text, iv=None):
        var1 = BlockEncryption.create_iv(iv)
        var2 = BlockEncryption.create_key(key)
        var3 = BlockEncryption.pad(text)
        var4 = DES3.new(var2, DES3.MODE_CBC, var1)
        var5 = encrypt(var4, var3)
        return encode_base64(var5, var1)

    @staticmethod
    def decrypt_cbc(key, text):
        var1 = BlockEncryption.create_key(key)
        var2, var3 = decode_base64(text)
        var4 = DES3.new(var1, DES3.MODE_CBC, var2)
        var5 = decrypt(var4, var3)
        return BlockEncryption.remove_padding(var5)


class Hash:

    def __init__(self):
        pass

    @staticmethod
    def md5(text):
        return hashlib.md5(text).digest()

    @staticmethod
    def sha1(text):
        return hashlib.sha1(text).digest()

    @staticmethod
    def sha224(text):
        return hashlib.sha224(text).digest()

    @staticmethod
    def sha256(text):
        return hashlib.sha256(text).digest()

    @staticmethod
    def sha384(text):
        return hashlib.sha384(text).digest()

    @staticmethod
    def sha512(text):
        return hashlib.sha512(text).digest()
