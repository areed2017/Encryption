import base64
import hashlib

from Crypto.Hash import MD5


class MethodMessageDigest:

    def __init__(self):
        pass

    @staticmethod
    def md5(text):
        return hashlib.md5(text.encode("utf-8")).digest()

    @staticmethod
    def base64_md5(text):
        return base64.b64encode(MethodMessageDigest.md5(text))

    @staticmethod
    def test_all(self, text):
        line_break = "\n=============================MODE=============================\n"
        text = raw_input("Text to hash: ")  # "This is a confidential string"

        print("Given;\n\t-Text\t\t\t\t'" + str(text) + "'")

        print(line_break.replace("MODE", "Message Digest 5 (MD5)"))
        print("Before Base64 Encoding: " + MethodMessageDigest.md5(text))
        print("after Base64 Encoding: " + MethodMessageDigest.base64_md5(text))

