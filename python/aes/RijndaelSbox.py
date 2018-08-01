
def rotl8(x, shift):
    return 0xff & (((x) << (shift)) | ((x) >> (8 - (shift))))


def get_sbox():
    sbox = [None] * 256
    p = q = 1
    first_time = True

    # loop invariant: p * q == 1 in the Galois field
    while p != 1 or first_time:  # To simulate a do/while loop
        # multiply p by 3
        p = p ^ (p << 1) ^ (0x1B if p & 0x80 else 0)
        p = p & 0xff

        # divide q by 3
        q ^= q << 1
        q ^= q << 2
        q ^= q << 4
        q ^= 0x09 if q & 0x80 else 0
        q = q & 0xff

        # compute the affine transformation
        x_formed = q ^ rotl8(q, 1) ^ rotl8(q, 2) ^ rotl8(q, 3) ^ rotl8(q, 4)

        sbox[p] = x_formed ^ 0x63
        first_time = False

    # 0 is a special case since it has no inverse
    sbox[0] = 0x63

    return sbox