atbash = {}

atbash['a'] = 'z'
atbash['b'] = 'y'
atbash['c'] = 'x'
atbash['d'] = 'w'
atbash['e'] = 'v'
atbash['f'] = 'u'
atbash['g'] = 't'
atbash['h'] = 's'
atbash['i'] = 'r'
atbash['j'] = 'q'
atbash['k'] = 'p'
atbash['l'] = 'o'
atbash['m'] = 'n'
atbash['n'] = 'm'
atbash['o'] = 'l'
atbash['p'] = 'k'
atbash['q'] = 'j'
atbash['r'] = 'i'
atbash['s'] = 'h'
atbash['t'] = 'g'
atbash['u'] = 'f'
atbash['v'] = 'e'
atbash['w'] = 'd'
atbash['x'] = 'c'
atbash['y'] = 'b'
atbash['z'] = 'a'
atbash[' '] = ' '


def  main():
    codedmessage = ""
    message = raw_input("What is your message?")
    message = message.lower()
    for i in message:
        codedmessage=codedmessage+(atbash[i])
    print codedmessage


main()
