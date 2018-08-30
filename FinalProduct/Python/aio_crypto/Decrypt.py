from sys import argv
from aio_crypto import AES


TYPE = AES
FUNCTION = TYPE.decrypt_ecb
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
            FUNCTION = TYPE.decrypt_ecb
        elif value == "cbc":
            FUNCTION = TYPE.decrypt_cbc
        elif value == "cfb":
            FUNCTION = TYPE.decrypt_cfb
        elif value == "ctr":
            FUNCTION = TYPE.decrypt_ctr
        elif value == "obf":
            FUNCTION = TYPE.decrypt_ofb

    elif key == "key":
        KEY = value

    elif key == "text":
        TEXT = value

print("Decrypting...")
print(FUNCTION(KEY, TEXT))
