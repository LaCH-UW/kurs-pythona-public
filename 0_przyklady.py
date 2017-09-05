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

fname = 'lalka-tom-pierwszy.txt'

# liczenie słów w wersji naiwnej
def wersja_1(fname, searched_word):
    count = 0
    # otwieramy plik o kodowaniu utf8 do odczytu; fp to wskażnik plikowy,
    #  który zostanie zwolniony na końcu kontekstu (tam, gdzie kończy się wcięcie pod with)
    with open(fname, encoding="utf8") as fp:
        for line in fp:
            for word in line.split():
                if word == searched_word:
                    count += 1

    return count

def zapisz_slownik(dane):
    # otwieramy plik o kodowaniu utf8 i nazwie "tmp_out.txt" do zapisu;
    #  uwaga: jeśli plik wcześniej istniał, jego zawartość zostanie zniszczona
    with open('tmp_out.txt', 'w', encoding="utf8") as fp:
        for key, value in dane.items():
            fp.write(str(key) + ':' + str(value) + '\n');

# tablicowanie + czytanie całego pliku (a nie po linijce)
def wersja_3(fname):
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

def wersja_nltk(fname):
    with open(fname, encoding="utf8") as fp:
        raw_text = fp.read()
        # korzystamy z funkcji tokenizującej nltk -- naiwnej jeszcze, ale są lepsze
        word_tokens = word_tokenize(raw_text)
        # dedykowany słownik do częstości -- ma ciekawe metody, jak np. plot()
        freq_dist = FreqDist(word_tokens)
    return freq_dist

# tą liczbą można modyfikować czas działania programu
n = 30

with open(fname, encoding="utf8") as fp:
    # wyciągamy z pliku n wyrazów z pominięciem pierwszych 10 (bo są nudne -- "Bolesław", "Prus" etc.)
    searched = fp.read().split()[10:n+10]

print(searched)

# czas działania liniowy względem n (n rośnie dwa razy, program działa dwa razy dłużej)
result = []
begin = time.time()
for s in searched:
    result.append(wersja_1(fname, s))
print('wersja 1:', time.time() - begin)

print('====')

# czas działania asymptotycznie stały n (n rośnie dwa razy, program działa pomijalnie dłużej)
result = []
begin = time.time()
dane_3 = wersja_3(fname)
for s in searched:
    result.append(dane_3[s] if s in dane_3 else 0)
print('wersja 3:',time.time() - begin)

print('====')

zapisz_slownik(dane_3)

# działa dłużej niż powyższe, ale asymptotycznie zachowuje się jak wersja_3
result = []
begin = time.time()
dane_nltk = wersja_nltk(fname)
for s in searched:
    result.append(dane_nltk[s] if s in dane_nltk else 0)
print('wersja nltk:',time.time() - begin)

# rysujemy pierwsze 20 "słów" z rozkładu wyprodukowanego przez NLTK;
#  uwaga z dużymi liczbami albo wołaniem plot() bez argumentów!
dane_nltk.plot(20)



