from sys import argv
from aio_crypto import AES


TYPE = AES
FUNCTION = TYPE.encrypt_ecb
KEY = "No Key"
TEXT = "No text"


for arg in argv:
    if "=" not in arg:
        continue

    key = arg.split("=")[0].lower()
    value = arg.split("=")[1]

    if key == "type":
        value = value.lower()
        if value is "aes":
            TYPE = AES

    elif key == "mode":
        value = value.lower()
        if value == "ecb":
            FUNCTION = TYPE.encrypt_ecb
        elif value == "cbc":
            FUNCTION = TYPE.encrypt_cbc
        elif value == "cfb":
            FUNCTION = TYPE.encrypt_cfb
        elif value == "ctr":
            FUNCTION = TYPE.encrypt_ctr
        elif value == "obf":
            FUNCTION = TYPE.encrypt_ofb

    elif key == "key":
        KEY = value

    elif key == "text":
        TEXT = value

print("Encrypting...")
print(FUNCTION(KEY, TEXT))
