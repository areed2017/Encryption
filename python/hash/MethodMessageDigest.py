import base64
import hashlib

from Crypto.Hash import MD5


class MethodMessageDigest:

    def __init__(self, str):
        self.str = str

    def md5(self):
        return hashlib.md5(self.str.encode("utf-8")).digest()

    def base64_md5(self):
        return base64.b64encode(self.md5())

    def test_all(self):
        line_break = "\n=============================MODE=============================\n"
        text = raw_input("Text to hash: ")  # "This is a confidential string"
        self.str = text

        print (hashlib.algorithms)

        print("Given;\n\t-Text\t\t\t\t'" + str(text) + "'")

        print(line_break.replace("MODE", "Message Digest 5 (MD5)"))
        print("Before Base64 Encoding: " + self.md5())
        print("after Base64 Encoding: " + self.base64_md5())

