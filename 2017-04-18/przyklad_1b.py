#!/usr/bin/python3

fname = 'lalka-tom-pierwszy.txt'

def wersja_2(fname):
    struct = {}
    with open(fname, encoding="utf8") as fp:
        for line in fp:
            for word in line.split():
                word = word.lower().replace('.', '').replace('?', '').replace('!', '').replace('…', '')
                if word not in struct:
                    struct[word] = 1
                else:
                    struct[word] += 1

    return struct

def wez_wynik(dane, word):
    # czemu nie działam??
    return dane[word] if word in dane else 0

if __name__ == '__main__':
    dane = wersja_2(fname)
    print('Wystąpień Wokulskiego:', wez_wynik(dane, 'Wokulski'))

