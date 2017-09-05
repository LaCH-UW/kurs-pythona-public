#!/usr/bin/python3

import unicodedata
   
# https://en.wikipedia.org/wiki/Unicode_character_property

fname = 'lalka-tom-pierwszy.txt'

def wersja_3(fname):
    struct = {}
    with open(fname, encoding="utf8") as fp:
        for word in ''.join(c for c in f.read() if unicodedata.category(c) in ('Zs', 'Zl', 'Ll', 'Lu')).lower().split():
            if word not in struct:
                struct[word] = 1
            else:
                struct[word] += 1

    return struct

def wez_wynik(dane, word):
    word = word.lower()
    return dane[word] if word in dane else 0

if __name__ == '__main__':
    dane = wersja_3(fname)
    print('Wystąpień Wokulskiego:', wez_wynik(dane, 'Wokulski'))

