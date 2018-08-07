import base64

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA


class MethodRSA:

    PRIVATE_KEY = "private_key.pem"
    PUBLIC_KEY = "public_key.pem"

    def __init__(self, path_to_keys=""):
        self.path_to_keys = path_to_keys
        self.public_key = RSA.importKey(open(self.path_to_keys + self.PUBLIC_KEY).read())
        self.private_key = RSA.importKey(open(self.path_to_keys + self.PRIVATE_KEY).read())

    def encrypt(self, text):
        cipher = PKCS1_v1_5.new(self.public_key)
        cipher_text = cipher.encrypt(text.encode('utf-8'))
        return base64.b64encode(cipher_text)

    def decrypt(self, text):
        cipher = PKCS1_v1_5.new(self.private_key)
        cipher_text = base64.b64decode(text)
        return cipher.decrypt(cipher_text, None)

    def make_keys(self):
        # paths
        private_key_pem = self.path_to_keys + self.PRIVATE_KEY
        public_key_pem = self.path_to_keys + self.PUBLIC_KEY
        private_key_der = self.path_to_keys + self.PRIVATE_KEY.replace("pem", "der")
        public_key_der = self.path_to_keys + self.PUBLIC_KEY.replace("pem", "der")

        # commands
        print("openssl genrsa -out " + private_key_pem + " 2048")
        print("openssl pkcs8 -topk8 -inform PEM -outform DER -in " + private_key_pem + " -out " + private_key_der + " -nocrypt")
        print("openssl rsa -in " + private_key_pem + " -pubout -outform DER -out " + public_key_der)
        print("openssl rsa -in " + private_key_pem + " -pubout -outform PEM -out " + public_key_pem)

    @staticmethod
    def test_all():
        text = raw_input("Text to encrypt: ")  # "This is a confidential string"

        rsa = MethodRSA("")
        rsa.make_keys()

        print\
            (
                "\n\nGiven;"
                "\n\t-public key \n\t\tmodule=" + str(rsa.public_key.n) + "\n\t\texponent=" + str(rsa.public_key.e) +
                "\n\t-private key\n\t\tmodule=" + str(rsa.private_key.n) + "\n\t\texponent=" + str(rsa.private_key.d) +
                "\n\t-Text=" + str(text)
            )

        encrypted = rsa.encrypt(text)
        print("\n\nEncrypted = " + encrypted)
        decrypted = rsa.decrypt(encrypted)
        print("\n\nDecrypted = " + decrypted)
