from __future__ import print_function
#Note: the proper name of this doc is ();#!, but windows doesn't let certain symbols occur in filenames

def lex(prog):
    return [x for x in prog]

def run(prog):
    loops = []
    prog = lex(prog)
    i = 0
    while i < len(prog):
        c = prog[i]

        if c == '(':
            loops.append(i)
        elif c == ')':
            i = loops.pop()-1
        elif c == ':':
            print(prog[i+1], end='')
        elif c == ';':
            prog[i+2] = raw_input()[0]
        elif c == '+':
            prog[i-1] = chr(ord(prog[i-1])+1)
        elif c == '-':
            prog[i-1] = chr(ord(prog[i-1])-1)
        elif c == '#':
            loops = run(raw_input()[0])
        elif c == '?':
            if c in '():;+-#?!':
                return loops
        elif c == '!':
            return loops
        i+=1
    return loops

run(raw_input('Program: '))
