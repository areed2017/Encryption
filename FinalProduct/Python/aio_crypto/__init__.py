import base64
import hashlib

import Crypto
import Crypto.Random
from Crypto.Cipher import PKCS1_v1_5 as Pk
from Crypto.Cipher import DES3 as MD
from Crypto.Cipher import AES as MA
from Crypto.PublicKey import RSA as MR
from Crypto.Cipher import Blowfish as Meb
from Crypto.Util import Counter as Co


def u8(text):
    return text.encode('utf-8')


def eb64(text, iv=None):
    if iv is None:
        return base64.b64encode(text)
    return base64.b64encode(iv + text)


def db64(text, iv=None):
    if iv is None:
        return base64.b64decode(text)
    new_text = db64(text)
    iv = new_text[0:MA.block_size]
    return new_text.replace(iv, "")


def epr(cipher, text):
    return cipher.encrypt(text)


def dpr(cipher, text):
    return cipher.decrypt(text)


class BE:

    def __init__(self):
        pass

    @staticmethod
    def ck(k):
        h = u8(k)
        return Hash.sha256(h)

    @staticmethod
    def cc():
        return Co.new(128)

    @staticmethod
    def p(var1, var2=16):
        nobs = var2 - len(var1) % var2
        cab = chr(nobs)
        filler = nobs * cab
        return var1 + filler

    @staticmethod
    def rp(var1):
        lc = var1[len(var1) - 1:]
        nobs = ord(lc)
        lot = len(var1) - nobs
        rf = var1[:lot]
        return rf

    @staticmethod
    def ci(var1):
        if var1 is None:
            return Crypto.Random.new().read(MA.block_size)
        return var1


class AES:

    def __init__(self):
        pass

    @staticmethod
    def encrypt_ecb(key, text):
        var1 = BE.ck(key)
        var2 = BE.p(text)
        var3 = MA.new(var1, MA.MODE_ECB)
        var4 = epr(var3, var2)
        return eb64(var4)

    @staticmethod
    def decrypt_ecb(key, text):
        var1 = BE.ck(key)
        var2 = db64(text)
        var3 = MA.new(var1, MA.MODE_ECB)
        var4 = dpr(var3, var2)
        return BE.rp(var4)

    @staticmethod
    def encrypt_cbc(key, text, iv=None):
        var1 = BE.ci(iv)
        var2 = BE.ck(key)
        var3 = BE.p(text)
        var4 = MA.new(var2, MA.MODE_CBC, var1)
        var5 = epr(var4, var3)
        return eb64(var5, var1)

    @staticmethod
    def decrypt_cbc(key, text):
        var1 = BE.ck(key)
        var2, var3 = db64(text, True)
        var4 = MA.new(var1, MA.MODE_CBC, var2)
        var5 = dpr(var4, var3)
        return BE.rp(var5)

    @staticmethod
    def encrypt_ctr(key, text):
        var1 = BE.ck(key)
        var2 = BE.p(text)
        var3 = BE.cc()
        var4 = MA.new(var1, MA.MODE_CTR, counter=var3)
        var5 = epr(var4, var2)
        return eb64(var5)

    @staticmethod
    def decrypt_ctr(key, text):
        var1 = BE.ck(key)
        var2 = db64(text, True)
        var3 = BE.cc()
        var4 = MA.new(var1, MA.MODE_CTR, counter=var3)
        var5 = dpr(var4, var2)
        return BE.rp(var5)

    @staticmethod
    def encrypt_cfb(key, text, iv=None):
        var1 = BE.ci(iv)
        var2 = BE.ck(key)
        var3 = BE.p(text)
        var4 = MA.new(var2, MA.MODE_CFB, var1)
        var5 = epr(var4, var3)
        return eb64(var5, iv)

    @staticmethod
    def decrypt_cfb(key, text):
        var1 = BE.ck(key)
        var2, var3 = db64(text, True)
        var4 = MA.new(var1, MA.MODE_CFB, var2)
        var5 = dpr(var4, var3)
        return BE.rp(var5)

    @staticmethod
    def encrypt_ofb(key, text, iv=None):
        var1 = BE.ci(iv)
        var2 = BE.ck(key)
        var3 = BE.p(text)
        var4 = MA.new(var2, MA.MODE_OFB, var1)
        var5 = epr(var4, var3)
        return eb64(var5, var1)

    @staticmethod
    def decrypt_ofb(key, text):
        var1 = BE.ck(key)
        var2, var3 = db64(text, True)
        var4 = MA.new(var1, MA.MODE_OFB, var2)
        var5 = dpr(var4, var3)
        return BE.rp(var5)


class RSA:

    def __init__(self):
        pass

    @staticmethod
    def create_key(location):
        return MR.importKey(open(location).read())

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

        var1 = Pk.new(key)
        var2 = u8(text)
        var3 = epr(var1, var2)
        return eb64(var3)

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

        var1 = Pk.new(key)
        var2 = db64(var1)
        return dpr(var1, var2)

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
        var1 = BE.ck(key)
        var2 = BE.p(text)
        var3 = Meb.new(var1, Meb.MODE_ECB)
        var4 = epr(var3, var2)
        return eb64(var4)

    @staticmethod
    def decrypt_ecb(key, text):
        var1 = BE.ck(key)
        var2 = db64(text)
        var3 = Meb.new(var1, Meb.MODE_ECB)
        var4 = dpr(var3, var2)
        return BE.rp(var4)

    @staticmethod
    def encrypt_cbc(text, key, iv=None):
        var1 = BE.ci(iv)
        var2 = BE.ck(key)
        var3 = BE.p(text)
        var4 = Meb.new(var2, Meb.MODE_CBC, var1)
        var5 = epr(var4, var3)
        return eb64(var5, var1)

    @staticmethod
    def decrypt_cbc(key, text):
        var1 = BE.ck(key)
        var2, var3 = db64(text, True)
        var4 = Meb.new(var1, Meb.MODE_CBC, var2)
        var5 = dpr(var4, var3)
        return BE.rp(var5)


class TDES:

    def __init__(self):
        pass

    @staticmethod
    def encrypt_ecb(key, text):
        var1 = BE.ck(key)
        var2 = BE.p(text)
        var3 = MD.new(var1, MD.MODE_ECB)
        var4 = epr(var3, var2)
        return eb64(var4)

    @staticmethod
    def decrypt_ecb(key, text):
        var1 = BE.ck(key)
        var2 = eb64(text)
        var3 = MD.new(var1, MD.MODE_ECB)
        var4 = dpr(var3, var2)
        return BE.rp(var4)

    @staticmethod
    def encrypt_cbc(key, text, iv=None):
        var1 = BE.ci(iv)
        var2 = BE.ck(key)
        var3 = BE.p(text)
        var4 = MD.new(var2, MD.MODE_CBC, var1)
        var5 = epr(var4, var3)
        return eb64(var5, var1)

    @staticmethod
    def decrypt_cbc(key, text):
        var1 = BE.ck(key)
        var2, var3 = db64(text)
        var4 = MD.new(var1, MD.MODE_CBC, var2)
        var5 = dpr(var4, var3)
        return BE.rp(var5)


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
