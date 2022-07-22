#! /usr/bin/python3

def xor(a, b):
	return chr(ord(a) ^ ord(b))

def encrypt(flag):
	flag_l = list(flag) # turn string into list

	for i in range(len(flag)): # for i in length of str
		char = flag[i]
		for j in range(i + 1, len(flag)): # for all other characters to the right of flag
			char = xor(char, flag[j]) # repeatedly xor char until you get to the end
		flag_l[i] = char

	return ''.join(flag_l) # rejoin flag

def solve():
	enc = open('encrypted.txt', 'r').read()
	enc_l = list(enc)

	for i in range(len(enc) - 1, -1, -1): # iterate through the string backwards
		char = enc[i]
		for j in range(i + 1, len(enc)): # iterate every other character to the right
			char = xor(char, enc_l[j]) # repeatedly xor already known characters

		enc_l[i] = char

	print(''.join(enc_l))
		
if __name__ == '__main__':
	solve()