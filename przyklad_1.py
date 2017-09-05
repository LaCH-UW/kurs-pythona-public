#!/usr/bin/python3

from slowa import wersja_poprzednia
import slowa

fname = 'lalka-tom-pierwszy.txt'

searched = ['jak', 'Jak', 'Wokulski', 'Wokulski.']

# bez prefiksu 'slowa', bo zrobiliśmy "from . import ."
dane = wersja_poprzednia(fname)
for s in searched:
    print(s, slowa.wez_wynik(dane, s))


# spróbuj teraz wypisać do pliku 'Rzecki.txt' liczbę wystąpień słowa 'Rzecki'

