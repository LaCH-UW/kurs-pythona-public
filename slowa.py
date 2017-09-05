#!/usr/bin/python3

import time

# jeśli PyCharm podkreśla słowo nltk na czerwono, umieszczenie kursora na tym słowie
#  i naciśnięcie alt+enter powinno dać opcję "Install nltk"
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# matplotlib nie używamy bezpośrednio (korzysta z niego nltk), ale dzięki poniższemu napisowi możemy użyć PyCharma, aby doinstalować paczkę j.w.
import matplotlib

# Należy pobrać pakiet Punkt przed pierwszym użyciem, wołając komendę:
# nltk.download('punkt')

def wersja_poprzednia(fname):
    struct = {}
    with open(fname, encoding="utf8") as fp:
        # funkcja split() dzieli stringa po grupach białych znaków (spacja, tab, enter etc.)
        #  gdy podamy parametr, podzielimy po nim -- np. split(',') podzieli string po przecinkach
        for word in fp.read().split():
            if word not in struct:
                struct[word] = 1
            else:
                struct[word] += 1

    return struct

def wez_wynik(dane, w):
    return dane[w] if w in dane else 0


print("jestem niegrzecznym kodem")

if __name__ == '__main__':

    print("tutaj może być przykład użycia")

