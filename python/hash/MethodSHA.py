import base64
import hashlib


class MethodSecureHashAlgorithm:

    def __init__(self, st):
        self.str = st
        self.hashed = ""

    def base64(self):
        return base64.b64encode(self.hashed )

    def sha1(self):
        self.hashed = hashlib.sha1(self.str.encode("utf-8")).digest()
        return self.hashed

    def sha224(self):
        self.hashed = hashlib.sha224(self.str.encode("utf-8")).digest()
        return self.hashed

    def sha256(self):
        self.hashed = hashlib.sha256(self.str.encode("utf-8")).digest()
        return self.hashed

    def sha384(self):
        self.hashed = hashlib.sha384(self.str.encode("utf-8")).digest()
        return self.hashed

    def sha512(self):
        self.hashed = hashlib.sha512(self.str.encode("utf-8")).digest()
        return self.hashed

    def test_all(self):
        line_break = "\n=============================MODE=============================\n"
        text = raw_input("Text to hash: ")  # "This is a confidential string"
        self.str = text

        print("Given;\n\t-Text\t\t\t\t'" + str(text) + "'")

        print(line_break.replace("MODE", "Secure Hash Algorithm (SHA1)"))
        print("Before Base64 Encoding: " + self.sha1())
        print("after Base64 Encoding: " + self.base64())

        print(line_break.replace("MODE", "Secure Hash Algorithm (SHA224)"))
        print("Before Base64 Encoding: " + self.sha224())
        print("after Base64 Encoding: " + self.base64())

        print(line_break.replace("MODE", "Secure Hash Algorithm (SHA256)"))
        print("Before Base64 Encoding: " + self.sha256())
        print("after Base64 Encoding: " + self.base64())

        print(line_break.replace("MODE", "Secure Hash Algorithm (SHA384)"))
        print("Before Base64 Encoding: " + self.sha384())
        print("after Base64 Encoding: " + self.base64())

        print(line_break.replace("MODE", "Secure Hash Algorithm (SHA512)"))
        print("Before Base64 Encoding: " + self.sha512())
        print("after Base64 Encoding: " + self.base64())

        print(line_break.replace("MODE", "===="))
        print("ONLY Encoded")

        self.sha1()
        print("Secure Hash Algorithm 1 (SHA1) Base64 Encoding: \t\t" + self.base64())

        self.sha224()
        print("Secure Hash Algorithm 224 (SHA224) Base64 Encoding: \t" + self.base64())

        self.sha256()
        print("Secure Hash Algorithm 256 (SHA256) Base64 Encoding: \t" + self.base64())

        self.sha384()
        print("Secure Hash Algorithm 384 (SHA384) Base64 Encoding: \t" + self.base64())

        self.sha512()
        print("Secure Hash Algorithm 512 (SHA512) Base64 Encoding: \t" + self.base64())
