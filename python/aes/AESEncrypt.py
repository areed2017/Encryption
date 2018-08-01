import math

from aes.RijndaelSbox import get_sbox


class Encrypt:
    def __init__(self, text, key):
        self.text = text
        self.key = key
        self.state = []
        self.round_keys = [[], [], [], [], [], [], [], [], [], [], []]
        self.rcon = [1]
        for i in range(1, 11):
            value = 2 * self.rcon[i-1]
            if value > 128:
                value = 27
            self.rcon.append(value)
        self.sbox = get_sbox()

    def encrypt(self):
        print("text = '" + str(self.text) + "'")
        print("key = '" + str(self.key) + "'")
        print("key length = " + str(len(self.key) * 8) + " bits")
        print("key length = " + str(len(self.key)) + " bytes\n")

        break_line = "============================================================================\n"

        print(break_line + "Initialize RCon")
        self.print_rcon()

        print(break_line + "Initialize Rijndael's S-Box")
        self.print_sbox()

        print(break_line + "Initialize State Array")
        self.init_values_in_state_arr()
        self.print_state_arr()

        print(break_line + "Initialize the first round with the values of our state array")
        self.init_round_one()
        self.print_round_keys()

        print(break_line + "Initialize the remaining rounds from the previous")
        self.init_remaining_rounds()
        self.print_round_keys()

        print(break_line + "Preform Sub Byte on every row in the state array")
        print("Before: ")
        self.print_state_arr()
        self.sub_byte()
        print("After: ")
        self.print_state_arr()

        print(break_line + "Preform a Row Shift on every row in the state array")
        print("Before: ")
        self.print_state_arr()
        for i in range(len(self.state)):
            self.state[i] = self.shift_row(self.state[i], i)
        print("After: ")
        self.print_state_arr()

        print(break_line + "Preform Mix Columns on every row except the last in the state array")
        print("Before: ")
        self.print_state_arr()
        self.mix_column()
        print("After: ")
        self.print_state_arr()

        print(break_line + "Preform XOR round key on every row in the state array")
        print("Before: ")
        self.print_state_arr()
        self.xor_round_key()
        print("After: ")
        self.print_state_arr()

    def init_values_in_state_arr(self):
        self.state = []
        for i in range(4):
            self.state.append([[], [], [], []])
            for j in range(4):
                location = j + (4 * i)
                value = "-"
                if location < len(self.text):
                    value = self.text[location]
                self.state[i][j] = value

    def sub_byte(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                self.state[i][j] = self.sbox[int(self.state[i][j])]

    @staticmethod
    def shift_row(row, row_index):
        new_row = []
        if row_index == 0:
            new_row = [row[0], row[1], row[2], row[3]]
        if row_index == 1:
            new_row = [row[3], row[0], row[1], row[2]]
        if row_index == 2:
            new_row = [row[2], row[3], row[0], row[1]]
        if row_index == 3:
            new_row = [row[1], row[2], row[3], row[0]]
        return new_row

    def mix_column(self):

        mix = [
            [2, 1, 1, 3],
            [3, 2, 1, 1],
            [1, 3, 2, 1],
            [1, 1, 3, 2],
        ]

        print("Algorithm Used: ")
        print( "[c'0, c'1, c'2, c'3] = " + str(mix) + " * [c0,c1,c2,c3]")

        for row in range( len(self.state)):
            if row == len(self.state) - 1:
                continue
            c = 0
            for column in range( len(self.state[row])):
                c = c ^ self.state[row][column] ^ mix[row][column]
            self.state[row].append(c)

    def xor_round_key(self):
        pass

    def init_round_one(self):
        round = []
        for row in self.state:
            for byte in row:
                round.append(byte)
        self.round_keys[0] = round

    def init_remaining_rounds(self):
        print("Formulas: ")
        print("\tWeight 0 = (key[i-1]:W0) XOR (key[i-1]:W3 Rotated Right by 8 bits) XOR Rcon[i]")
        print("\tWeight j ( when 1 > j > 4 ) = (key[i-1]:Wj) XOR key[i]:W(j-1)")
        for i in range(1, 11):
            self.round_keys[i] = [[], [], [], []]
            self.round_keys[i][0] = self.round_keys[i - 1][0] ^ rotate_right(self.round_keys[i - 1][3], 8) ^ self.rcon[i]
            self.round_keys[i][1] = self.round_keys[i - 1][1] ^ self.round_keys[i][0]
            self.round_keys[i][2] = self.round_keys[i - 1][2] ^ self.round_keys[i][1]
            self.round_keys[i][3] = self.round_keys[i - 1][3] ^ self.round_keys[i][2]

    def print_rcon(self):
        print("\n -RCon-")
        for i in range(len(self.rcon)):
            print("RCon[" + str(i) + "] = " + str(self.rcon[i]))
        print("")

    def print_round_keys(self):
        print("\n -Round Keys-")
        for i in range(len(self.round_keys)):
            print("R" + str(i) + "\t " + str(self.round_keys[i]))
        print("")

    def print_state_arr(self):
        print("\n -State Array-")
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                location = j + (4 * i)
                d = "D" + str(location) + " = "
                tab = "\t\t"
                value = d + str(self.state[i][j])
                if len(str(value)) > 7:
                    tab = "\t"
                print(value + tab, end="")
            print("")
        print("")

    def print_sbox(self):
        print("\n -Rijndael's S-Box-")
        print("\t\t", end="")
        for i in range(int(math.sqrt(len(self.sbox)))):
            print(str(i) + "\t\t", end="")
        print("")
        for i in range(int(math.sqrt(len(self.sbox)))):
            print(str(i) + "\t\t", end="")
            for j in range(int(math.sqrt(len(self.sbox)))):
                location = j + (4 * i)
                print(str(self.sbox[location]) + "\t\t", end="")
            print("")
        print("")


def rotate_right(data, shift_by):
    return (data >> shift_by) | (data << 32 - shift_by) & 0xFFFFFFFF
