# Loop Lover

This challenge is from the BDSEC 2022 CTF. The description read as follows:

> Loops are fun. Are they?

It came with two attached files, `ciphertext.py` and `enc.py`:
```
kU1HlnN1aQMBNNRDzX20M73X9RwUTRz9
```
```python
def f(t):
    c = list(t)
    for i in range(len(t)):
        for j in range(i, len(t) - 1):
            for k in range(j, len(t) - 2):
                c[k], c[k+1] = c[k+1], c[k]
    return "".join(c)

if __name__ == "__main__":
    flag = open("flag.txt", "r").read()
    open("ciphertext.txt", "w").write(f(flag))
```
Essentially, what this does is do a bunch of random loops then performs some weird array assignments and joins them all together. Every other crypto challenge I've done before this (which is not a lot) included bitwise operations, so I was a bit surprised.

I didn't have any clue how to start, so I just pushed it aside as "too hard" and went to a different one. However, when I came back, I more closely examined the `c[k], c[k+1] = c[k+1], c[k]` part, and tried in the python REPL — and it just swaps two adjacent array elements. This was very helpful, and I imagined the problem as [the game where you track the ball under the cup](https://youtu.be/9bto_3Z1dqc) (sorry for explaining it poorly).

Anyways, there is one key property that I noticed. The value of each letter of the input didn't matter. This got me to run a test where I ran a 33 (length of `ciphertext.txt`) sized flag with all unique characters and noted where the different characters went. I then made a dictionary of mapping from output to input, and applying that to the `ciphertext.txt` I got this:
```
QkRTRUN7anU1N19MMDBwX20zXzR3NHl9
```
From here I just threw it in [CyberChef](https://gchq.github.io/CyberChef/) (such a handy tool for a lazy person like me) and turns out it was a base64 encoded string with the flag:
```
BDSEC{ju57_L00p_m3_4w4y}
```

