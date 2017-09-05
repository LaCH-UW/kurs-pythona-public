#!/usr/bin/python3

import unicodedata

fname = 'lalka-tom-pierwszy.txt'

def wersja_4(fname):
    struct = {}
    with open(fname, encoding="utf8") as fp:
        for word in ''.join(c if unicodedata.category(c) in ('Zs', 'Zl', 'Ll', 'Lu') else ' ' for c in fp.read()).lower().split():
            if word not in struct:
                struct[word] = 1
            else:
                struct[word] += 1

    return struct

def wez_wynik(dane, word):
    word = word.lower()
    return dane[word] if word in dane else 0

def wokulski_helper(fname):
    result = []
    with open(fname) as fp:
        print(''.join(c if unicodedata.category(c) in ('Zs', 'Zl', 'Ll', 'Lu') else '#' for c in fp.read()))

if __name__ == '__main__':
    dane = wersja_4(fname)
    print('Wystąpień Wokulskiego:', wez_wynik(dane, 'Wokulski'))

