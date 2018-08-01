from aes.AESEncrypt import Encrypt
import os


key = os.urandom(16)
encrypt = Encrypt("Text", key)
encrypt.encrypt()
quit()

#
# def step_1():
#     print("STEP 1: Acquire Key And Plan Text")
#     # text = input("Input a string to encrypt: ")
#     text = "test"
#     key = ""
#     for i in range(int(256/8)):
#         key += random.choice(string.ascii_letters)
#
#     key = Key(key)
#     print("key: " + str(key))
#     print("key length:" + str(len(key)* 8) + " bits" )
#     print("Text: " + text)
#
#     return text
#
#
# def step_2(text):
#     print("STEP 2: Cypher")
#     print("\tData from the string to encrypt is placed within an array")
#     text = list(text)
#     print("\tText: " + str(text))
#
#     print("\tMap each letter's ascii value to its corresponding value in Rijndael's S-Box")
#     sbox = getSbox()
#     for i in range(len(text)):
#         text[i] = chr(sbox[ord(text[i])])
#     print("\tText: " + str(text))
#
#


# text = step_1()
# step_2(text)
#



