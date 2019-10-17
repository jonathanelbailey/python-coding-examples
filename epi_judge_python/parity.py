from test_framework import generic_test

# parity brute force example

# def parity(x):
#     result = 0
#     while x:
#         result ^= x & 1     # equivalent to result = result ^ x & 1
#         x >>= 1             # equivalent to x = x >> 1
#     return result

# parity xor hack example

def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
