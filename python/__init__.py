from aes import MethodAES, pad

LINE_BREAK = "\n=============================MODE=============================\n"
TEXT = "This is a confidential string"
KEY = "key"
IV = pad("hard code", 16)

aes = MethodAES("key")

print("Given;\n\t-key\t\t\t\t'" + str(KEY) + "'\n\t-Text\t\t\t\t'" + str(TEXT) + "'\n\t-Initial Vector\t\t'" + IV + "'")

raw_input("Continue...")
print(LINE_BREAK.replace("MODE", "Mode ECB"))
for i in range(3):
    encrypted = aes.encrypt_ecb(TEXT)
    print("Encrypted: " + encrypted)
    print("Encrypted Length: " + str(len(encrypted)))
    print("Decrypted: " + aes.decrypt_ecb(encrypted))
    print("")


raw_input("Continue...")
print(LINE_BREAK.replace("MODE", "Mode CBC With Hardcoded Initial Vector"))
for i in range(3):
    encrypted = aes.encrypt_cbc(TEXT, IV)
    print("Encrypted: " + encrypted)
    print("Encrypted Length: " + str(len(encrypted)))
    print("Decrypted: " + aes.decrypt_cbc(encrypted))
    print("")


raw_input("Continue...")
print(LINE_BREAK.replace("MODE", "Mode CBC With Random Initial Vector"))
for i in range(3):
    encrypted = aes.encrypt_cbc(TEXT)
    print("Encrypted: " + encrypted)
    print("Encrypted Length: " + str(len(encrypted)))
    print("Decrypted: " + aes.decrypt_cbc(encrypted))
    print("")

raw_input("Continue...")
print(LINE_BREAK.replace("MODE", "Mode CTR"))
for i in range(3):
    encrypted = aes.encrypt_ctr(TEXT)
    print("Encrypted: " + encrypted)
    print("Encrypted Length: " + str(len(encrypted)))
    print("Decrypted: " + aes.decrypt_ctr(encrypted))
    print("")

raw_input("Continue...")
print(LINE_BREAK.replace("MODE", "Mode CFB With Hardcoded Initial Vector"))
for i in range(3):
    encrypted = aes.encrypt_cfb(TEXT, IV)
    print("Encrypted: " + encrypted)
    print("Encrypted Length: " + str(len(encrypted)))
    print("Decrypted: " + aes.decrypt_cfb(encrypted))
    print("")

raw_input("Continue...")
print(LINE_BREAK.replace("MODE", "Mode CFB With Random Initial Vector"))
for i in range(3):
    encrypted = aes.encrypt_cfb(TEXT)
    print("Encrypted: " + encrypted)
    print("Encrypted Length: " + str(len(encrypted)))
    print("Decrypted: " + aes.decrypt_cfb(encrypted))
    print("")

raw_input("Continue...")
print(LINE_BREAK.replace("MODE", "Mode OFB With Random Initial Vector"))
for i in range(3):
    encrypted = aes.encrypt_ofb(TEXT)
    print("Encrypted: " + encrypted)
    print("Encrypted Length: " + str(len(encrypted)))
    print("Decrypted: " + aes.decrypt_ofb(encrypted))
    print("")