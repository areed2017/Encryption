import math
import string
import threading
import time
from random import choice
from timeit import default_timer as timer

from matplotlib import pyplot

from encryption import MethodAES, MethodRSA, MethodDES3, MethodBlowFish
from hash import MethodMessageDigest, MethodSHA

texts = dict()
fluke_tolerance = .1
prog = dict()
accuracy = 100




def is_fluke(point, other_points):
    if len(other_points) < 1:
        return False
    last_point = other_points[len(other_points) - 1]
    delta = abs(last_point - point)
    return delta > fluke_tolerance


def graph_data(method, graph, color, label, _range, progress_loc):
    byte_size = []
    time_took = []

    for i in range(1, _range):
        bytes_in_text = 0
        text = ""
        if str(i) in text:
            text = texts[str(i)]
        while bytes_in_text <= i:
            text += choice(string.ascii_letters)
            bytes_in_text = len(text.encode('utf-8'))
        texts[str(i)] = text

        avg_time = 0
        for j in range(accuracy):
            start = timer()
            method(text)
            end = timer()
            avg_time += (end - start) * 1000
        time_elapsed = avg_time / accuracy

        if time_elapsed > 0 and not is_fluke(time_elapsed, time_took):
            time_took.append(time_elapsed)
            byte_size.append(bytes_in_text)
        prog[progress_loc] = math.floor((float(i)/float(_range)) * 100.0)

    graph.plot(byte_size, time_took, color=color, label=label, linewidth=1)


def graph_data2(encryption, decryption, graph, color, label, _range, progress_loc):
    byte_size = []
    time_took = []

    for i in range(0, _range):
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
        for j in range(accuracy):
            start = timer()
            decryption(text)
            end = timer()
            avg_time += (end - start) * 1000
        time_elapsed = avg_time / accuracy

        if time_elapsed > 0 and not is_fluke(time_elapsed, time_took):
            time_took.append(time_elapsed)
            byte_size.append(bytes_in_text)

        prog[progress_loc] = math.floor((float(i)/float(_range)) * 100.0)

    graph.plot(byte_size, time_took, color=color, label=label, linewidth=1)


y_label = 'Time Spent to Process(Milliseconds)'
x_label = 'Size of Text Process (Bytes )'
cycles = 245
done = False


def progress():
    while not done:
        time.sleep(1)
        for key in prog:
            print("'" + key + "'\t\t" + str(prog[key]) + "%     \r")


def save_graphs_encryption(save_location, title, methods):
    colors = ['g', 'b', 'c', 'm', 'y', 'k']
    print("Creating Graph for '" + title + "'")
    prog[save_location] = 0

    for i in range(len(methods)):
        graph_data(methods[i], pyplot, colors[i % len(colors)], methods[i].__name__.replace("encrypt_", ""), cycles, save_location)
    pyplot.title(title)

    if len(methods) > 1:
        pyplot.legend()
    pyplot.ylabel(y_label)
    pyplot.xlabel(x_label)
    pyplot.savefig(save_location)
    pyplot.figure()
    print("Graph for '" + title + "' Completed")
    del prog[save_location]


def save_graphs_decryption(save_location, title, encryption_methods, decryption_methods):
    colors = ['g', 'b', 'c', 'm', 'y', 'k']
    print("Creating Graph for '" + title + "'")
    prog[save_location] = 0
    for i in range(len(encryption_methods)):
        graph_data2(encryption_methods[i], decryption_methods[i], pyplot, colors[i % len(colors)], decryption_methods[i].__name__.replace("decrypt", ""), cycles, save_location)

    pyplot.title(title)
    if len(encryption_methods) > 1:
        pyplot.legend()
    pyplot.ylabel(y_label)
    pyplot.xlabel(x_label)
    pyplot.savefig(save_location)
    pyplot.figure()
    print("Graph for '" + title + "' Completed")
    del prog[save_location]


threading.Thread(target=progress).start()


""" ------ AES ----- """
aes = MethodAES.MethodAES("This is a test key for aes")

save_graphs_encryption("../imgs/aes/encryption/ECB.png", "AES-128-ECB Encryption Speeds", [aes.encrypt_ecb])
save_graphs_encryption("../imgs/aes/encryption/CBC.png", "AES-128-CBC Encryption Speeds", [aes.encrypt_cbc])
save_graphs_encryption("../imgs/aes/encryption/CFB.png", "AES-128-CFB Encryption Speeds", [aes.encrypt_cfb])
save_graphs_encryption("../imgs/aes/encryption/CTR.png", "AES-128-CTR Encryption Speeds", [aes.encrypt_ctr])
save_graphs_encryption("../imgs/aes/encryption/OFB.png", "AES-128-OFB Encryption Speeds", [aes.encrypt_ofb])
save_graphs_encryption("../imgs/aes/encryption/All.png", "AES-128 Encryption Speeds",
                       [
                           aes.encrypt_ecb,
                           aes.encrypt_cbc,
                           aes.encrypt_cfb,
                           aes.encrypt_ctr,
                           aes.encrypt_ofb
                       ])
pyplot.close()

save_graphs_decryption("../imgs/aes/decryption/ECB.png", "AES-128-ECB Encryption Speeds", [aes.encrypt_ecb], [aes.decrypt_ecb])
save_graphs_decryption("../imgs/aes/decryption/CBC.png", "AES-128-CBC Encryption Speeds", [aes.encrypt_cbc], [aes.decrypt_cbc])
save_graphs_decryption("../imgs/aes/decryption/CFB.png", "AES-128-CFB Encryption Speeds", [aes.encrypt_cfb], [aes.decrypt_cfb])
save_graphs_decryption("../imgs/aes/decryption/CTR.png", "AES-128-CTR Encryption Speeds", [aes.encrypt_ctr], [aes.decrypt_ctr])
save_graphs_decryption("../imgs/aes/decryption/OFB.png", "AES-128-OFB Encryption Speeds", [aes.encrypt_ofb], [aes.decrypt_ofb])
save_graphs_decryption("../imgs/aes/decryption/All.png", "AES-128 Decryption Speeds",
                       [
                           aes.encrypt_ecb,
                           aes.encrypt_cbc,
                           aes.encrypt_cfb,
                           aes.encrypt_ctr,
                           aes.encrypt_ofb
                       ],
                       [
                           aes.decrypt_ecb,
                           aes.decrypt_cbc,
                           aes.decrypt_cfb,
                           aes.decrypt_ctr,
                           aes.decrypt_ofb
                       ])
pyplot.close()


""" ----- Triple DES ----- """
des = MethodDES3.MethodDES3()
save_graphs_encryption("../imgs/des3/encryption/ECB.png", "Triple DES ECB Encryption Speeds", [des.encrypt_ecb])
save_graphs_encryption("../imgs/des3/encryption/CBC.png", "Triple DES CBC Encryption Speeds", [des.encrypt_cbc])
save_graphs_encryption("../imgs/des3/encryption/All.png", "Triple DES Encryption Speeds",
                       [
                            des.encrypt_ecb,
                            des.encrypt_cbc
                       ])
pyplot.close()

save_graphs_decryption("../imgs/des3/decryption/ECB.png", "Triple DES ECB Encryption Speeds", [des.encrypt_ecb],
                       [des.decrypt_ecb])
save_graphs_decryption("../imgs/des3/decryption/CBC.png", "Triple DES CBC Encryption Speeds", [des.encrypt_cbc],
                       [des.decrypt_cbc])

save_graphs_decryption("../imgs/des3/decryption/All.png", "Triple DES Decryption Speeds",
                       [
                           des.encrypt_ecb,
                           des.encrypt_cbc
                       ],
                       [
                           des.decrypt_ecb,
                           des.decrypt_cbc
                       ])
pyplot.close()


""" ----- Blowfish ----- """
blowfish = MethodBlowFish.MethodBlowfish()
save_graphs_encryption("../imgs/blowfish/encryption/ECB.png", "Blowfish ECB Encryption Speeds", [blowfish.encrypt_ecb])
save_graphs_encryption("../imgs/blowfish/encryption/CBC.png", "Blowfish CBC Encryption Speeds", [blowfish.encrypt_cbc])
save_graphs_encryption("../imgs/blowfish/encryption/All.png", "Blowfish Encryption Speeds",
                       [
                           blowfish.encrypt_ecb,
                           blowfish.encrypt_cbc
                       ])
pyplot.close()

save_graphs_decryption("../imgs/blowfish/decryption/ECB.png", "Blowfish ECB Encryption Speeds", [blowfish.encrypt_ecb],
                       [blowfish.decrypt_ecb])
save_graphs_decryption("../imgs/blowfish/decryption/CBC.png", "Blowfish CBC Encryption Speeds", [blowfish.encrypt_cbc],
                       [blowfish.decrypt_cbc])

save_graphs_decryption("../imgs/blowfish/decryption/All.png", "Blowfish Decryption Speeds",
                       [
                           blowfish.encrypt_ecb,
                           blowfish.encrypt_cbc
                       ],
                       [
                           blowfish.decrypt_ecb,
                           blowfish.decrypt_cbc
                       ])
pyplot.close()


""" ------ RSA ----- """
rsa = MethodRSA.MethodRSA()
save_graphs_encryption("../imgs/rsa/encryption/All.png", "RSA Encryption Speeds", [rsa.encrypt])
save_graphs_decryption("../imgs/rsa/decryption/All.png", "RSA Decryption Speeds", [rsa.encrypt], [rsa.decrypt])
pyplot.close()

""" ------ Comparing ----- """
save_graphs_encryption("../imgs/comparing/encryption/All.png", "Encryption Speeds",
                       [
                            aes.encrypt_ecb,
                            aes.encrypt_cbc,
                            rsa.encrypt,
                            des.encrypt_ecb,
                            des.encrypt_cbc,
                            blowfish.encrypt_ecb,
                            blowfish.encrypt_cbc,
                       ])
pyplot.close()
save_graphs_decryption("../imgs/comparing/decryption/All.png", "Decryption Speeds",
                       [
                            aes.encrypt_ecb,
                            aes.encrypt_cbc,
                            rsa.encrypt,
                            des.encrypt_ecb,
                            des.encrypt_cbc,
                            blowfish.encrypt_ecb,
                            blowfish.encrypt_cbc,
                       ],
                       [
                            aes.decrypt_ecb,
                            aes.decrypt_cbc,
                            rsa.decrypt,
                            des.decrypt_ecb,
                            des.decrypt_cbc,
                            blowfish.decrypt_ecb,
                            blowfish.decrypt_cbc,
                       ],
                       )
pyplot.close()

save_graphs_encryption("../imgs/comparing/encryption/ECB.png", "ECB Encryption Speeds",
                       [
                            aes.encrypt_ecb,
                            des.encrypt_ecb,
                            blowfish.encrypt_ecb,
                       ])
pyplot.close()

save_graphs_decryption("../imgs/comparing/decryption/ECB.png", "ECB Decryption Speeds",
                       [
                            aes.encrypt_ecb,
                            des.encrypt_ecb,
                            blowfish.encrypt_ecb,
                       ],
                       [
                            aes.decrypt_ecb,
                            des.decrypt_ecb,
                            blowfish.decrypt_ecb,
                       ],
                       )
pyplot.close()

save_graphs_encryption("../imgs/comparing/encryption/CBC.png", "CBC Encryption Speeds",
                       [
                            aes.encrypt_cbc,
                            des.encrypt_cbc,
                            blowfish.encrypt_cbc,
                       ])
pyplot.close()

save_graphs_decryption("../imgs/comparing/decryption/CBC.png", "CBC Decryption Speeds",
                       [
                            aes.encrypt_cbc,
                            des.encrypt_cbc,
                            blowfish.encrypt_cbc,
                       ],
                       [
                            aes.decrypt_cbc,
                            des.decrypt_cbc,
                            blowfish.decrypt_cbc,
                       ],
                       )
pyplot.close()

"""   --- MD5 ---   """
md5 = MethodMessageDigest.MethodMessageDigest()
save_graphs_encryption("../imgs/md5/md5.png", "MD5 Hashing Speeds",
                       [
                            md5.md5,
                       ])

pyplot.close()
"""   --- SHA ---   """
sha = MethodSHA.MethodSecureHashAlgorithm()
save_graphs_encryption("../imgs/sha/All.png", "SHA Hashing Speeds",
                       [
                            sha.sha1,
                            sha.sha224,
                            sha.sha256,
                            sha.sha384,
                            sha.sha512,
                       ])
pyplot.close()

save_graphs_encryption("../imgs/sha/sha1.png", "SHA-1 Hashing Speeds", [sha.sha1])
save_graphs_encryption("../imgs/sha/sha224.png", "SHA-224 Hashing Speeds", [sha.sha224])
save_graphs_encryption("../imgs/sha/sha256.png", "SHA-256 Hashing Speeds", [sha.sha256])
save_graphs_encryption("../imgs/sha/sha384.png", "SHA-384 Hashing Speeds", [sha.sha384])
save_graphs_encryption("../imgs/sha/sha512.png", "SHA-512 Hashing Speeds", [sha.sha512])
pyplot.close()

# noinspection PyRedeclaration
done = True

