#! /usr/bin/python3

def encode(t):
    c = list(t)
    for i in range(len(t)):
        for j in range(i, len(t) - 1):
            for k in range(j, len(t) - 2):
                c[k], c[k+1] = c[k+1], c[k]
    return ''.join(c)

def solve():
    example_in = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456'
    example_out = encode(example_in)

    mapping = {}
    for i, char in enumerate(example_in):
        mapping[example_out.index(char)] = i # maps Cipher Index : Flag Index

    real_in = open('ciphertext.txt', 'r').read()
    result = [' '] * len(real_in)

    for i, char in enumerate(real_in):
        result[mapping[i]] = char

    print(''.join(result))

if __name__ == '__main__':
    solve()