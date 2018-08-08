import base64
import hashlib


class MethodSecureHashAlgorithm:

    def __init__(self):
        pass

    @staticmethod
    def base64(hashed):
        return base64.b64encode(hashed)

    @staticmethod
    def sha1(text):
        return hashlib.sha1(text.encode("utf-8")).digest()

    @staticmethod
    def sha224(text):
        return hashlib.sha224(text.encode("utf-8")).digest()

    @staticmethod
    def sha256(text):
        return hashlib.sha256(text.encode("utf-8")).digest()

    @staticmethod
    def sha384(text):
        return hashlib.sha384(text.encode("utf-8")).digest()

    @staticmethod
    def sha512(text):
        return hashlib.sha512(text.encode("utf-8")).digest()

    @staticmethod
    def test_all():
        line_break = "\n=============================MODE=============================\n"
        text = raw_input("Text to hash: ")  # "This is a confidential string"
        MethodSecureHashAlgorithm.str = text

        print("Given;\n\t-Text\t\t\t\t'" + str(text) + "'")

        print(line_break.replace("MODE", "Secure Hash Algorithm (SHA1)"))
        print("Before Base64 Encoding: " + MethodSecureHashAlgorithm.sha1(text))
        print("after Base64 Encoding: " + MethodSecureHashAlgorithm.base64(text))

        print(line_break.replace("MODE", "Secure Hash Algorithm (SHA224)"))
        print("Before Base64 Encoding: " + MethodSecureHashAlgorithm.sha224(text))
        print("after Base64 Encoding: " + MethodSecureHashAlgorithm.base64(text))

        print(line_break.replace("MODE", "Secure Hash Algorithm (SHA256)"))
        print("Before Base64 Encoding: " + MethodSecureHashAlgorithm.sha256(text))
        print("after Base64 Encoding: " + MethodSecureHashAlgorithm.base64(text))

        print(line_break.replace("MODE", "Secure Hash Algorithm (SHA384)"))
        print("Before Base64 Encoding: " + MethodSecureHashAlgorithm.sha384(text))
        print("after Base64 Encoding: " + MethodSecureHashAlgorithm.base64(text))

        print(line_break.replace("MODE", "Secure Hash Algorithm (SHA512)"))
        print("Before Base64 Encoding: " + MethodSecureHashAlgorithm.sha512(text))
        print("after Base64 Encoding: " + MethodSecureHashAlgorithm.base64(text))

        print(line_break.replace("MODE", "===="))
        print("ONLY Encoded")

        MethodSecureHashAlgorithm.sha1(text)
        print("Secure Hash Algorithm 1 (SHA1) Base64 Encoding: \t\t" + MethodSecureHashAlgorithm.base64(text))

        MethodSecureHashAlgorithm.sha224(text)
        print("Secure Hash Algorithm 224 (SHA224) Base64 Encoding: \t" + MethodSecureHashAlgorithm.base64(text))

        MethodSecureHashAlgorithm.sha256(text)
        print("Secure Hash Algorithm 256 (SHA256) Base64 Encoding: \t" + MethodSecureHashAlgorithm.base64(text))

        MethodSecureHashAlgorithm.sha384(text)
        print("Secure Hash Algorithm 384 (SHA384) Base64 Encoding: \t" + MethodSecureHashAlgorithm.base64(text))

        MethodSecureHashAlgorithm.sha512(text)
        print("Secure Hash Algorithm 512 (SHA512) Base64 Encoding: \t" + MethodSecureHashAlgorithm.base64(text))
