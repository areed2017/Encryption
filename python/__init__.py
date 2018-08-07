import hashlib
from sys import argv

from encryption.MethodAES import MethodAES
from encryption.MethodRSA import MethodRSA

from hash.MethodMessageDigest import MethodMessageDigest
from hash.MethodSHA import MethodSecureHashAlgorithm


for arg in argv:
    if arg.lower() == "-aes":
        MethodAES("", "").test_all()
    elif arg.lower() == "-md":
        MethodMessageDigest("").test_all()
    elif arg.lower() == "-sha":
        MethodSecureHashAlgorithm("").test_all()
    elif arg.lower() == "-rsa":
        MethodRSA().test_all()
