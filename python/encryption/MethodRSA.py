from random import random


class Key:

    def __init__(self):
        self.modulus = 0
        self.exponent = 1


class KeyFactory:

    PRINT = True

    def __init__(self):
        self.public = None
        self.private = None

    def get_instance(self, algorithm):
        if algorithm is not "rsa":
            return "Algorithm is not supported"

        p = 2  # random.randint(1, 1561115651)
        q = 7  # random.randint(1, 1561115651)
        if self.PRINT:
            print("First Pick Two Random Numbers, \n\tp = " + str(p) + "\n\tq = " + str(q))

        n = p * q
        if self.PRINT:
            print("next multiply p and q, \n\tn = p * q = " + str(n))

        l = (q-1) * (p-1)
        if self.PRINT:
            print("next find l, \n\tl = (q - 1) * (p - 1) = " + str(l))

            #https://hackernoon.com/how-does-rsa-work-f44918df914b

