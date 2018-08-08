import string
from random import choice
from matplotlib import pyplot
from timeit import default_timer as timer
from encryption import MethodAES
from encryption.MethodBlowFish import MethodBlowfish
from encryption.MethodDES3 import MethodDES3

texts = dict()
fluke_tolerance = .1


def is_fluke(point, other_points):
    if len(other_points) < 1:
        return False
    last_point = other_points[len(other_points) - 1]
    delta = abs(last_point - point)
    return delta > fluke_tolerance


def graph_data(method, graph, color, label, _range):
    byte_size = []
    time_took = []

    for i in range(5, _range):
        bytes_in_text = 0
        text = ""
        if str(i) in text:
            text = texts[str(i)]
        while bytes_in_text <= i:
            text += choice(string.ascii_letters)
            bytes_in_text = len(text.encode('utf-8'))
        texts[str(i)] = text

        avg_time = 0
        for j in range(100):
            start = timer()
            method(text)
            end = timer()
            avg_time += (end - start) * 1000
        time_elapsed = avg_time / 10

        if time_elapsed > 0 and not is_fluke(time_elapsed, time_took):
            time_took.append(time_elapsed)
            byte_size.append(bytes_in_text)

    graph.plot(byte_size, time_took, color=color, label=label, linewidth=1)


def graph_data2(encryption, decryption, graph, color, label, _range):
    byte_size = []
    time_took = []

    for i in range(5, _range):
        bytes_in_text = 0
        text = ""
        if str(i) in text:
            text = texts[str(i)]
        while bytes_in_text <= i:
            text += choice(string.ascii_letters)
            bytes_in_text = len(text.encode('utf-8'))
        texts[str(i)] = text

        avg_time = 0
        text = encryption(text)
        for j in range(100):
            start = timer()
            decryption(text)
            end = timer()
            avg_time += (end - start) * 1000
        time_elapsed = avg_time / 10

        if time_elapsed > 0 and not is_fluke(time_elapsed, time_took):
            time_took.append(time_elapsed)
            byte_size.append(bytes_in_text)

    graph.plot(byte_size, time_took, color=color, label=label, linewidth=1)


cycles = 500

# aes = MethodAES.MethodAES("This is a test key for aes")
# graph_data(aes.encrypt_ecb, pyplot, 'r', 'AES-128-ECB', cycles)
# graph_data(aes.encrypt_cbc, pyplot, 'r', 'AES-128-CBC', cycles)
# graph_data(aes.encrypt_cfb, pyplot, 'r', 'AES-128-CFB', cycles)
# graph_data(aes.encrypt_ctr, pyplot, 'c', 'AES-128-CTR', cycles)
# graph_data(aes.encrypt_ofb, pyplot, 'm', 'AES-128-OFB', cycles)
# pyplot.title("AES Decryption Speeds")
# pyplot.ylabel('Time In milliseconds Took To Process')
# pyplot.xlabel('Size In Bytes Of Text Encrypted')
# pyplot.legend()
# pyplot.figure()
#
# rsa = MethodRSA()
# graph_data(rsa.encrypt, pyplot, 'k', "RSA", cycles)
#
# pyplot.title("RSA Decryption Speeds")
# pyplot.ylabel('Time In milliseconds Took To Process')
# pyplot.xlabel('Size In Bytes Of Text Encrypted')
# pyplot.figure()

# des = MethodDES3()
# graph_data(des.encrypt_ecb, pyplot, 'b', "DES-3-ECB", cycles)
# graph_data(des.encrypt_ecb, pyplot, 'g', "DES-3-CBC", cycles)
# pyplot.title("DES-3 encryption Speeds")
# pyplot.ylabel('Time In milliseconds Took To Process')
# pyplot.xlabel('Size In Bytes Of Text Hash')
# pyplot.legend()
# pyplot.figure()

blowfish = MethodBlowfish()
graph_data2(blowfish.encrypt_ecb, blowfish.decrypt_ecb, pyplot, 'b', 'Blowfish-ECB', cycles)
graph_data2(blowfish.encrypt_cbc, blowfish.encrypt_cbc, pyplot, 'g', "Blowfish-CBC", cycles)

pyplot.title("Blowfish Decryption Speeds")
pyplot.ylabel('Time In milliseconds Took To Process')
pyplot.xlabel('Size In Bytes Of Text Hash')
pyplot.legend()
pyplot.figure()

graph_data(blowfish.encrypt_ecb, pyplot, 'b', 'Blowfish-ECB', cycles)
graph_data(blowfish.encrypt_cbc, pyplot, 'g', "Blowfish-CBC", cycles)

pyplot.title("Blowfish Encryption Speeds")
pyplot.ylabel('Time In milliseconds Took To Process')
pyplot.xlabel('Size In Bytes Of Text Hash')
pyplot.legend()

# graph_data(MethodSecureHashAlgorithm.sha1, pyplot, 'g', "Secure Hashing Algorithm 1", cycles)
# pyplot.title("Secure Hashing Algorithm 1 Speeds")
# pyplot.ylabel('Time In milliseconds Took To Process')
# pyplot.xlabel('Size In Bytes Of Text Hash')
# pyplot.figure()
# pyplot.subplot(221)

# graph_data(MethodSecureHashAlgorithm.sha224, pyplot, 'r', "Secure Hashing Algorithm 224", cycles)
# pyplot.title("Secure Hashing Algorithm 224 Speeds")
# pyplot.ylabel('Time In milliseconds Took To Process')
# pyplot.xlabel('Size In Bytes Of Text Hash')
# pyplot.figure()
# pyplot.subplot(222)

# graph_data(MethodSecureHashAlgorithm.sha256, pyplot, 'c', "Secure Hashing Algorithm 256", cycles)
# pyplot.title("Secure Hashing Algorithm 256 Speeds")
# pyplot.ylabel('Time In milliseconds Took To Process')
# pyplot.xlabel('Size In Bytes Of Text Hash')
# pyplot.figure()
# pyplot.subplot(223)

# graph_data(MethodSecureHashAlgorithm.sha384, pyplot, 'm', "Secure Hashing Algorithm 384", cycles)
# pyplot.title("Secure Hashing Algorithm 384 Speeds")
# pyplot.ylabel('Time In milliseconds Took To Process')
# pyplot.xlabel('Size In Bytes Of Text Hash')
# pyplot.figure()
# pyplot.subplot(224)

# graph_data(MethodSecureHashAlgorithm.sha512, pyplot, 'k', "Secure Hashing Algorithm 512", cycles)
# pyplot.title("Secure Hashing Algorithm 512 Speeds")
# pyplot.ylabel('Time In milliseconds Took To Process')
# pyplot.xlabel('Size In Bytes Of Text Hash')
# pyplot.figure()
# pyplot.subplot(211)

# graph_data(MethodMessageDigest.md5, pyplot, 'b', "Message Digest 5", cycles)
# pyplot.title("Message Digest 5 Speeds")
# pyplot.ylabel('Time In milliseconds Took To Process')
# pyplot.xlabel('Size In Bytes Of Text Hash')
# pyplot.figure()
# pyplot.subplot(212)

pyplot.show()
