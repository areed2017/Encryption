
class Bit:
    MAX_BIT = 8

    def __init__(self, arr):
        if type(arr) is list:
            self.value = 0
            reverse_order = []
            if type(arr) is str:
                arr = list(arr)
                print(arr)
            for val in reversed(arr):
                reverse_order.append(val)
            for i in range(len(reverse_order)):
                self.value += int(reverse_order[i]) * (pow(2, i))
        else:
            self.value = int(arr)

    def __int__(self):
        return self.value

    def __str__(self):
        value = ""
        values = self.to_array()
        for val in values:
            value += str(val)
        return str(value) + " (" + str(self.value) + ")"

    def to_array(self):
        value = []
        remainder = self.value
        for i in range(self.MAX_BIT):
            v = pow(2, self.MAX_BIT - 1 - i)
            if remainder < v:
                value.append(0)
            else:
                value.append(1)
                remainder -= v
        return value

    def add(self, i):
        self.value += int(i)

    def sub(self, i):
        self.value -= int(i)


class SuperSimpleAES:

    @staticmethod
    def rotl8(x, shift):
        return (pow(Bit.MAX_BIT, 3) - 1) & ((x << shift) | (x >> (Bit.MAX_BIT - shift)))

    def __init__(self, key, text):
        if type(text) is not Bit:
            text = Bit(text)

        self.state = []
        self.key = key
        self.text = text

    def encrypt(self):
        print("Establishing State Array")
        self.state = [[Bit(self.key[0]), Bit(self.key[1])], [Bit(self.key[2]), Bit(self.key[3])]]
        self.print_state()

        print("\n\nApplying Substitution, (SBox)")
        for row in range(len(self.state)):
            for col in range(len(self.state[row])):
                value = int(self.state[row][col])
                print(str(value) + " => ", end="")
                value = self.rotl8(value, 1)
                print(str(value))
                self.state[row][col] = value
        self.print_state()

        print("\n\nApplying Right Shift")
        temp = self.state[0][0]
        self.state[0][0] = self.state[0][1]
        self.state[0][1] = temp
        temp = self.state[1][0]
        self.state[1][0] = self.state[1][1]
        self.state[1][1] = temp
        self.print_state()

        print("\n\n")

    def print_sbox(self):
        print("-Substitution Table (S-Box)- ")
        for bit in range(pow(Bit.MAX_BIT, 2)):
            print(str(Bit(bit)) + " => " + str(Bit(self.rotl8(bit, 1))))

    def print_state(self):
        print("-State Array-")
        for i in range( len(self.state) ):
            for j in range( len(self.state[i])):
                print(str(self.state[i][j]) + "\t\t", end="")
            print("")


ssa = SuperSimpleAES("aes1".encode('utf-8'), 5)
ssa.encrypt()
