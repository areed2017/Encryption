from Utillities import make_keys
from sys import argv
import encryption.RSA as RSA
import encryption.AES as AES
import codes


TYPE = None
TEXT = None
KEY = None
ENCRYPT = False

RSA.set_public_default_key("public_key.pem")
RSA.set_private_default_key("private_key.pem")

requestCode = codes.RegistrationRequestCode("796440f98c3513b1e0706b907d256882", "")
print("Code: " + requestCode.encrypt())


for i in range(1, len(argv), 2):
    if argv[i] == "-t":
        TYPE = argv[i + 1]
    elif argv[i] == "-c":
        make_keys(argv[i+1])
    elif argv[i] == "-e":
        ENCRYPT = True
        TEXT = argv[i + 1]
    elif argv[i] == "-d":
        ENCRYPT = False
        TEXT = argv[i + 1]
    elif argv[i] == "-k":
        KEY = argv[i + 1]
    else:
        print(argv[i])

res = ""
if TYPE is None:
    pass
elif TYPE.lower() == "aes":
    if KEY is None or TEXT is None:
        print("Both a key and text are required to encrypt and decrypt with aes")
    elif ENCRYPT:
        print("Encrypted: " + AES.encrypt(TEXT, KEY))
    else:
        print("Decrypted: " + AES.decrypt(TEXT, KEY))

elif TYPE.lower() == "rsa":
    if ENCRYPT:
        if KEY is not None:
            print("Encrypted: " + RSA.encrypt(TEXT, KEY))
        else:
            print("Encrypted: " + RSA.encrypt(TEXT))
    else:
        if KEY is not None:
            print("Decrypted: " + RSA.decrypt(TEXT, KEY))
        else:
            print("Decrypted: " + RSA.decrypt(TEXT))
else:
    print("Encryption type not set, use -t *TYPE(AES/RSA)* to set the type")

quit()