from matplotlib import pyplot as plt
from matplotlib import rc
from nltk import FreqDist

# ustawiamy czcionkę wspierającą unicode - w domyślnej są tylko znaki ASCII
rc('font', family='DejaVu Sans')

words = ['Wokulski', 'Rzecki', 'subiekt', 'handel', 'sklep']
title1 = 'lalka-tom-pierwszy.txt'
title2 = 'lalka-tom-drugi.txt'

def line_plot(data1, data2, names):
    plt.title("Liczba wystąpień słów")
    plt.xlabel("Próbki")
    plt.ylabel("Liczba wystąpień")

    plt.plot(data1, color='r', label="Dane 1")
    plt.plot(data2, color='b', label="Dane 2")
    plt.legend()

    plt.grid()

    plt.xticks(range(len(names)), names, rotation=90)

    plt.tight_layout()
    plt.savefig('plot.png')
    plt.show()

def count_freq(fname):
    with open(fname) as fp:
        split_words = fp.read().split()
        freq_dist = FreqDist(split_words)
    return freq_dist

def return_values(freq, words):
    result = []
    for s in words:
        result.append(freq[s] if s in freq else 0)
    return result


def make_plot(file1, file2, words):
    freq1 = count_freq(file1)
    freq2 = count_freq(file2)

    res1 = return_values(freq1, words)
    res2 = return_values(freq2, words)

    line_plot(res1, res2, words)

make_plot(title1, title2, words)

# teraz dopisz kod tworzący wykres punktowy zawierający liczbę wystąpień słów z listy
# z punktami różnych kolorów dla pierwszego i drugiego tomu "Lalki"
# dostosuj legendę itp.

# podpowiedź: funkcję plt.plot(y) zastępuje funkcja plt.scatter(x, y)

