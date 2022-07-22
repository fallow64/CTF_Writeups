# Dominoes

This challenge from BDSec 2022 was pretty interesting. It's not hard at all, and pretty much everybody with some experience would get it, but I just wanna document my experience.

## The Challenge

The description read as follows:
> My classmate Zeem is into loops and basic bitwise operations. Interestingly, he thought he could create an encryption algorithm and use it to protect his files.
> 
> Can you bypass his encryption to get the flag?

The two attached files were `encrypted.txt`, the encrypted key, and `encrypt.py`, the script for encryption (this version is refactored):
```python
def encrypt(input_str):
	result = list(input_str)

	for i in range(len(input_str)):
		char = input_str[i]
		for j in range(i + 1, len(input_str)):
			char = chr(ord(char) ^ ord(input_str[j]))		
		result[i] = char

	return "".join(result)

def main():
	flag = open("flag.txt", "r").read()
	enc_flag = encrypt(flag)

	f = open("encrypted.txt", "w")
	f.write(enc_flag)
	f.close()

if __name__ == "__main__":
	main()
```
The encryption method used here is basically to take each character, XOR the character to the right of it, then take the output of that and XOR or it with the, bla bla bla until the end.

My immediate thought was the last character. Because it has nothing to XOR to the right of it, it would stay the same. In the encrypted flag the last character was a right bracket, most likely from the flag format. So, from here, we just work backwards.

Here is an excerpt of the end: `I}N}`
From here, you do `'N' XOR '}'`, which is 3, then `'}' XOR '3 XOR '}'`, which is 3, then `'I' XOR '3' XOR '3' XOR '}` (which is 4). This part may be confusing to read, but it was also very confusing to code. I guess the best explanation is that instead of using the encoded string to get the next thing to XOR, you use the one that you are generating.

Anyways, using this you can decrypt the file and get the resulting flag:
```
BDSEC{n0t_50_e45y_hUh?_433}
```
If you wanna take a lesson from this, it's probably that experience helps. Even thought I've only played 1 CTF ever before this, I still knew to look out for the end of linear-iterative bitwise encryptions (which is a fancy word that I probably made up and also used wrong).