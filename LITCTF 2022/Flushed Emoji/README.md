# Flushed Emoji

This challenge is from LITCTF 2022. I'm pretty new to CTFs myself, but I thought it was pretty cool, so I'm going to write about it.

The description reads as follows:
> Flushed emojis are so cool! Learn more about them [here](http://litctf.live:31781/)!

You are given two flask servers, one for the primary site and one for a data server. I won't put those here, but they will be in the repository.

The main site has a button with a form that "steals" your username and password and displays the password back to you. It prevents you from putting periods in the password field, but that's easily mitigated. From here, you just use SSTI injection in the password field to get RCE.

```python
{{lipsum['__globals__']['os']['popen']('ls')['read']()}}
```

Now, we can view the source code of the running server and find the IP for data server is `172.24.0.8:8080` (a private IP, which I was too dumb to realize at first).

The data server just selects any users that match the same username and password. This is pretty much SQL injection 101 material. However, it only returns `True` or `False`, based on whether or not it selected anything. The query ends up like this:

```SQL
SELECT * FROM users WHERE username='{username}' AND password='{password}'
```

Using the RCE to run python from the command line, you can use the requests library to POST to the data server. Remember though, you can't use periods, so I just encoded them as `\x2E`. From here, it's just bog-standard blind SQL injection. Check the first character of the password against all printable characters, and if it matches move on to the next one. You can see the full implementation in the `bruteforce()` function of `solve.py`. The SQL query ends up looking like this (curly brackets are python variables):

```SQL
SELECT * FROM users WHERE username='XXXXX' AND password='' OR substr(password, {str(index)}, 1)='{char}'/*'
```

Using this, you get the flag:

```
LITCTF{flush3d_3m0ji_o.0}
```

---------------------------------------

## Notes

1. The python code is horrendous. I tried to clean it up a bit, however it's still very messy to follow. Just make sure to put your hazmat suit on before reading it.
2. In my implementation, I make a request to the server for each SQL query. This is very inefficient and I could've ran a python file on the server that did the bruteforcing (I'm pretty sure bruteforcing is the correct term) and just printed the final flag. But, my implementation works well enough and that's the most important thing.
3. The main site checks whether or not you put the correct username and password and says

    > OMG you are like so good at guessing our flag I am lowkey jealoussss.
    
    if you got it right. However, you cannot put the flag in the password field as it contains periods. Also, it filters out any non-alphanumeric characters anyway, so the curly brackets, period, and underscore would've been removed. This doesn't effect the challenge, just an small oversight for a meaningless message.