# pyprison
This challenge from ImaginaryCTF 2022, which is my first ever CTF. It's pretty simple, and I wouldn't really call this a writeup, it's just documenting my stupidity.

We are given one file, `main.py`:
```python
while True:
  a = input(">>> ")
  assert all(n in "()abcdefghijklmnopqrstuvwxyz" for n in a)
  exec(a)
```

This is just a python sandbox with the restriction that all commands have to be undercase letters or paranthesis, and no spaces are allowed. I had no clue how to approach this at the start. When I first saw this, I immediately thought that the tools that we have are builtins or tuples.

The first idea I had is that we could import things using some sort of tuple and `chr()` then call it, but I honestly had no idea what to do. My mind was stuck on building integers, using `chr()`, and then using import or something like that.

So, I got to thinking — if I wanted to create "any" integer I wanted, how could I do that? Well, I could use `len()`, but how could I control the length of something. Then it hit me — `input()`! So now I could make any character or letter I wanted, but I had no clue how to make multiple. I was pretty much stuck.

But then I realized my stupidity. I could've just done `exec(input())` the entire time. I don't think I need to explain in detail the rest of my steps.

```
ictf{pyprison_more_like_python_as_a_service_12b19a09}
```

So that was the rollercoaster of my stupidity, I hope you enjoyed it. While you're at it, go check out ImaginaryCTF. They hold daily CTF challenges and have a monthly leaderboard. They're pretty cool!